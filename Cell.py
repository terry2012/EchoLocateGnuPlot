class Cell(object):
	def __init__(self):
		self.cellName = None
		self.cellLat = None
		self.cellLong = None
		self.cellCalls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.cellSetupFailures = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.cellDrops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.cellAudioIssue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	def add(self,type,hour):
		if(type == 'call'):
			self.cellCalls[hour] = self.cellCalls[hour]+1
		elif(type == 'callDrop'):
			self.cellDrops[hour] = self.cellDrops[hour]+1
		elif(type == 'setupFailure'):
			self.cellSetupFailures[hour] =self.cellSetupFailures[hour]+1
		elif(type == 'audioIssue'):
			self.cellAudioIssue[hour] = self.cellAudioIssue[hour]+1
	def toString(self):
		s1 = str(self.cellName) + '\t' + str(self.cellLat) + '\t' + str(self.cellLong) + '\t'+\
			str(self.cellCalls)+'\t'+str(self.cellSetupFailures)+'\t'+str(self.cellDrops)+'\t'+\
			str(self.cellAudioIssue)
		return s1
	
	
	
