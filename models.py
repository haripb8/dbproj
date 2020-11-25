from django.db import models
class sdb(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)

# Create your models here.
