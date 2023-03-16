from django.db import models

# Create your models here.
class movie1(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    des  = models.TextField()
    image = models.ImageField(upload_to='img')