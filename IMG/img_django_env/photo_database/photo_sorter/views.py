# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here
from django.http import HttpResponse

# detail page to display coordinates
# def detail(request, photo_id):
#    return HttpResponse("You're looking at image %s." % photo_id)




def index(request):
    return HttpResponse("Hello, world. You're at the photo sorter index!!")
