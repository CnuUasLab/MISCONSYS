## -*- coding: utf-8 -*-

#===========================================#
# View program for the images application   #
# Allows for an HttpRequest to be answered. #
#                                           #
#          Author:   David Kroell           #
#          Version:  03/01/2018             #
#                                           #
#===========================================#

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from .models import Image
from .models import Target


def index(request):
    return HttpResponse("Hello, world. you're at the images index.")

def images(request):
    return HttpResponse("Returning all images")

def targets(request):
    return HttpResponse("Getting all targets")

