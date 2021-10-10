from django.db import models
from django.db.models import manager

# Create your models here.

class BookDetails(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(null= True)
    price = models.IntegerField(null=True)
    file = models.FileField(default=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name