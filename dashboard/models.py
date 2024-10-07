from django.db import models



# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('user', 'USER'),
    ]
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices= ROLE_CHOICES, null=True)