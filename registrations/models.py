from django.db import models

class Customer(models.Model):
    fname_text = models.CharField(max_length=200)
    lname_text = models.CharField(max_length=200)





# Create your models here.
