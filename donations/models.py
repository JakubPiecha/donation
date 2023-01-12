from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)


class Institution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.IntegerField(choices={
        (1, 'fundacja'),
        (2, 'organizacja pozarządowa'),
        (3, 'zbiórka lokalna')}, default=1)
    categories = models.ManyToManyField('Category')


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(get_user_model(), null=True, default=None, on_delete=models.SET_DEFAULT)
