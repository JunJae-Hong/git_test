from django.db import models

# Create your models here.
#class Lol(models.Model):
    #name = models.CharField(max_length=100)
    #gender = models.CharField(max_length=50)
    #hp = models.IntegerField()
    #text = models.TextField()

class Lol(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField()
