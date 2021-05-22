from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    session_token = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
