from django.db import models
from datetime import date, datetime

# Create your models here.
class Listing(models.Model):
    game_title = models.CharField(max_length=100)
    game_availbility = models.BooleanField(default=True)
    game_description = models.TextField(blank=True)
    game_date = models.DateTimeField(default=datetime.now, blank=True)
    release_date = models.DateField(default='test')
    genre = models.CharField(max_length=50,default='test')
    publisher = models.CharField(max_length=50,default='test')
    rating = models.CharField(max_length=50,default='test')
    hdd = models.CharField(max_length=50,default='test', blank=True)
    compatibility = models.CharField(max_length=50,default='test')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',default='default.jpg')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.game_title