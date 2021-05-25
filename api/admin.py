from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Test)
admin.site.register(models.CompanyInfo)
admin.site.register(models.CompanyTest)


