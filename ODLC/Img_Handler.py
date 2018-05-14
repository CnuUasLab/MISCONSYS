#!/usr/bin/python2
from PIL import Image
import pandas as pd
import math

class Img_Handler:
	'api for cropping photos'

	def __init__(self, _pullDir, _saveDir, _size=150, _offset=-50, _imgXY=(4000,3000), _imgDataFile="photolog.txt"):
		self.pullDir = _pullDir
		self.saveDir = _saveDir
		self.size = _size
		self.offset = _offset
		self.imgXY = _imgXY
		self.imgData = Img_Data(self.pullDir, self.saveDir, _imgDataFile)

	def cropSingle(self, imgName):
		img = Img_Obj(self.pullDir, self.saveDir, imgName)
		img.loadImg()

		step = self.size + self.offset

		latLonAltYaw = self.imgData.getLatLonAltYaw(imgName)

		for x in range(0, self.imgXY[0], step):
			for y in range(0, self.imgXY[1], step):

				xMax = x+self.size
				yMax = y+self.size

				subImg = img.crop(x, y, xMax, yMax)
				saveName = imgName[:imgName.rfind('.')] + "_" + str(x) + "_" + str(y) + ".jpg"
				subImg.save(saveName)

				latLon = self.imgData.calcLatLon(latLonAltYaw, x, y, self.size, self.imgXY)

				fileName = imgName[:imgName.rfind('.')] + ".txt"
				self.imgData.save(latLon, fileName)


class Img_Obj:
	'handles reading, writing, and manipulating actual images'

	def __init__(self, _pullDir, _saveDir, _imgName, _img=None):
		self.pullDir = _pullDir
		self.saveDir = _saveDir
		self.imgName = _imgName
		self.img = _img

		#self.loadImg()

	def loadImg(self):
		self.img = Image.open(self.pullDir + self.imgName)

	def crop(self, xMin, yMin, xMax, yMax):
		tmp_obj = Img_Obj(None, self.saveDir, None, None)
		tmp_obj.img = self.img.crop((xMin, yMin, xMax, yMax))
		return tmp_obj

	def save(self, saveName):
		self.img.save(self.saveDir + saveName)

class Img_Data:
	'handles reading, writing, and calculations on image data'

	def __init__(self, _pullDir, _saveDir="./", _dataFile="photolog.txt", _imgDir=None):
		self.pullDir = _pullDir
		self.dataFile = _dataFile

		if(_imgDir is None):
			_imgDir = _pullDir

		self.imgDir = _imgDir
		self.df = pd.read_csv(self.pullDir + self.dataFile)

	def getLatLonAltYaw(self, imgName):
		for x in range(0,len(self.df)):

			imgNameLoc = self.df.iloc[x][' fileName'].rfind('/')+1
			imgName = self.df.iloc[x][' fileName'][imgNameLoc:]

			if(imgName == imgName):
				lat = self.df.iloc[x][' lat']
				lon = self.df.iloc[x][' lng']
				alt = self.df.iloc[x][' relativeAltitude']
				yaw = self.df.iloc[x][' yaw']
				return (lat, lon, alt, yaw)
				
		return None

	def calcLatLon(self, latLonAltYaw, xMin, yMin, subSize, origXY):
		if(latLonAltYaw is None):
			return None

		lat = latLonAltYaw[0]
		lon = latLonAltYaw[1]
		alt = latLonAltYaw[2]

		# if camera is rotated +90 degrees from plane yaw
		yaw = latLonAltYaw[3] + 90 # TODO: check this assumption

		xMid = xMin+subSize/2
		yMid = yMin+subSize/2

		FOV = 80.0
		origDist = 2 * alt * math.tan( math.radians(FOV) / 2.0 )
		xOffset = xMid - origXY[0] / 2.0
		yOffset = origXY[1] / 2.0 - yMid

		subX = xOffset / origXY[0] * origDist
		subY = yOffset / origXY[1] * origDist

		lat = lat + subY / 111111.0 * math.sin(yaw)
		lon = lon + subX / 111111.0 * math.cos(lat) * math.cos(yaw)

		return (lat, lon)

	def save(self, latLon, fileName):
		# TODO: append data to file
		return None

ih = Img_Handler("./sample-data/", "./generated-images/", _size=500, _offset=-250)

ih.cropSingle("sample.jpg")