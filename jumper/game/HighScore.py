class HighScore:
	
	def __init__(self):
		self.fileName = "res/HighScores.txt"
		self.maxRecords = 35
	
	def checkScore(self, score):
		with open(self.fileName) as records:
			data = ""
			for rec in records:
				data = rec
			if data.split(":")[1] < score:
				records.close()
				return True
			records.close()
		return False
	
	def saveScore(self, score, name):
		curRec = []
		with open(self.fileName) as ifile:
			for line in ifile.readlines():
				curRec.append(line)
			ifile.close()
		
		index = 0
		with open(self.fileName, "w") as ofile:
			newEntry = False
			for _ in range(50):
				if int(curRec[index].split(":")[1]) > score or newEntry:
					ofile.write(curRec[index])
					index += 1
				else:
					ofile.write(str(score) + ":" + name)
					newEntry = True
			ofile.close()
			
	
	def getTopScores(self, top):
		topScores = []
		with open(self.fileName) as ifile:
			for line in ifile.readlines():
				data = line.split(":")
				topScores.append({"name":line[0], "score":data[1]})
				if len(topScores) > top:
					break
		return topScores
