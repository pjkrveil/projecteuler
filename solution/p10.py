import math

def solution(n):
	multiples = set()

	for i in range(2, n+1):
		if i not in multiples:
			yield i
			multiples.update(range(i*i, n+1, i))


itr = 0
ml = list(solution(2000000))

for i in ml:
	itr += int(i)

print itr