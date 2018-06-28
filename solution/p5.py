import math
from math import factorial

#smallest multiple

# def gcd(x,y): return y and gcd(y, x % y) or x
def gcd(x, y):
	while (y):
		x, y = y, x % y

	return x

def lcm(x, y):
	return (x * y) // gcd(x, y)

n = 1

for i  in range(1, 21):
	n = lcm(n, i)

print(n)
