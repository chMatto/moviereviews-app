from django.db import models

# Create your models here.
class News(models.Model):#Model is Mother class
    #This set the requirement for the News database
    headline = models.CharField(max_length= 200) 
    body = models.TextField()
    date = models.DateField()

    #This display the heading of news in the Admin page
    def __str__(self):
        return(self.headline," posted on ", self.date)