from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    balance = models.FloatField()

    def __str__(self):
        return self.name
