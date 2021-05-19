import random
class SecretWord:
	
	def __init__(self):
		self.secretWord
		self.wordProgress
		
	
	def guessWord(self, word):
		
		return False
	
	def guessLetter(self, letter):
		
		return False
	
	def getNewWord(self, min, max):
		possWords = []
		with open("res/words.txt") as wordList:
			for word in wordList.readlines():
				if len(word) >= min:
					possWords.append(word)
				
				if len(word) > max:
					break
		self.secretWord = possWords[random.randrange(len(possWords))]
	
	def getWord(self):
		return self.secretWord
	
	def getProgress(self):
		return self.wordProgress