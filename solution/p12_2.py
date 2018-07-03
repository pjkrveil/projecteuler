import math

def primeNumList(n):
	pList = [2]
	num = 3

	while len(pList) != n:
		t = 0

		for p in pList:
			t = p

			if num % p == 0:
				break
		
		if pList[-1] == t and num not in pList:
				pList.append(num)

		num += 2

	return pList

def counterFactor(num):
	numDiv = 0
	pList = primeNumList(num)

	for p in pList:
		numDiv += (num // p)

	return numDiv

def solution(fNum):
	num = 0
	incr = 1

	while True:
		fList = []

		num += incr 
		incr += 1

		if counterFactor(num) == fNum:
			break

	return num

#import pdb; pdb.set_trace()

print solution(500)
