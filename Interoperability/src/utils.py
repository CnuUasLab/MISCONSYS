import os
from singleton import Singleton

#===============
# Static class for OS
# Constant use on headers.
#===============
class bcolors:
	HEADER = '\033[95m'
    	OKBLUE = '\033[94m'
    	OKGREEN = '\033[92m'
    	WARNING = '\033[93m'
    	FAIL = '\033[91m'
    	ENDC = '\033[0m'
    	BOLD = '\033[1m'
	SUCCESS = '\033[1;42m'
    	UNDERLINE = '\033[4m'
    	ERROR = '\033[1;41m'

        
#==================================
#  Queue to handel the
#  continuous posting process.
#==================================
class Queue():
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


#=============================
#
# Utilities class for loging messages in the console
# Class takes on a singleton pattern.
#
#=============================
@Singleton
class Utils():
	def __init__(self):
		self.logs = []
		self.currLog = 'Initialized'

	def log(self, string):
		print bcolors.BOLD + string + bcolors.ENDC
		self.currLog = string
		self.logs.append(string)
        
	def prompt(self, question, affirmOpt):
		'''
			Not functional yet. Will be used for CLI.
		'''
		opt = input(bcolors.BOLD + question + bcolors.ENDC)
		if (opt in affirmOpt):
			return True
		else:
			return False

	def errLog(self, string):
		print bcolors.ERROR + string + bcolors.ENDC

		self.currLog = string
                self.logs.append(string)

	def succLog(self, string):
		print bcolors.SUCCESS + string + bcolors.ENDC

		self.currLog = string
                self.logs.append(string)

	def getPreviousLogs(self):
		return self.logs

#	def dump(self):
#		f = open("./dumpFile.txt","w+")
#		for (word in self.getPreviousLogs()):
#			f.write(word)
