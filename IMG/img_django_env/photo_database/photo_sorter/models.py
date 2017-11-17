# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# For now, a photo will have an id, path, longitude, latitude, and altitude
# Add more attributes later



class Photo(models.Model):
    
    # photo id
    photo_id = models.PositiveIntegerField()
    
    # photo path
    photo_path = models.CharField(max_length = 500)
    
    # photo-longitude
    photo_longitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    # photo-latitude
    photo_latitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    # photo-altitude
    photo_altitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    # toString prints file path
    def __str__(self):
        return self.photo_path



