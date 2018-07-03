import math

def numOfDiv(num):
	nod = 0
	sqrt = int(math.sqrt(num))

	for i in range(1, sqrt+1):
		if num % i == 0:
			nod += 2

	if sqrt ** 2 == num:
		nod -= 1

	return nod

def solution(dNum):
	num = 0
	incr = 1

	while (numOfDiv(num) < dNum):
		num += incr
		incr += 1

	return num

print solution(500)