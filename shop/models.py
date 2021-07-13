from django.db import models

# Create your models here.
class Shop(models.Model):
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  category = models.CharField(max_length=30)
  price = models.CharField(max_length=50)
  region = models.CharField(max_length=50)
  is_available = models.BooleanField(default=True)
  
  def __str__(self):
    return self.title