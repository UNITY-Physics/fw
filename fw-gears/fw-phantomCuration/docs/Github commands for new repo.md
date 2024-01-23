Github commands for new repo

If copied from existing repo, check there isn't already a .git folder

In a clean local repo initate as 'main'
> git init -b main

Add contents of current folder to staging
> git add .   

Add a comment
> git commit -m "First commit"

Link the remote repository location to the current repo
> git remote add origin https://github.com/Nialljb/fw-phantom-curation.git

Check
> git remote -v

Push staged repo
> git push -u origin main