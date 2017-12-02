#=====================================================#
#                                                     #
#            Mission Handeler, and Processor          #
#         Center for the Ground Control Station       #
#                                                     #
#                Author: David Kroell                 #
#                        Joseph Doye                  #
#                                                     #
#               Version: 1.0.1                        #
#                                                     #
#=====================================================#

import sys
import requests
import thread
import re

sys.path.insert(0, "../interop/client")
import interop

sys.path.insert(0, "../daemon_py")
from daemon import Daemon

#=========================================
#
# Mission module class for the mission
# that is a singleton class.
#
#-----params:----------------------------
#       hst - hostname
#       prt - port that the competition server runs on
#       usr - Username for the competition server
#       pss - Password for the competition server
#       pid - Process ID for the daemon
#
#=========================================
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

		self.sysTime = None

		self.username = usr
		self.password = pss

		self.logged_in = False
		try:
                        while not self.logged_in:
                                try:
			                self.client = interop.Client( url=self.host+":"+self.port,
							              username=self.username,
							              password=self.password
				        )
                                        self.logged_in = True
                                except requests.ReadTimeout:
                                        self.logged_in = False
                                        self.util.log("RETR: Login Competition server")

                        #self.logged_in = True
			self.util.succLog("Successfully logged into competition server.")

			self.util.log("Attempting to start Competition Server Retrieval Thread.")
			thread.start_new_thread(self.populateMissionComponents, ())
			self.util.succLog("Successfully started mission retrieval thread.")

		except interop.exceptions.InteropError:
			self.util.errLog("ERROR: Invalid login to competition server.")
		except requests.exceptions.ConnectionError:
			self.util.errLog("Connection error with competition server - Are you sure the Server is Running?")
			self.logged_in = False

 # ==================
    #
    # Populates the mission components we need after each
    # time they are retrieved from the main task.
    #
    # Serves the purpose of synchronizing with mavlink thread module.
    #
    # ==================
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

        pass

    # ===================
    #
    # Returns whether we're logged
    # into the competition server or not.
    #
    # ===================
    def isLoggedIn(self):
        #return true or false depending on connection status
        return self.logged_in

    # ====================
    #
    # Grabs obstacle data from
    # interop server.
    #
    # ====================
    def getObstacles(self):
        r = self.client.get(self.URIs['OBS'])
        return r.json()

        # =================================================
        # Post a target to the server that may
        #  or may not have image data with it.
        #
        # --------------params:--------------
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
        # =================================================

    def postTarget(self, pId, pUser, pType, pLat, pLon, pOrient, pShape,
                       pBgColor, pAlphanumeric, pAlphanumericColor, pDescription,
                       pActionableOverride, pAutonomous=False, pTeamId="CNU_IMPRINT",
                       pImagePath=None):
        thisTarget = interop.odlc(self, id = pId,user =  pUser,type =  pType,latitude =  pLat,longitude = pLon,orientation = pOrient,shape = pShape,
                       background = pBgColor,ahphanumeric =  pAlphanumeric,alphanumeric_color = pAlphanumericColor,description = pDescription,
                       actionable_override = pActionableOverride, pAutonomous=False, pTeamId="CNU_IMPRINT",
                       pImagePath=None)
        if(self.client.isLoggedIn()):

            self.client.post_target(thisTarget)



        # ========================
        # Post telemetry to the server.
        #
        # -------params:----------
        #	  lat - latitude value of plane.
        #	  lon - longitude value of plane.
        #	  alt - altitutde of the plane.
        #	  hdg - uas heading fo plane.
        # ========================
    def postTelemetry(self, lat=38.145245, lon=-76.427946, alt=50, hdg=90):
        tel = interop.Telemetry(latitude = lat, longitude = lon, altitude = alt, heading = hdg)
        pass

    # =====================
    # Get the system time.
    # ---------------------
    # =====================
    def getSystemTime(self):
        return self.mission_components['STI']

    # =============================
    # 	   Post a detected target on
    #	the field through the SIRE module.
    #
    # -------params:---------------
    #	  typ - The type of target
    #	  lat - latitude location of the target
    #	  lon - longitude location of the target
    #	  ori - Orientation of the target
    #	  shp - Shape of the target
    #	  bgc - background color of the taget
    #	  letter - Letter printed on the front of the target
    #	  color - color of the target text.
    #	  image_path - path of the image where target is found.
    # ============================
    def postTarget(self, typ='standard', lat=38.145215, lon=-76.427942, ori='n', shp='square',):
        target = interop.odlc(type=typ,
                        latitude=lat,
                        longitude=lon,
                        orientation=ori,
                        shape=shp)

        target = client.post_telemetry(target)

        self.mission_components['STI'] = self.client.get(self.URIs['TEL']).json()[len(self.client.get(self.URIs['TEL']).json()) - 1]['timestamp']
        # ==========================
        #
        # Retrieve the mission data for the competition.
        #
        # ==========================

    def getMissionData(self):
        m = self.client.get(self.URIs['MIS'])
        return m.json()

