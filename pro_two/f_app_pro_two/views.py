from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("<em>My second Project</em")

def help(request):
	help_dic = {'first_temp_tag': 'HELP'}
	return render(request, 'f_app_pro_two/help.html', context=help_dic)
