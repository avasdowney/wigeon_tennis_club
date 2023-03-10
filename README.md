# CS460W Semester Project
Cam, Anthony, Ava

## Configuring GitHub Credentials
1. Follow these [steps](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to get your PAT to be able to use as a password and save it somewhere safe
1. To store in terminal so you dont have to manually enter every time follow [this tutorial](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)

## Getting started with coding
1. Get the repo locally using ```git clone https://github.com/avasdowney/wigeon_tennis_club.git```
1. Switch to your branch using ```git checkout -b {your name}```. We can merge changes from our individual branches via pull requests.

## How to make changes
1. In Git Bash navigate to working directory using ```cd {folder to enter}``` to change directory and ```ls``` to see the directory you are in
1. Make sure you pull code before you start working so we do not overwrite changes using ```git pull https://github.com/avasdowney/wigeon_tennis_club.git```
1. Make the changes you want to make
1. Pull code from the repo again using ```git pull https://github.com/avasdowney/wigeon_tennis_club.git```
1. Add your changes using ```git add .``` to add all modifications to local changelog
1. Write a commit message brefily describing your changes using ```git commit -m "{message}"```
1. Push your changes up into the GitHub repository using ```git push```. If you refresh the GitHub page your changes should be visible in your branch now.

## Development Things
1. Run server using ```python3 manage.py runserver``` in base directory redirects to http://localhost:8000/polls/
1. Test server using ```python3 manage.py test polls``` in base directory
1. If running from new clone of the repo run ```python3 manage.py migrate``` to instantiate database

### admin
1. Admin page: http://localhost:8000/admin/
1. Create admin profile: ```python3 manage.py createsuperuser```

