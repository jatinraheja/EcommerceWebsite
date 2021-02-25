from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Login(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

