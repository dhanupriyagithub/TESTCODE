from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
       return self.name   #return the string type

    
    class Meta:
        db_table= 'city'

class Authentication(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
       return self.name   #return the string type

    
    class Meta:
        db_table= 'authentication'

    