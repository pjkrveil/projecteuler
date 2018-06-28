import math
#import pdb; pdb.set_trace()

largestPalNum = 0

for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		num = i * j
		strnum = str(num)

		if strnum == strnum[::-1] and num > largestPalNum:
			largestPalNum = num

print largestPalNum




#Orignal Version

# import math
# #import pdb; pdb.set_trace()

# largestPalNum = 0

# for i in range(999, 99, -1):
# 	for j in range(999, 99, -1):
# 		num = i * j
# 		strnum = str(num)

# 		if len(strnum) % 2 == 0:
# 			token1 = strnum[:len(strnum)//2]
# 			token2 = strnum[len(strnum)//2:]

# 		else:
# 			token1 = strnum[:len(strnum)//2]
# 			token2 = strnum[len(strnum)//2 + 1:]

# 		if token1 == token2[::-1] and num > largestPalNum:
# 			largestPalNum = num

# print largestPalNum
