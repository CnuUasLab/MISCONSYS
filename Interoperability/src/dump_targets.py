#===============================================#
#   Python script to be run after the           #
#  plane has landed to round up all Target      #
#  Data from the image server and push it to    #
#  the competition server.                      #
#                                               #
#            Author: davidkroell                #
#                                               #
#===============================================#

import sys
import requests
import thread
import re
import time
import json

from utils import Utils
from mission import Mission

sys.path.insert(0, "../../img/client")
from client import IMGClient

util = Utils()

try:
	# Extract JSON data from configs.
	with open('./config.json') as data_file:
		constants = json.load(data_file)
	util.succLog("Successfully extracted config data")

except IOError:
	util.errLog("WARNING: Config file not found!")
	util.errLog("Aborting operation! Make sure config.json exists in the /src directory.")
	sys.exit(0)


img_cli = IMGClient('0.0.0.0', '5001')

# Instantiate Mission module.
miss = Mission(
		constants['auvsi']['host'],
		constants['auvsi']['port'],
		constants['auvsi']['username'],
		constants['auvsi']['password']
		)

target_list = img_cli.getTargets()

for tgt in target_list:
    img_id = tgt['image']
    print img_id
    img_obj = img_cli.getImage(img_id)

    path = img_obj['img_photo']

    miss.postImage( lat=img_obj['lat'],
                    lon=img_obj['lon'],

                    ori=tgt['direction'],
                    shp=tgt['shape_choices'],
                    bgc=tgt['shape_color'],
                    letter=tgt['alphanumeric'],
                    color=tgt['alphanumeric_color'],

                    image_path=path
    )
