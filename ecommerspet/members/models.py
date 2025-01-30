from django.db import models
from ecommerspet import *
import psycopg2

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # joined_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(max_length= 10)
    phone = models.CharField(max_length=20)
    regesteed_on = models.DateTimeField(auto_now_add=True)
    paymentmode = models.TextField(max_length=100)

    def __str__(self):
        return self.name
