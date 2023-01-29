from django.contrib import admin

# Register your models here.
from .models import Movie, Review


admin.site.register(Movie)
admin.site.register(Review)

#admin.site.register(Sample)