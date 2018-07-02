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

---

* Setting up projects and applicatins involves creating views and mapping URLs
* simple template tags
* serve static media files 

---

* With models and databases we accept infor from the user, input it into a database, 
we retrieve that information from a database and use it to generate content for the user

* SQLite can come in handy here with Django and Python in general, we use models to incorporate a databse into a django project and can switch backends easily

* Settings.py we can edit the engine parameter used for databses 

* Create move, use class structre inside of applitcations in models.py

---

we will inherent from subclass of djangos built in models class

* Then each attribute of class represents a field which is just like a column name with contrains in SQL 

* SQL operates like a giant table, with each column representing a field , and each row representing an entry data point 

* Eeach column has a type of field, such as charField, IntergerField etc..

* Each filed will then have a contraint like max_char or max_length

---

Then there is the table model relationship, 

often models will reference each other 

* for this referencing to work we use **foreign keys and primary keys**

* the unique ID in one table is the foreign key in another, later we iwll focus on one-to-one and many-to-many relationships 

---

_INSERT MODEL EXAMPLES HERE LATER_

---

After everythins is set up we migrate the databases, sjango does the heavy lifting of creating SQL tables taht corresponds to the models we created, 

python manage.py migrate

---

then register changes to your app, 

python manage.py makemigrations _yourapp_

we can then later on use the shell from the manage.py file to play around with the models, 
Djangos admin has so many useful features 

---

We just:
Set up projects and applications
Created views and mapped URLs
Used simple Templates and tags
Served static media files 

For our web app, start with django 2 part one, 

---

Now we will: 
Models Databases and Admin
Models Overview 
Important, accept info from user, input into database, retreive info from database, generate content 
for the user, 

---

* An essential part of any website is the ability to accept information from a user and input it into a database and retrieve information from a database and use it to generate content for the user.

* An essential part of any website is the ability to accept information from a user and input it into a database and retrieve information from a database and use it to generate content for the user.

* In the settings.py file you can edit the ENGINE parameter used for DATABASES
To create an actual model, we use a class structure inside of the relevant applications models.py file

* In the settings.py file you can edit the ENGINE parameter used for DATABASES
To create an actual model, we use a class structure inside of the relevant applications models.py file

* SQL operates like a giant table, with each column representing a field, and each row representing an entry.


* Each column has a type of field, such as a CharField, IntegerField, DateField, etc.
Each field can also have constraints


* For example, a CharField should have a max_length constraint, indicating the maximum number of characters allowed

* The last thing to note is table (or models) relationships.
Often models will reference each other

* For this referencing to work we use the concepts of Foreign Keys and Primary Keys.

* A primary key is a unique identifier for each row in a table

* A foreign key just denotes that the column coincides with a primary key of another table


class Topic(models.Model):
	top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
	category = models.ForeignKey(Topic)
name = models.CharField(max_length=264)
	url = models.URLField()

class Webpage(models.Model):
	topic = models.ForeignKey(Topic)
name = models.CharField(max_length=264)
	url = models.URLField()

	def __str__(self):
		return self.name
    
    
* After we’ve set up the models we can migrate the database
This basically let’s Django do the heavy lifting of creating SQL databases that correspond to the models we created

* Django can do this entire process with a simple command:
python manage.py migrate 
Then register the changes to your app, shown here with some generic “app1”:
python manage.py makemigrations app1 
 

* Then migrate the database one more time:
python manage.py migrate 
We can then later on use the shell from the manage.py file to play around with the models

 
---


how to use Django Forms to accept User Input and connect it to the database and retrieve it later on.

Django Forms Advantages:
Quickly generate HTML form widgets
Validate data and process it into a Python data structure
Create form versions of our Models, quickly update models from Forms

The first thing we need to do is create a forms.py file inside the application! 
After that we call Django’s built in forms classes (looks very similar to creating models).

Example inside of forms.py:
from django import forms
class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)


Inside our views.py file we need to import the forms (two ways to do this)
from . import forms
from forms import FormName


 
We can then create a new view for the form
def form_name_view(request):
	form = forms.FormName()
	return render(request,’form_name.html’,
							{‘form’:form})


Then we just add the view to the app’s urls, either directly or with include(). Directly:
from basicapp import views
urlpatterns = [
url(r’formpage/’,views.form_name_view,
    name = ‘form_name’),
]


We can then create the templates folder along with the html file that will hold the template tagging for the form.
Remember to update the settings.py file to reflect the TEMPLATE_DIR variable!
Also remember that your views should reflect subdirectories inside templates!

So now everything is setup for us to go into the form_name.html file inside templates/basicapp and add in the actual template tagging that will create the Django Form!


There are several ways you can “inject” the form using template tagging. You can just pass in the key from the context dictionary:
{{ form }}





