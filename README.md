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


This is the first time we’ve encountered thinking about site security measures!
This is a Cross-Site Request Forgery (CSRF) token, which secures the HTTP POST action that is initiated on the subsequent submission of a form. 

The Django framework requires the CSRF token to be present. 
If it is not there, your form may not work!
It works by using a “hidden input” which is a random code and checking that it matches the user’s local site page.

---

**Model Forms**

We’ve seen how we can use Django Forms to grab information from the user and then do something with it.
So far we’ve only printed out that information, but what if we wanted to save it to a model?

Luckily Django makes accepting form input and passing it to a model very simple!
Instead of inheriting from the forms.Forms class, we will use forms.ModelForm in our forms.py file.

This helper class allows us to create a form from a pre-existing model
We then add an inline class (something we haven’t seen before) called Meta
This Meta class provides information connecting the model to the form.

Example:
from django import forms
from myapp.models import MyModel
class MyNewForm(forms.ModelForm):
	# Form Fields go here
		class Meta:
			model = MyModel
        fields = # Let’s see the options!



The fields attribute will connect to model
from django import forms
from myapp.models import MyModel
class MyNewForm(forms.ModelForm):
	# Form Fields go here
		class Meta:
			model = MyModel
        fields = # Let’s see the options!

---

Create a ModelForm in forms.py
Connect the form in the template
Edit views.py to show the form
Figure out how to .save() the data
Verify the model is admin registered

---

Whenever we want to modify the data that Learning Log manages,
we’ll follow these three steps: modify models.py, call makemigrations on
learning_logs, and tell Django to migrate the project.

---------------

Defining the Entry Model
To record what we’ve been learning about chess and rock climbing, we need
to define a model for the kinds of entries users can make in their learning
logs. Each entry needs to be associated with a particular topic. This relationship
is called a many-to-one relationship, meaning many entries can be
associated with one topic

---------------

The Django Shell
Now that we’ve entered some data, we can examine that data programmatically
through an interactive terminal session. This interactive environment is
called the Django shell, and it’s a great environment for testing and troubleshooting
your project. Here’s an example of an interactive shell session:
(ll_env)learning_log$ python manage.py shell
u >>> from learning_logs.models import Topic
>>> Topic.objects.all()
[<Topic: Chess>, <Topic: Rock Climbing>]
The command python manage.py shell (run in an active virtual environment)
launches a Python interpreter that you can use to explore the data
stored in your project’s database. Here we import the model Topic from the
learning_logs.models module u. We then use the method Topic.objects.all()
to get all of the instances of the model Topic; the list that’s returned is called
a queryset.

-------------


To get data through a foreign key relationship, you use the lowercase
name of the related model followed by an underscore and the word set u.
For example, say you have the models Pizza and Topping, and Topping is
related to Pizza through a foreign key. If your object is called my_pizza,
representing a single pizza, you can get all of the pizza’s toppings using
the code my_pizza.topping_set.all().

================================

Making Pages: The Learning Log Home Page
Usually, making web pages with Django consists of three stages: defining
URLs, writing views, and writing templates. First, you must define patterns
for URLs. A URL pattern describes the way the URL is laid out and tells
Django what to look for when matching a browser request with a site URL
so it knows which page to return.
Each URL then maps to a particular view—the view function retrieves
and processes the data needed for that page. The view function often calls a
template, which builds a page that a browser can read. To see how this works,
let’s make the home page for Learning Log. We’ll define the URL for the
home page, write its view function, and create a simple template.
Because all we’re doing is making sure Learning Log works as it’s supposed
to, we’ll keep the page simple for now. A functioning web app is fun
to style when it’s complete; an app that looks good but doesn’t work well
is pointless. For now, the home page will display only a title and a brief
description.

---------------------

To make it clear which urls.py we’re working in, we add a docstring
at the beginning of the file u. We then import the url function, which is
needed when mapping URLs to views v. We also import the views module
w; the dot tells Python to import views from the same directory as the
current urls.py module. The variable urlpatterns in this module is a list of
individual pages that can be requested from the learning_logs app x.
The actual URL pattern is a call to the url() function, which takes
three arguments y. The first is a regular expression. Django will look for
a regular expression in urlpatterns that matches the requested URL string.
Therefore, a regular expression will define the pattern that Django can
look for.
Let’s look at the regular expression r'^$'. The r tells Python to interpret
the following string as a raw string, and the quotes tell Python where
the regular expression begins and ends. The caret (^) tells Python to
find the beginning of the string, and the dollar sign tells Python to look
for the end of the string. In its entirety, this expression tells Python to
look for a URL with nothing between the beginning and end of the URL.
Python ignores the base URL for the project (http://localhost:8000/), so an
empty regular expression matches the base URL. Any other URL will not
match this expression, and Django will return an error page if the URL
requested doesn’t match any existing URL patterns.
The second argument in url() at y specifies which view function
to call. When a requested URL matches the regular expression, Django
will call views.index (we’ll write this view function in the next section).
The third argument provides the name index for this URL pattern so we
can refer to it in other sections of the code. Whenever we want to provide
a link to the home page, we’ll use this name instead of writing out a URL.

------------------


