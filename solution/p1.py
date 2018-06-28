import math

numList = []
t = 1
result = 0

for i in range(1, 1000) :
	if i % 3 == 0 or i % 5 == 0:
		numList.append(i)

for i in numList:
	result += i

print result