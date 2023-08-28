from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    EmpID = models.CharField(max_length=50)
    EmpPost = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to="upload")
    Age = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Address = models.TextField(max_length=225)
    
