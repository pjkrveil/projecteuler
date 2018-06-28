import math

def pFactors(n):
	i = 2
	factors = []

	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)

	if n > 1:
		factors.append(n)

	return factors

n1 = 13195
n2 = 600851475143



print pFactors(n2)[-1]