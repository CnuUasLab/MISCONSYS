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
	sys.exit(0)

# Start Telemetry module to load data into.
telemetry = {}

util.succLog("Setting up mavlink recieving protocol - Instantiating modules...")

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
                
                # populate the coordinate elements of the telemetry module
                telemetry['longitude'] = float(telemPacket.lon)/10000000
                telemetry['latitude'] = float(telemPacket.lat)/10000000
                telemetry['heading'] = float(telemPacket.hdg)/1000
                telemetry['altitude'] = float(telemPacket.alt)/10000

                # print telemetry
                print miss.getSystemTime()

                if (miss.isLoggedIn()):
                    # thread.start_new_thread(postTelem, (telemetry,))
                    postTelem(telemetry)

            # print telemetry
            if missPacket != None:
                print missPacket

            missPacket = miss.getMissionComponents()
            # Recalculate the number of seconds elapsed
            
            elapsed = time.time() - startTime
            # If one second has elapsed reset the clock and print the frequency.
            if elapsed >= 1:
                global packets_sent
                telemetry['frequency'] = packets_sent

                # print telemetry['frequency']
                startTime = time.time()
                packets_sent = 0

    except KeyboardInterrupt:
        break
    except sys.stderr:
        util.errLog("ERR: Exit main on sys call. Terminating Sys call.")
