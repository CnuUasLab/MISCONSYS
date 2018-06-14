#=======================================#
#   Serialization model for different   #
#     REST components of the server     #
#                                       #
#         Author: davidkroell           #
#        Version: 1.0.5                 #
#                                       #
#=======================================#


from rest_framework import serializers

from .models import Image
from .models import Target

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'img_photo', 'img_path', 'lon', 'lat')


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('id', 'image', 'shape_choices', 'shape_color', 'alphanumeric',  'alphanumeric_color', 'direction')
