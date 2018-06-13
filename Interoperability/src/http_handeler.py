#!/usr/bin/env python

#==========================================#
#        HTTP Handeler Class for           #
#    Websocket publication and retrieval   #
#                                          #
#         Author: David Kroell             #
#        Version: 2.0.3                    #
#                                          #
#==========================================#

import flask
import requests

from singleton import Singleton
from flask import request, jsonify


#===================================
#   HTTP Constants Singleton
#
#  The purpose of this class is to hold
# the variables that are served by the
# http web api
#===================================
@Singleton
class HTTPConstants():
	def __init__(self):
		print "Starting the Constants Singleton."
		self.mission = {}
		self.mission['initilized'] = True

		self.telemetry = {}
		self.telemetry['initialized'] = True

		self.obstical_stationary = {}
		self.obstical_stationary['initialized'] = True

		self.obstical_moving = {}
		self.obstical_moving['initialized'] = True

	# Getters for the API components
	def getMission(self):
		return self.mission

	def getTelemetry(self):
		return self.telemetry

	def getObsticalStationary(self):
		return self.obstical_stationary

	def getObsticalMoving(self):
		return self.obstical_moving

	# Setters for the API Components
	def setMission(self, pMis):
		self.mission = pMis

	def setTelemetry(self, pTelem):
		self.telemetry = pTelem

	def setObsticalStationary(self, pOS):
		self.obstical_stationary = pOS

	def setObsticalMoving(self, pOM):
		self.obstical_moving = pOM

# Initialization of the Web Application.
# Utilizes the Singleton instance of the HTTPConstants that it serves.
def WebappAPIInit(pPort):
	app = flask.Flask(__name__)
	app.config["DEBUG"] = True
	const = HTTPConstants()

	@app.route('/', methods=['GET'])
	def home():
		return '''<h1>MISCONSYS Web API</h1>
<p>Mission Configuration System API for class constants including such things like telemetry <br> and Mission constants from the competition server.</p>'''


	@app.route('/api/v1/telemetry', methods=['GET'])
	def api_telemetry():
		#const = HTTPConstants()
		return jsonify(const.getTelemetry())

	@app.route('/api/v1/mission', methods=['GET'])
	def api_mission():
		#const = HTTPConstants()
		return jsonify(const.getMission())

	@app.route('/api/v1/obstical_stationary', methods=['GET'])
	def api_OS():
		#const = HTTPConstants()
		return jsonify(const.getObsticalStationary())

	@app.route('/api/v1/obstical_moving', methods=['GET'])
	def api_OM():
		#const = HTTPConstants()
		return jsonify(const.getObsticalMoving())

	app.run(host="0.0.0.0", port=pPort, debug=False, use_reloader=False)



#================================
#  Function used to return JSON
# data with Waypoints required by comp.
#================================
def grabWaypoints():
	obj = requests.get("http://0.0.0.0:5000/api/v1/mission")
	WYP = obj.json()['WYP']

	return WYP


if __name__ == "__main__":
	WebappAPIInit()
