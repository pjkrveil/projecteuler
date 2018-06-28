import math

def findFactor(num, fList=[]):
	for i in range(2, num+1):
		if num % i == 0:
			fList.append(i)
			findFactor(num / i, fList)
			break

	return fList


n1 = 13195
n2 = 600851475143

print findFactor(n2)

"""
import pdb; pdb.set_trace()
print findFactor(n1)
"""
