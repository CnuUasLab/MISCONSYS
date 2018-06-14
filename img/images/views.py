## -*- coding: utf-8 -*-

#===========================================#
# View program for the images application   #
# Allows for an HttpRequest to be answered. #
#                                           #
#          Author:   davidkroell            #
#          Version:  2.0.3                  #
#                                           #
#===========================================#

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Image
from .models import Target
from .serializers import ImageSerializer

def index(request):
    return HttpResponse("Hello, world. you're at the images index.")


#=====================================
# View Set for an independant image.
# -----------------------------------
#  Allows us to configure functions at
#   specific ednpoints.
#=====================================
class ImageViewSet(ModelViewSet):

    # Required Attributes.
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    
    #=====================================
    #  Handle Post request for the Image.
    #=====================================
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #======================================
    # Handle Get request for the Images collectively.
    #======================================
    def get(self, request, format=None):
        return Reponse(Image.objects.all(), status=status.HTTP_200_OK)
