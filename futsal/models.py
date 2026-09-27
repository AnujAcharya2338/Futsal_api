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
    f_description = models.TextField(max_length=100)
    f_supports_5a = models.BooleanField(default=False)
    f_supports_7a = models.BooleanField(default=False)
    f_price_5a = models.DecimalField(max_digits=10,decimal_places=2)
    f_price_7a = models.DecimalField(max_digits=10,decimal_places=2)
    f_location = models.CharField(max_length=50)
    f_is_active = models.BooleanField(default=True)
    f_opening_time = models.TimeField()
    f_closing_time = models.TimeField()

class Booking(models.Model):
    STATUS = [
        ('pending','PENDING'),
        ('confirmed', 'CONFIRMED'),
        ('cancelled', 'CANCELLED'),
        ('completed', 'COMPLETED'),
    ]
    GAME_TYPE = [
        ('5A','5A'),
        ('7A','7A')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    futsal = models.ForeignKey(Futsal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    game_type = models.CharField(max_length=2, choices=GAME_TYPE)

    
    
    