from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#This will be the require field for adding the Movie 
class Movie(models.Model):
    #Title and description is to limit
    #  the length of the text input
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    #This will come as optional
    url = models.URLField(blank=True) #This will come as optional

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    #This means that user can create multiple reviews. 
    # Similarly, movie can have multiple reviews
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text
