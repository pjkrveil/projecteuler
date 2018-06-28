import math

#import pdb; pdb.set_trace()

def primeNumList(n):

	# store prime number in the list
	numList = [2]

	# start from 3
	num = 3

	while len(numList) != n:

		t = 0

		for p in numList:
			t = p

			if num % p == 0:
				break
		
		if numList[-1] == t and num not in numList:
				numList.append(num)

		num += 2

	return numList[-1]

numb = int(raw_input("Type n for n-th prime number: "))

print primeNumList(numb)