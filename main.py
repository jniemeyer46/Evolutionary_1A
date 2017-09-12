import sys
import string
import config1

def main():
	print(config1.random.randrange(1,21))

	# obtain the problem file and throw it into a list object
	shapes = open(sys.argv[2]).read().splitlines()
	
	# Variables that will be used to set the 2d array of material
	maxWidth = shapes[0].split(" ",1)[0]
	maxLength = getLength(shapes)

	# REMOVE THESE BEFORE SUBMISSION
	print(maxWidth)
	print(maxLength)

	# the material sheet being used to cut out shapes
	materialSheet = [[0 for x in range(0, int(maxWidth))] for y in range(0, int(maxLength))]


# will return the maxLength of the sheet of material
def getLength(listShapes):
	maxLength = 0

	for shape in listShapes:
		print(shape)
		moves = shape.split(" ")
		print(moves)
		if shape[0].isdigit():
			pass
		elif 'L' not in shape and 'R' not in shape:
			maxLength += 1
		elif 'L' in shape and 'R' not in shape:
			maxLength += 1
			for element in moves:
				if element[0] == 'L':
					maxLength += int(element[1])
		elif 'L' not in shape and 'R' in shape:
			maxLength += 1
			for element in moves:
				if element[0] == 'R':
					maxLength += int(element[1])
		else:
			LCount = 0
			RCount = 0
			for element in moves:
				if element[0] == 'L':
					LCount += int(element[1])
				elif element[0] == 'R':
					RCount += int(element[1])
			if LCount > RCount:
				maxLength += LCount + 1
			elif LCount < RCount:
				maxLength += RCount + 1
			else:
				maxLength += LCount + 1
	return maxLength


if __name__ == '__main__':
	main()