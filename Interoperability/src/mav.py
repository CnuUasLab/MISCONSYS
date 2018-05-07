#===============================================================#
#								#
#			Mavlink Library				#
#								#
#			Author: davidkroell    			#
#			Version: 2016-10-03			#
#								#
#	     This is the mavlink library that is used		#
#	  to send and recieve mavlink data from/to the plane.	#
#								#
#===============================================================#

from pymavlink import mavutil
from utils import Utils

import json
import socket
import thread

#====================
# Mavlink module class. Creates new instance of Mavlink Module
#
# ip: - Is the hostname of the place recieving packets.
# port - Is the port on which you recieve packets. (usually 14550)
#====================
class Mavlink():
    def __init__(self, ip, port):
        self.util = Utils()

	self.target_ip   = ip
        self.target_port = port

        self.new_packet = False
        self.current_packet = ""

        self.util.log("Starting mavudp session on - "+str(self.target_ip)+":"+str(self.target_port))
        self.mav = mavutil.mavudp(str(self.target_ip)+":"+str(self.target_port), input=True)

        thread.start_new_thread(self.startUDPStream, ())

    # Function called in the thread to constantly update packets.
    def startUDPStream(self):
        while True:
            #	statusPacket = mav.recv()
            status = self.mav.recv_msg()
            if(status!=None and not(self.new_packet)):
                self.new_packet = True
		self.current_packet = status

    # Accessor, to get the current packet
    def getMavPacket(self):
        if(self.new_packet):
            self.new_packet = False
            return self.current_packet
        else:
            return None

    # Posts data to the airplane.
    def postData(self, packet):
        '''
        We gotta figure out how to do this.
        I'm researching it.
        '''
        pass
