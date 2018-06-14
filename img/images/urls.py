
#=====================================#
#   Url routing for the application   #
#  Allows for routing of the app to   #
#  function properly                  #
#                                     #
#         Author: davidkroell         #
#        Version: 03/01/2018          #
#                                     #
#=====================================#

# -- Import dependencies
from django.conf.urls import url, include
from . import views

# -- Get Rest component dependencies --
from rest_framework import renderers, routers

router = routers.DefaultRouter()
router.register('images', views.ImageViewSet,  'images')
# Wire up our API using automatic URL Routing.
# -- Different routes that are possible to access.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls))
    # Begin the url api we need.
   # url(r'^api/images/$', views.images, name='images'),
   # url(r'^api/targets/$', views.targets, name='targets'),
]





