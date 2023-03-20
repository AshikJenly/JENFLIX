from django.db import models



# Create your models here.

    
class UserInfoDB1(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    key_enc=models.CharField(max_length=150)
    