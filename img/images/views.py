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


def index(request):
    return HttpResponse("Hello, world. you're at the images index.")


