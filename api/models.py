from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

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

class Test(models.Model):
    test_name = models.CharField(max_length=50)

    def __str__(self):
        return self.test_name

class CompanyInfo(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50, default='Anonymous')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name

class CompanyTest(models.Model):
    test = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.test

# class CompanyLocation(models.Model):
#     company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
#     area = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     state = models.CharField(max_length=50, blank=True, null=True)
#     pincode = models.CharField(max_length=20, blank=True, null=True)
    
#     def __str__(self):
#         return self.company.company_name