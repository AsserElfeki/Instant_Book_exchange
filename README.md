# How To Use
### Git
Clone the repository (to clone you have to use githubtoken or ssh connection), if you want to do any work on your local version always do:
```sh
git pull
```
before editing. After you finish your job:
```sh
git add . #for adding any files you created
git commit -a -m "commit message" #to commit your changes, -a stands for all, you can commit specific files if you want.
```
And last but not least:
```sh
git push
```
### Python
In terminal move to your cloned directory then:
```sh
sudo pipenv install
```
It will install all needed pip packeges (they are in Pipfile).
Next:
```sh
sudo pipenv shell
```
This will put you into virtual environment shell from where you can run commands like:
```sh
python manage.py runserver #starts the server
python manage.py makemigrations #makes migrations, run it after changes to your models.py files
python manage.py migrate #run it after makemigrations
```
That's it folks.
