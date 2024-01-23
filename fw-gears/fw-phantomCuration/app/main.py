"""Main module."""
import flywheel
import logging
import os
import json

log = logging.getLogger(__name__)

def find_files():

    """Runs the phantom curation algorithm.

    Args:
        input_image: FISP acquistion dicom.
    
    Returns:
    output_dir: Phantom QA project.


    """

    log.info("Starting the process curation process...")
    
    # Read config.json file
    p = open('/flywheel/v0/config.json')
    config = json.loads(p.read())

    # Read API key in config file
    api_key = (config['inputs']['api-key']['key'])
    fw = flywheel.Client(api_key=api_key)

    # Get the Phantom QA project
    phantom = fw.lookup("dev/Phantom_QA")

    # Get the parent id from inputs in config file
    input_container_type = config.get("inputs", {}).get("dicom-input", {}).get("hierarchy", {}).get("type")
    if input_container_type == 'session':
        session_id = config.get("inputs", {}).get("dicom-input", {}).get("hierarchy", {}).get("id")
        session_container = fw.get(session_id)
        print("running from session level...")
        print("session_container is : ", session_container.label)

        project_id = session_container.parents.project
        project = fw.get(project_id)
        print("project_container is : ", project.label)
        
    else:
        parent_id = config.get("inputs", {}).get("dicom-input", {}).get("hierarchy", {}).get("id")
        parent = fw.get(parent_id)
        print(parent.parents)
        project_id = parent.parents.project
        project = fw.get(project_id)
        print("project_container is : ", project.label)

    for subject in project.subjects.iter():
        subLabel = subject.label
        if subLabel.startswith('137-00') or subLabel.startswith('13700') or subLabel.startswith('137-00'):
            print("Looks like a phantom scan: ", subLabel)
            
            for session in subject.sessions.iter():
                print("session: ", session.label)
                # Add a tag to a session
                session.add_tag('Phantom')

                # Create new subject in Phantom QA project
                try:
                    phantom_subject = phantom.add_subject(label=subject.label)                                
                except:
                    # If subject already exists, reload it
                    phantom_subject = phantom.subjects.find_one("label=" + subject.label)
                    
                # Move session to Phantom QA project
                dest_sub = phantom_subject.reload()
                try:
                    print("Moving session: ", session.label)
                    session.update({'subject': dest_sub.id})
                except:
                    print("Error moving session")
                    continue
    log.info("Exiting main...")
    return 0

