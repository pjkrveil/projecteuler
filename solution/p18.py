import math

triangle = []

triangle.append([75])
triangle.append([95, 64])
triangle.append([17, 47, 82])
triangle.append([18, 35, 87, 10])
triangle.append([20, 04, 82, 47, 65])
triangle.append([19, 01, 23, 75, 03, 34])
triangle.append([88, 02, 77, 73, 07, 63, 67])
triangle.append([99, 65, 04, 28, 06, 16, 70, 92])
triangle.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
triangle.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
triangle.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
triangle.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
triangle.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
triangle.append([63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
triangle.append([04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23])


def sumUp(curPos):
	leftNum = triangle[curPos[0]+1][curPos[1]]
	rightNum = triangle[curPos[0]+1][curPos[1]+1]

	if leftNum > rightNum:
		triangle[curPos[0]][curPos[1]] += leftNum

	else:
		triangle[curPos[0]][curPos[1]] += rightNum

	return triangle[curPos[0]][curPos[1]]


def decDim(triangle):
	for i in range(len(triangle)-2, -1, -1):
		for j in range(0, len(triangle[i])):
			triangle[i][j] = sumUp([i, j])

	return triangle[0][0]


#import pdb; pdb.set_trace()

print decDim(triangle)
