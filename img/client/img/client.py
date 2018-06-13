#=========================================================#
#                                                         #
#               Core IMG Client Module                    #
#                                                         #
#    This module provides a Python interface to           #
#  the IMG API. Usage of this client api is required      #
#  to access the information enclosed in the IMG server   #
#                                                         #
#                  Author: davidkroell                    #
#                 Version: 2.0.3                          #
#                                                         #
#=========================================================#

from concurrent.futures import ThreadPoolExecutor
import functools
import json
import requests
import threading


#=======================================
#
#  Client which provides access to the IMG Api
# This client uses sessions to make requests to
# IMG server.
#
#=======================================
class Client(object):

    def __init__(self, url, username, password, timeout=10, max_retries=10):

        self.url = url
        self.timeout = timeout

        self.session = requests.Session()
        self.session.mount('http://', requests.adapters.HTTPAdapter(max_retries=max_retries))
	self.post('/admin/login', data={'username':username, 'password':password})


    #================================
    #  Get request to server
    #================================
    def get(self, uri, **kwargs):

        r = self.session.get(self.url + uri, timeout=self.timeout, **kwargs)
        if not r.ok:
            raise Exception('Had trouble doing a Get request to the server.')
        return r

    #===============================
    # Post request to the server
    #===============================
    def post(self, uri, **kwargs):

        r = self.session.post(self.url + uri, timeout=self.timeout, **kwargs)
        if not r.ok:
            raise Exception('Had trouble doing a POST request to the server.')
        
        return r

    #===============================
    # Put request to the server
    #===============================
    def put(self, uri, **kwargs):
         
        r = self.session.put(self.url + uri, timeout=self.timeout, **kwargs)
        if not r.ok:
            raise InteropError(r)
        return r

    #================================
    # Delete request to the server
    #================================
    def delete(self, uri):
        
        r = self.session.delete(self.url + uri, timeout=self.timeout)
        if not r.ok:
            raise InteropError(r)
        return r
