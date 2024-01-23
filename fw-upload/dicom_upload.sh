# Flywheel login
fw login ${FW_CLI_API_KEY}

# Command to move to Flywheel
fw ingest dicom ~/Desktop/Anon global_map "PRISMA-Demo" --detect-duplicates --verbose

# Explanation of the command:
# fw is the command line interface for Flywheel
# ingest is the command to upload data to Flywheel
# dicom is the type of data being uploaded
# ~/Desktop/Anon is the path to the data being uploaded (in this case, the Anon folder on the Desktop)
# global_map is the name of the "group" that the data will be uploaded to
# "PRISMA-Demo" is the name of the project that the data will be uploaded to
# --detect-duplicates is a flag that will check for duplicate data and not upload it if it already exists
# --verbose is a flag that will print out the progress of the upload

