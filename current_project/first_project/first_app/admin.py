from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage
# Register your models here.

# tell app here that our models exists

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# registerd and ready to use with admin interface now, but need to 
# create superuse to be allowed to do so now, 