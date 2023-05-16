from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    owner= models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount=models.FloatField()
    date= models.DateField(default=now)
    description = models.TextField()
    catagory = models.CharField(max_length=256)


    def __str__(self):
        return self.catagory
    
