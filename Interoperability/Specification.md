# Interoperability

# Introduction

The Interoperability section is meant to be set up between different sections. The two main sections are the main class and the mission class.
We need to create others as well that are described in the specification. The Interoperability server's main purpose is
to control communication between the ground station and the competition server. There are several design specifications that
need to be taken care of.

# Use of Daemons

Python does have a multi-threading class. However, the multi-threader in python does not accomplish what it set out to accomplish
which is parallel processing of different tasks in the main computation of the program. There is simultaneous processing. However,
it isn't done in parallel. The reason why this is a problem is because the competition clearly states that there should be 
a minimum frequency that we post telemetry at. If we have a dedicated process, then this becomes simpler.

Daemons are how we can solve this issue. The main idea behind doing this is that we create a separate background process in
and of itself. By keeping track of the main process, we can control whether it's running or not, and make sure that it's not running on it's own.

# Design

This is the general design specification that is occuring in this program. There are a few things happening behind the scene that are not shown in the picture.

<<<<<<< HEAD
=======
![alt text](https://github.com/CnuUasLab/MISCONSYS/blob/david.patch.spec/Interoperability/img/interop.jpg "Suggested Interop")
>>>>>>> master

The image details connections between the main process, and other external programs. These main processes are serviced information
through an http server, were we serve nothing but a json object over an http server held on the central workstation. Since most
of this is happening over one system, a lot of the interoperability stuff will not need to be serviced outside the workstation
doing the processing.

Because of this there are a few tasks that are specfic to the system design.

Task | Description
--- | ---
<<<<<<< HEAD
main.py | program that has a specific function of starting up all processes and serving information that is recieved through these processes.
mission.py | program that interfaces with the competition server, and spawns a daemon that posts telemetry to the competition server

=======
main.py | Program that has a specific function of starting up all processes and serving information that is recieved through these processes.
mission.py | Program that interfaces with the competition server, and spawns a daemon that posts telemetry to the competition server
FELC.js | This is just a resemblence for the front end. All of the front end's information will be gained from the http server.
mav.py | This is a mavlink section of the code. It grabs information from the Plane, and it allows us to update telemetry.
config.json | This is a placeholder for all of the configuration stuff in the program.
Utils.py | Simple utility function that we can use to log information as we go along.

A lot of the code examples can be found in the POKEMON repository in the CnuUasLab to use as an example for this year's code.

# Interface

<b> main (Last Year's Code) </b>
```python
#!/bin/python
#=======================================================#
# Main class for handeling Interoperability operations. #
#                                                       #
#                Author: davidkroell                    #
#                  Version: 0.0.1                       #
#=======================================================#

from mav import Mavlink
from mission import Mission
from utils import Utils
from flask import Flask, render_template
from flask_socketio import SocketIO
from imgclient import IMGClient

import sys
import socket
import thread
import json
import sys
import time
        
util = Utils()

try:
	# Extract JSON data from configs.
	with open('./config.json') as data_file:
		constants = json.load(data_file)
	util.succLog("Successfully extracted config data")

except IOError:
	util.errLog("WARNING: Config file not found!")
	util.errLog("Aborting operation! Make sure config.json exists in the /src directory.")
	util.errLog("I'm angry so I'm going to dump everything into dumpFile.txt now! GoodBye!!!")
#	util.dump() - > Being developed.
	sys.exit(0)

# Start Telemetry module to load data into.
telemetry = {}

util.succLog("Setting up mavlink recieving protocol - Instantiating modules...")

#try:
#        imgr = IMGClient("localhost", "cnuuas", "N0Ax1s")
#        util.succLog("Connection to IMG Server - Successful")
#except socket.gaierror:
#        util.errLog("ERR: No Access to the IMGClient FTP Server")

# Instantiate a Mavlink module.
mavl = Mavlink(
		constants['mavl-incoming']['host'],
		constants['mavl-incoming']['port']
	      )

# Instantiate Mission module.
miss = Mission(
		constants['auvsi']['host'],
		constants['auvsi']['port'],
		constants['auvsi']['username'],
		constants['auvsi']['password']
		)

# Grab mission/server data from the competition server.
missPacket = miss.getMissionComponents()

packets_sent = 0
startTime = time.time()

# Starting front end components.
util.log("Initiating telemetry status console front end")

util.log("Ready to recieve Mavlink Packets...")

packets_sent = 0
def postTelem(telemetry):
        global packets_sent

        # post telemetry to the Competition server.
        miss.postTelemetry(
                telemetry['latitude'],
                telemetry['longitude'],
                telemetry['altitude'],
                telemetry['heading']
        )
        packets_sent += 1


while True:
	try:
        	udpPacket = mavl.getMavPacket()
        	lonLatPacket = " "
        	if(udpPacket != None):

                	if (udpPacket.get_type() == "GLOBAL_POSITION_INT"):
	                       	telemPacket = udpPacket

				# populate the longitude element of the telemetry module
				telemetry['longitude'] = float(telemPacket.lon)/10000000
				telemetry['latitude'] = float(telemPacket.lat)/10000000
				telemetry['heading'] = float(telemPacket.hdg)/1000
				telemetry['altitude'] = float(telemPacket.alt)/10000

#				print telemetry
                                print miss.getSystemTime()
                                
				if (miss.isLoggedIn()):
#					thread.start_new_thread(postTelem, (telemetry,))
					postTelem(telemetry)
#					print telemetry

		if missPacket != None:
			pass
#			print missPacket
		missPacket = miss.getMissionComponents()

		# Recalculate the number of seconds elapsed
		elapsed = time.time() - startTime

		# If one second has elapsed reset the clock and print the frequency.
		if elapsed >= 1:
			global packets_sent
			telemetry['frequency'] = packets_sent
#			print telemetry['frequency']

			startTime = time.time()
			packets_sent = 0

	except KeyboardInterrupt:
		break
        except sys.stderr:
                util.errLog("ERR: Exit main on sys call. Terminating Sys call.")
```

<b> mission </b>
```python

class Mission():
   def __init__(self, hst, prt, usr, pss): #  (DAEMON PROCESS SPAWNED)
   	pass

   #==================
   #
   # Populates the mission components we need after each
   # time they are retrieved from the main task.
   #
   # Serves the purpose of synchronizing with mavlink thread module.
   #
   #==================
   def populateMissionComponents(self):           # (DAEMON SPAWNED)
   	pass
   	

   #===================
   #
   # Returns whether we're logged
   # into the competition server or not.
   #
   #===================
   def isLoggedIn(self):
   	pass

   #====================
   #
   # Grabs obstacle data from
   # interop server.
   #
   #====================
   def getObstacles(self):
   	pass

       #=================================================
       # Post a target to the server that may
       #  or may not have image data with it.
       #
       #--------------params:--------------
       #     pId                   -  Optional. The ID of the target.
       #     pUser                 -  Optional. The ID of the user who created the target.
       #     pType                 -  Target type, must be one of TargetType.
       #     pLat                  -  Optional. Target latitude in decimal degrees.
       #     pLon                  -  Optional. Target longitude in decimal degrees.
       #     pOrient               -  Optional. Target orientation.
       #     pShape                -  Optional. Target shape.
       #     pBgColor              -  Optional. Target color.
       #     pAlphanumeric         -  Optional. Target alphanumeric. [0-9, a-z, A-Z].
       #     pAlphanumericColor    -  Optional. Target alphanumeric color.
       #     pDescription          -  Optional. Free-form description of the target.
       #     pAutonomous           -  Defaults to False. Indicates that this is an ADLC target.
       #     pTeamId               -  Optional. The username of the team to submit targets.
       #     pActionableOverride   -  Optional. Manually sets the target to be actionable.
       #     pImagePath            -  Optional. Image path to be specified if involved in post.
       #=================================================
       def postTarget(self, pId, pUser, pType, pLat, pLon, pOrient, pShape,
                      pass 
       
   #========================
   # Post telemetry to the server.
   #
   #-------params:----------
   #	  lat - latitude value of plane.
   #	  lon - longitude value of plane.
   #	  alt - altitutde of the plane.
   #	  hdg - uas heading fo plane.
   #========================
   def postTelemetry(self, lat=38.145245, lon=-76.427946, alt=50, hdg=90):
               pass

   #=====================
   # Get the system time.
   #---------------------
   #=====================
   def getSystemTime(self):
   	pass

   #=============================
   # 	   Post a detected target on
   #	the field through the SIRE module.
   #
   #-------params:---------------
   #	  typ - The type of target
   #	  lat - latitude location of the target
   #	  lon - longitude location of the target
   #	  ori - Orientation of the target
   #	  shp - Shape of the target
   #	  bgc - background color of the taget
   #	  letter - Letter printed on the front of the target
   #	  color - color of the target text.
   #	  image_path - path of the image where target is found.
   #============================
   def postTarget(self, typ='standard', lat=38.145215, lon=-76.427942, ori='n', shp='square',
   	pass

   #==========================
   #
   # Retrieve the mission data for the competition.
   #
   #==========================
   def getMissionData(self):
   	pass
```

<b> mav </b>
```python
class Mavlink():
    def __init__(self, ip, port):
        pass

    # Function called in the thread to constantly update packets. (DAEMON PROCESS SPAWNED)
    def startUDPStream(self):
        pass

    # Accessor, to get the current packet
    def getMavPacket(self):
        pass

    # Posts data to the airplane.
    def postData(self, packet):
        pass
```
>>>>>>> master
