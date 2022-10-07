from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
   first_name = models.CharField(max_length= 20,null=True)
   middle_name = models.CharField(max_length= 20, null=True)
   last_name = models.CharField(max_length= 20,null=True)
   gender = models.CharField(max_length= 10,null=True)
   age = models.PositiveSmallIntegerField()
   phone_number = models.CharField(max_length= 15,null=True)
   id_number = models.IntegerField()