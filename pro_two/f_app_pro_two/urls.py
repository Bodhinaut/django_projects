from django.conf.urls import url
from f_app_pro_two import views

urlpatterns = [
	url(r'^$', views.help, name='help'),
]