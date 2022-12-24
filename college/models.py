from django.db import models

# Create your models here.
class UserForm(models.Model):
    name=models.CharField(max_length=10)
    rollno=models.IntegerField()
    branch=models.CharField(max_length=10)
    phno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)