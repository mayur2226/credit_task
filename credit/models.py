from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=50, default="")
    current_credit = models.IntegerField(default=0)
    phone_no = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.email

class Transfer(models.Model):
    sender = models.CharField(max_length=20,default="")
    reciever = models.CharField(max_length=20,default="")
    amount = models.IntegerField()
    def __str__(self):
        return self.sender        
