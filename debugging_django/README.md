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

utilize manage.py show_urls

install django_extensions

This will help give us in what order the url resolution has been attempted. 

