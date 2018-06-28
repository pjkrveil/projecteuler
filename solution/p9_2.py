import math

#import pdb; pdb.set_trace()

for i in range(1, 1001):
	for j in range(i + 1, 1001):
			k = 1000 - i - j

			if i < j and j < k and i * i + j * j == k * k :
				ansList = [i, j, k]
				result = i * j * k

print ansList, result