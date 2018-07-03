import math

longestLength = 0

def collatzSeq(start):
	length = 1
	lastElm = start

	while lastElm != 1:
		if lastElm % 2 == 0:
			lastElm = lastElm // 2

		else:
			lastElm = 3 * lastElm + 1

		length += 1

	return length

for i in range(2, 1000001):
	temp = collatzSeq(i)

	if longestLength < temp:
		longestLength = temp
		num = i

print longestLength, num