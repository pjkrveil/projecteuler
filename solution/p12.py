import math

def checkFactor(num):
	if num == 1:
		fList = [1]
	else:
		fList = [1, num]

	for i in range(2, num):
		if num % i == 0:
			fList.append(i)

	return fList

def counter(fList):
	return len(fList)

def solution(fNum):
	num = 0
	incr = 1

	while True:
		fList = []

		num += incr 
		incr += 1

		if counter(checkFactor(num)) == fNum:
			break

	return num

#import pdb; pdb.set_trace()

print solution(500)
