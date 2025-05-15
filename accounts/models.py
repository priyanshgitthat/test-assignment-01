from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    profile = models.ImageField(upload_to='photos',null=False,blank=False)
    addressLine1 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField(null=True,blank=True)
    USER_TYPE_CHOICES =(
        ('patient','Patient'),
        ('doctor','Doctor'),
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='patient'
    )
 
    def __str__(self):
        return f"{self.username} - {self.user_type.capitalize()}"