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
#       pHost - hostname
#       pPort - port that the competition server runs on
#       pUser - Username for the competition server
#       pPass - Password for the competition server
#       pPID  - Process ID for the daemon - Do not mess with this.
#
#=========================================
class Mission():
    def __init__(self, pHost="0.0.0.0", pPort="8080",
                 pUser="testadmin", pPass="testpass", pPID="./pid/mission_proc.pid"):

        # Identify Host and Port foir class vars
        self.host = pHost
        self.port = pPort

        # Identify username and password.
        self.username = username
        self.password = password

        # Initialize object component data
        self.URIs = {}
        self.Mission_Components = {}
        
        # Initialize individual mission components
        self.Mission_Components['OBS'] = {}
        self.Mission_Components['WYP'] = {}
        self.Mission_Components['STI'] = {}
        self.Mission_Components['TAR'] = {}
        self.Mission_Components['FLZ'] = {}

        # Initialize server URIs
        self.URIs['LOG'] = "/api/login"
        self.URIs['OBS'] = "/api/obstacles"
        self.URIs['TEL'] = "/api/telemetry"
        self.URIs['MIS'] = "/api/missions"

        #Initialize condition variables
        self.missionComponentsAvailable = False

        self.logged_in = False
        try:
            while not self.logged_in:
                try:
                    self.client = interop.Client( url=self.host+":"+self.port,
                                                  username = self.username,
                                                  password = self.password
                                                  )
                    self.logged_in = True
                except requests.ReadTimeout:
                    self.logged_in = False
                    sys.exit()
                    
                    # Start Daemon Process here.
                    
                except interop.exceptions.InteropError:
                    sys.exit() # We didn't make it
                except requests.exceptions..ConnectionError:
                    self.logged_in = False
        

        
        
