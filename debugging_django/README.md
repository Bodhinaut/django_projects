### Example issues and solution to a growing Django application. 

Let's say a view starts to malfunction due to the URLs growing over time. 
A GET that should execute a view with a certain function x may start executing Y instead. If the URL routing is messing up you could try
use **django.core.urlresolvers.resolve** method and try that from shell. We can then confirm it is wrongly being resolved. 

In general a good idea for prevention of this issues is to keep things modular. Keep
your index.html files, templates, within subtemplates in specified folders. Keep those views and url patterns in the proper application
folder. Also, have the urls.py have many **includes()** with their own unique prefixes. 

Keep the urls.py clean in your project folder, use include and specify those urls to seperate applications and template folders. 
Use include() to link them all together 

Following is an example and solution at debugging.

---

https://github.com/django-extensions/django-extensions

utilize manage.py show_urls

install django_extensions - third party app, provides management commands, started with providing management commands that aren't in core

This will help give us in what order the url resolution has been attempted. 

install django extensions in settings.py file 

manage.py dumpscript, to output in python a script that will allow you to repopulate your database as python objects, still need django
but good way to keep your info in portable format that supports django backend 

next is to use manag.py export_emails, export your users emails to be able to use that data, 

manage.py graph_models , outputs dot file with grahic visuals, shows beautiful and pretty database with connections, representation of 
your database, 

**manage.py grah_modes auth blog | dot -Tpng -o test.png**


manag.py runscript update.py - gives all context and models around your django app for updates

manage.py shell_plus - launch and load models into django shell 

