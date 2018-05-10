#============================================#
#                 Mission Handler            #
#	            Author: davidkroell          #
#                                            #
#               version: 2017-12-28          #
#                                            #
#============================================#

import sys
import requests
import thread
import re

from utils import Utils, Queue
from multiprocessing import Process

sys.path.insert(0, "../interop/client/")
import interop

#==================================
#
# Missions module for each mission.
#
#------params:---------------------
#	hst - hostname/ipaddr
#	prt - port that the competition sever runs on.
#	usr - Username for the server
#	pss - Password for the server
#
#==================================
class Mission():
    def __init__(self, hst, prt, usr, pss):
        self.util = Utils()

        self.host = hst
        self.port = prt

        self.URIs = {}
        self.URIs['LOG'] = "/api/login"
        self.URIs['OBS'] = "/api/obstacles"
        self.URIs['TEL'] = "/api/telemetry"
        self.URIs['MIS'] = "/api/missions"

        self.componentsAvailable = False

        self.mission_components = {}

        self.mission_components['OBS'] = {}
        self.mission_components['WYP'] = {}
        self.mission_components['STI'] = {}
        self.mission_components['TAR'] = {}
        self.mission_components['FLZ'] = {}

        self.telemetry_buffer = Queue()
        self.sysTime = None
        
        self.username = usr
        self.password = pss
        self.logged_in = False
		
        try:
            while not self.logged_in:
                try:
                    self.client = interop.Client( url=self.host+":"+self.port,
                    username=self.username,password=self.password)
                    self.logged_in = True
                except requests.ReadTimeout:
                    self.logged_in = False
                    self.util.log("RETR: Login Competition server")

            #self.logged_in = True
            self.util.succLog("Successfully logged into competition server.")

            self.util.log("Starting the mission components process.")
            self.procMiss = Process(target=self.populateMissionComponents, args=())
            self.util.succLog("Successfully initiated multiproc mission components.")
            
            self.util.log("Starting the telemetry handeler function.")
            self.procTelem = Process(target=self.postTelemetryHandeler, args=())
            self.util.succLog("Successfully initiated multiproc telemetry handeler.")

        except interop.exceptions.InteropError:
            self.util.errLog("ERROR: Invalid login to competition server.")
        except requests.exceptions.ConnectionError:
            self.util.errLog("Connection error with competition server - Are you sure the Server is Running?")
            self.logged_in = False

	#==================
	#
	# Populates the mission components we need after each
	# time they are retrieved from the main task.
	#
	# Serves the purpose of synchronizing with mavlink thread module.
	#
	#==================
    def populateMissionComponents(self):
        while True:
            if not self.componentsAvailable:
                mission_data = self.getMissionData()[0]
                obstacle_data = self.getObstacles()

				# Update mission components
                self.mission_components['WYP'] = mission_data['mission_waypoints']
                self.mission_components['FLZ'] = mission_data['fly_zones']

                self.mission_components['TAR']['emergent_lastKnown'] = mission_data['emergent_last_known_pos']
                
                self.mission_components['TAR']['off_axis'] = mission_data['off_axis_target_pos']
                
                self.mission_components['TAR']['air_drop'] = mission_data['air_drop_pos']

                self.mission_components['OBS'] = obstacle_data
                self.componentsAvailable = True

	#========================
	#
	# Retrieves mission components from the mission class.
	# Triggers condition variable to allow for a new set to be retrieved.
	#
	#========================
    def getMissionComponents(self):
        if self.componentsAvailable:
            self.componentsAvailable = False
            return self.mission_components

	#===================
	#
	# Returns whether we're logged
	# into the competition server or not.
	#
	#===================
    def isLoggedIn(self):
        return self.logged_in

	#====================
	#
	# Grabs obstacle data from
	# interop server.
	#
	#====================
    def getObstacles(self):
        r = self.client.get(self.URIs['OBS'])
        return r.json()

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
                       pBgColor, pAlphanumeric, pAlphanumericColor, pDescription,
                       pActionableOverride, pAutonomous=False, pTeamId="CNU_IMPRINT",
                       pImagePath=None):
        imageAvailable = (pImagePath != None)
        mTarget = interop.Target(id=pId, user=pUser, type=pType,
                                    latitutde=pLat, longitude=pLon,
                                    orientation=pOrient, shape=pShape,
                                    background_color=pBgColor, alphanumeric=pAlphanumeric,
                                    alphanumeric_color=pAlphanumericColor, description=pDescription,
                                    autonomous=pAutonomous, team_id=pTeamId,
                                    actionable_override=pActionableOverride)
            
        if(self.client.isLoggedIn()):
            self.client.post_target(mTarget)
            if(imageAvailable):
                fileTypes = ['.jpg', '.png']
                imagePathValid = False
                for fileType in fileTypes:
                    if(pImagePath.endswith(fileType)):
                        imagePathValid = True
                    if(imagePathValid):
                        try:
                            mImage = Image(pImagePath)
                            self.client.post_target_image(pId, mImage)
                        except IOException:
                            self.util.err("ERROR: Error loading image file.")
                            
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
        telemetry = interop.Telemetry(latitude=lat,
                              			longitude=lon,
                              			altitude_msl=alt,
                              			uas_heading=hdg
						)
		
        self.telemetry_buffer.push(telemetry)
        
    #=======================
    # Handeler for pulling necessary
    # telemetry objects and posting 
    # them to the competition server
    #=======================
    def postTelemetryHandeler(self):
        while(True):
            if(not(self.telemetry_buffer.isEmpty())):
                mTelem = self.telemetry_buffer.pop()
                self.client.post_telemetry(mTelem)
                self.mission_components['STI'] = self.client.get(self.URIs['TEL']).json()[len(self.client.get(self.URIs['TEL']).json())-1]['timestamp']
            

	#=====================
	# Get the system time.
	#---------------------
	#=====================
    def getSystemTime(self):
        return self.mission_components['STI']

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
    def postTarget(self, typ='standard', lat=38.145215, lon=-76.427942, ori='n', shp='square', bgc='green', letter='A', color='white', image_path='~/image.png'):

        target = interop.Target(type=typ,
                        latitude=lat,
                        longitude=lon,
                        orientation=ori,
                        shape=shp,
                        background_color=bgc,
                        alphanumeric=letter,
                        alphanumeric_color=color)

        target = client.post_target(target)

        with open(image_path, 'rb') as f:
            image_data = f.read()
            self.client.put_target_image(target.id, image_data)

	#==========================
	#
	# Retrieve the mission data for the competition.
	#
	#==========================
    def getMissionData(self):
        r = self.client.get(self.URIs['MIS'])
        return r.json()


