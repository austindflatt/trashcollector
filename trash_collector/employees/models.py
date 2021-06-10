from django.db import models
# from ..customers.models import Customer
# Create your models here.


# TODO: Create an Employee model with properties required by the user stories
class Employees(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

