# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Photo

# Register your models here.
# This allows you to edit the photo_sorter app on the admin page
admin.site.register(Photo)

