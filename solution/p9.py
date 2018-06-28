import math

def pythTriplets(n = 1000):
	for z in xrange(5, n+1):
		z2 = z*z
		x = x2 = 1
		y = z-1; y2 = y*y

		while x < y:
			xy2 = x2 + y2

			if xy2 == z2:
				yield x, y, z

				x += 1; x2 = x*x
				y -= 1; y2 = y*y

			elif xy2 < z2:
				x += 1; x2 = x*x

			else:
				y -= 1; y2 = y*y

def getAnswer(pythList, condition):
	for i in pythList:
		if i[0] + i[1] + i[2] == condition:
			return i

pList = list(pythTriplets(1000))
ansValue = getAnswer(pList, 1000)
answer = ansValue[0] * ansValue[1] * ansValue[2]

print ansValue, answer