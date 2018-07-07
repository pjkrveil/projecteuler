def ascii2chr(word):
	result = 0

	for i in word:
		temp = int(ord(i))
		temp -= 64
		result += temp

	return result

def sortWord(wordList):
	length = len(wordList) - 1

	for i in range(length):
		for j in range(length - i):
			if len(wordList[j]) < len(wordList[j+1]):
				shortLength = len(wordList[j])
			else:
				shortLength = len(wordList[j+1])

			for k in range(shortLength):
				if ascii2chr(wordList[j][k]) > ascii2chr(wordList[j+1][k]):
					wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
				elif ascii2chr(wordList[j][k]) < ascii2chr(wordList[j+1][k]):
					break
				else:
					continue

	return wordList

wordList = []

with open('p022_names.txt') as inputfile:
	for line in inputfile:
		wordList = line.split(',')

for i in range(0, len(wordList)):
	wordList[i] = wordList[i][1:-1]

wordList = sortWord(wordList)

scoreList = []

for i in range(0, len(wordList)):
	scoreList.append((i+1) * ascii2chr(wordList[i]))

import pdb; pdb.set_trace()

totalSum = sum(scoreList)

print totalSum

#maxIdx = scoreList.index(max(scoreList))

#print "%s, %s scores" % (wordList[maxIdx], scoreList[maxIdx])



