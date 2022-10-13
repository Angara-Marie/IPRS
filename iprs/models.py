from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.
class Customer(models.Model):
   first_name = models.CharField(max_length= 20,null=True)
   middle_name = models.CharField(max_length= 20, null=True)
   last_name = models.CharField(max_length= 20,null=True)
   GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
   gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
   age = models.PositiveSmallIntegerField()
   id_number = models.IntegerField()