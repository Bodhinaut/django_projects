from django.conf.urls import url
from learn_app import views

# TEMPLATE TAGGING
app_name = 'learn_app' # look under here to find matching url

urlpatterns = [
	url(r'^relative/', views.relative, name='relative'),
	url(r'^other/$', views.other, name='other'),
	]