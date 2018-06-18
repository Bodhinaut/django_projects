Writing your first Django app, part 1
---

https://docs.djangoproject.com/en/2.0/intro/tutorial01/

---

Let’s learn by example.

Throughout this tutorial, we’ll walk you through the creation of a basic poll application.

It’ll consist of two parts:

A public site that lets people view polls and vote in them.
An admin site that lets you add, change, and delete polls.
We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):

$ python -m django --version
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

This tutorial is written for Django 2.0, which supports Python 3.4 and later. If the Django version doesn’t match, you can refer to the tutorial for your version of Django by using the version switcher at the bottom right corner of this page, or update Django to the newest version. If you’re using an older version of Python, check What Python version can I use with Django? to find a compatible version of Django.

See How to install Django for advice on how to remove older versions of Django and install a newer one.
