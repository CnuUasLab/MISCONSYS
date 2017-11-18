# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Models go here


class Photo(models.Model):
    
    # photo path (not required, just something we will use)
    photo_path = models.CharField(max_length = 500, default="none")
    
    # photo id
    photo_id = models.PositiveIntegerField()
    
    
    # *** OBJECT TYPE ***
    # choices for object type
    STANDARD = 'stnd'
    OFF_AXIS = 'off-ax'
    EMERGENT = 'emer'
    
    OBJECT_TYPE_CHOICES = (
        (STANDARD, 'standard'),
        (OFF_AXIS, 'off-axis'),
        (EMERGENT, 'emergent'),
    )
    
    # type of object (standard, off-axis or emergent)
    object_type = models.CharField(
        max_length = 20,
        choices = OBJECT_TYPE_CHOICES,
        default="none",
    )
    
    
    
    # photo-latitude
    photo_latitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    # photo-longitude (4 decimals at most, 7 digits total at most)
    photo_longitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    # photo-altitude
    photo_altitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    
    
    # *** ORIENTATION ***
    # choises for orientation
    NORTH = 'N'
    NORTHEAST = 'NE'
    EAST = 'E'
    SOUTHEAST = 'SE'
    SOUTH = 'S'
    SOUTHWEST = 'SW'
    WEST = 'W'
    NORTHWEST = 'NW'
    
    ORIENTATION_CHOICES = (
        (NORTH, 'N'),
        (NORTHEAST, 'NE'),
        (EAST, 'E'),
        (SOUTHEAST, 'SE'),
        (SOUTH, 'S'),
        (SOUTHWEST, 'SW'),
        (WEST, 'W'),
        (NORTHWEST, 'NW'),
    )
       
    # orientation (N,W,S ect...)
    orientation = models.CharField(
        max_length = 4,
        choices = ORIENTATION_CHOICES,
        default="none",
    )
    
    
    
    # choises for shape
    CIRCLE = 'circle'
    SEMICIRCLE = 'semicircle'
    QUARTER_CIRCLE = 'quarter circle'
    TRIANGLE = 'triangle'
    SQUARE = 'square'
    RECTANGLE = 'rectangle'
    TRAPEZOID = 'trapezoid'
    PENTAGON = 'pentagon'
    HEXAGON = 'hexagon'
    HEPTAGON = 'heptagon'
    OCTAGON = 'octagon'
    STAR = 'star'
    CROSS = 'cross'
    
    SHAPE_CHOICES = (
        (CIRCLE, 'circle'),
        (SEMICIRCLE, 'semicircle'),
        (QUARTER_CIRCLE, 'quarter circle'),
        (TRIANGLE, 'triangle'),
        (SQUARE, 'square'),
        (RECTANGLE, 'rectangle'),
        (TRAPEZOID, 'trapezoid'),
        (PENTAGON, 'pentagon'),
        (HEXAGON, 'hexagon'),
        (HEPTAGON, 'heptagon'),
        (OCTAGON, 'octagon'),
        (STAR, 'star'),
        (CROSS, 'cross'),
    )
    
    # shape of the object
    shape = models.CharField(
        max_length = 20,
        choices = SHAPE_CHOICES,
        default="none",
    )
    
    
    
    
    # color of the object
    background_color = models.CharField(max_length = 20, default="none")
    
    # the letter on the shape
    alphanumeric = models.CharField(max_length = 4, default="none")
    
    # the color of the letter
    alphanumeric_color = models.CharField(max_length = 20, default="none")
    
    
    # toString prints file path
    def __str__(self):
        return self.photo_path
        
        

