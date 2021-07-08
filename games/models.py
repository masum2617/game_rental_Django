from django.db import models
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    game_title = models.CharField(max_length=100)
    game_availbility = models.BooleanField(default=True)
    game_description = models.TextField(blank=True)
    game_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.game_title