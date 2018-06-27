# django_projects
python and django projects

---

Currently working on learning Anaconda, using virtual environments within to run Python and Django projects. 

---


### Django
A free and open source web framework. 
* It allows us to map a requested URL from a user to the code that is actually meant to handle it. It also allows us to create that requested HTML dynamically. 

* Templates allow us to inject calculated values and information from the _database_ into an HTML page to then show to the user. 

---

**Virtual Environments** are important. I use **Anaconda** because it allows us to create a virtual environment very easily. Python packages change and update often and these changes can crash websites and break backwards compatiability. We will test out new features and not break our web app by creating a virtual environment that contains the packages we wish to test out. This also allows us all to be on the same page with the same installed versions of software and in the same environment.

---

Anaconda makes this easy! It has a virtual environment handler. 

**conda create --name myEnv django**

You just created a virtual environment (venv) with the latest version of Django. 

**activate myEnv**
or
**source activate myEnv**
this is for BASH users, and GITBASH users

remember, anything we initialize our environment with will have those installions, so pip _library_ or whatever django installation
_example_

**conda create --name myDjangoEnv python=3.6**

you can deactive with 
**deactivate myEnv**
**source deactivate myEnv**

do 

**conda info --envs**
to see all of your venv

once you are in your venv, don't forget to 
**conda install django**

---

* django-admin

create first project with django by,

**django-admin startproject first_project**

this also creates the django project folder,
__init__.py: blank py script, lets Python know this is a directory to be treated as a package
settings.py: store project settings, add apps, templates, detail file path with python os module...
urls.py: url patterns ofr project, the different pages of the web app
wsgi.py: wbeserver gateway interface, helps us to deploy
manage.py: holds runserver and other important static commands for our web app
ex... **python manage.py runserver**
