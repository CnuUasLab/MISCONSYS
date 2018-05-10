#===========================================================#
#                                                           #
#                      Mavlink Library                      #
#                                                           #
#                    Author: davidkroell                    #
#                    Version: 2017-11-16                    #
#                                                           #
#	     This is the mavlink library that is used		    #
#	  to send and recieve mavlink data from/to the plane.	#
#                                                           #
#===========================================================#

from pymavlink import mavutil
from utils import Utils, Queue
from multiprocessing import Process

import json
import socket
import thread
import traceback

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
        
        self.MavBuffer = Queue()
        
        # thread.start_new_thread(self.startUDPStream, ())
        self.procMav = Process(target=self.startUDPStream, args=())

    # Function called in the thread to constantly update packets.
    def startUDPStream(self):
        while True:
            try:
                #statusPacket = mav.recv()
                status = self.mav.recv_msg()
                if (status != None):
                    self.MavBuffer.push(status)
            except:
                self.util.errLog("UDP Stream Error Occured.")
                traceback.print_exc()
                

    # Accessor, to get the current packet
    def getMavPacket(self):
        if(not(self.MavBuffer.isEmpty())):
            return self.MavBuffer.pop()
        else:
            return None

    # Posts data to the airplane.
    def postData(self, packet):
        '''
        We gotta figure out how to do this.
        I'm researching it.
        '''
        pass
