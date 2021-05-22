import random
class SecretWord:
	
	def __init__(self):
		self.secretWord = "a"
		self.wordProgress = []
		
	
	def guessWord(self, word):
		if word.upper() == self.secretWord:
			self.wordProgress = self.secretWord
			return True
		return False
	
	def guessLetter(self, letter):
		letter.upper()
		if letter in self.secretWord:
			index = 0
			for let in self.secretWord:
				if let == letter:
					self.wordProgress[index] = letter
				index += 1
			return True
		return False
	
	def getNewWord(self, min, max):
		possWords = []
		with open("res/words.txt") as wordList:
			for word in wordList.readlines():
				if len(word) >= min:
					possWords.append(word)
				
				if len(word) > max:
					break
		self.secretWord = (possWords[random.randrange(len(possWords))]).upper()
	
	def getWord(self):
		return self.secretWord
	
	def getProgress(self):
		return self.wordProgress