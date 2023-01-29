from django.contrib import admin

# Register your models here.
from .models import News

#This will add this class to the Admin platform
admin.site.register(News)