import math

num = str(math.factorial(100))

result = 0

for i in range(0, len(num)):
	temp = int(num[i])
	result += temp

print result