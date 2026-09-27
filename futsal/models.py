from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE = [
        ('user', 'USER'),
        ('admin', 'ADMIN')
        ]
    
    user_phone = models.CharField(max_length=10, blank=True)
    user_role = models.CharField(max_length=10, choices=ROLE, default='user')

class Futsal(models.Model):
    f_name = models.CharField(max_length=50)
    f_image = models.ImageField(upload_to='images/')
    f_description = models.CharField(max_length=100)
    f_supports_5a = models.BooleanField(default=False)
    f_supports_7a = models.BooleanField(default=False)
    f_price_5a = models.DecimalField(max_digits=10,decimal_places=2)
    f_price_7a = models.DecimalField(max_digits=10,decimal_places=2)
    f_location = models.CharField(max_length=50)
    f_is_active = models.BooleanField(default=True)

class Booking(models.model)
    