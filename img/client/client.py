#=============================================#
#  IMG Client API for recieveing and posting  #
#   Images as well as uploading Target info.  #
#                                             #
#               Author: davidkroell           #
#              Version: 2.0.4                 #
#                                             #
#=============================================#

import functools
import json
import requests
import threading

class IMGClient():
    def __init__(self, url, port):
        self.IMAGES = '/api/images/'
        self.TARGETS = '/api/targets/'

        self.url = url
        self.port = port
        
        self.session = requests.Session()
        self.session.mount('http://', requests.adapters.HTTPAdapter(max_retries=10))


    def getImages(self):
        access = 'http://'+self.url+':'+self.port+self.IMAGES  
        result = self.session.get(access, timeout=10)
        return result.json()

    
    def getImage(self, img_id):
        access = 'http://'+self.url+':'+self.port+self.IMAGES+'/'+img_id
        result = self.session.get(access, timeout=10)
        return(result.json())

    
    def postImage(self, pImgPhoto, pImgPath, pLon, pLat):
        values = {
            'img_path' : pImgPath,
            'lon' : pLon,
            'lat' : pLat
        }

        mFiles = { 'img_photo':pImgPhoto }
        
        access = 'http://'+self.url+':'+self.port+self.IMAGES
        result = self.session.post(access, timeout=10, data=values, files=mFiles)

        if result.ok:
            return result
        else:
            raise Exception(result)


    def getTargets(self):
        access = 'http://'+self.url+':'+self.port+self.TARGETS
        result = self.session.get(access, timeout=10)

        return result.json()

    def getTarget(self, target_id):
        access = 'http://'+self.url+':'+self.port+self.TARGETS+'/'+target_id
        result = self.session.get(access, timeout=10)
        return(result.json())

    def postTarget(self, img_id, shape, shape_color, alphanumeric, alphanumeric_color):
         access = 'http://'+self.url+':'+self.port+self.TARGETS
         values = {
             'image': img_id,
             'shape_choices':shape,
             'shape_color':shape_color,
             'alphanumeric':alphanumeric,
             'alphanumeric_color':alphanumeric_color
         }

         result = self.session.post(access, timeout=10, data=values)
