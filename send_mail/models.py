from django.db import models

# Create your models here.


class Contact(models.Model):
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    message= models.TextField(max_length=2000)

    def __str__(self):
        return self.name

