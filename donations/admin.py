from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Institution)
admin.site.register(models.Donation)
admin.site.register(models.CustomUser)



