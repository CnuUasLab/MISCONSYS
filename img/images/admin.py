#==================================================#
#       Admin control for the django app           #
#    Allows for admin controls in the context of   #
#    the images being modified.                    #
#                                                  #
#               Author: David Kroell               #
#              Version: 0.0.1                      #
#                                                  #
#==================================================#

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image, Target

admin.site.register(Image)
admin.site.register(Target)