import math

def fib_to(n):
	fibs = [1, 2]
	t = 1
	result = 0

	for i in range(2, n+1):
		if (fibs[-1] < 4000000):
			fibs.append(fibs[-1] + fibs[-2])

	for i in fibs:
		if i % 2 == 0:
			result += i

	return result

print fib_to(50)