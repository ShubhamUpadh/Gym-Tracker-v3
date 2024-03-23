from django.db import models

# Create your models here.

class users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 20)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(unique=True)
    
