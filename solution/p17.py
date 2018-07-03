import math

def firstDigit(num, counting):
	numLength = len(str(num))

	if numLength == 3:
		numpart = int(str(num)[1:])

	else:
		numpart = num

	if numpart >= 10 and numpart < 20:
		return counting

	else:
		firstdig = int(str(num)[-1])

		if firstdig == 1 or firstdig == 2 or firstdig == 6:
			counting += 3

		if firstdig == 4 or firstdig == 5 or firstdig == 9:
			counting += 4

		if firstdig == 3 or firstdig == 7 or firstdig == 8:
			counting += 5

		return counting

def secDigit(num, counting):
	numLength = len(str(num))

	if numLength == 3:
		numpart = int(str(num)[1:])

	else:
		numpart = num

	if numpart >= 10 and numpart < 20:
		if numpart == 10:
			counting += 3

		if numpart == 11 or numpart == 12:
			counting += 6

		if numpart == 15 or numpart == 16:
			counting += 7

		if numpart == 13 or numpart == 14 or numpart == 18 or numpart == 19:
			counting += 8

		if numpart == 17:
			counting += 9

	else:
		secdig = int(str(num)[1])

		if secdig == 4 or secdig == 5 or secdig == 6:
			counting += 5

		if secdig == 2 or secdig == 3 or secdig == 8 or secdig == 9:
			counting += 6

		if secdig == 7:
			counting += 7

	return counting

def thirdDigit(num, counting):
	thirddig = int(str(num)[0])

	counting = firstDigit(thirddig, counting)

	counting += 10

	return counting


def readNum(num):
	numLength = len(str(num))
	counting = 0

	if numLength == 4:
		counting = 11

	if numLength == 3:
		counting = firstDigit(num, secDigit(num, thirdDigit(num, counting)))

	if numLength == 2:
		counting = firstDigit(num, secDigit(num, counting))

	if numLength == 1:
		counting = firstDigit(num, counting)

	return counting

result = 0


#import pdb; pdb.set_trace()

for i in range(1, 1001):
	result += readNum(i)

print result