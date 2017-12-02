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
    def __init__(self, hst="0.0.0.0", prt="8080", usr="testadmin", pss="testpass"):
        
