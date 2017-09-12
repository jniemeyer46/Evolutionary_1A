import sys
import string
import random
import time
import Length
import rotate
import shapeManipulation


def main():
	#obtain configs in a list format
	config = open(sys.argv[1]).read().splitlines()

	# obtain the problem file and throw it into a list object
	shapes = open(sys.argv[2]).read().splitlines()
	
	# setting up variables using config file
	for rules in config:
		info = rules.split(" ")
		if info[0] == "fitness_evaluations":
			evaluations = info[1]
		elif info[0] == "runs":
			num_runs = info[1]
		elif info[0] == "prob_log":
			prob_log_file = info[1]
		elif info[0] == "prob_solution":
			prob_solution_file = info[1]
		elif info[0] == "seed":
			seed = eval(info[1])

	# Seeds the random function using a saved value that is put into the log file
	random.seed(seed)

	# Variables that will be used to set the 2d array of material
	maxWidth = shapes[0].split(" ")[0]
	maxLength = Length.getLength(shapes)
	#number of shapes in the problem file
	numShapes = shapes[0].split(" ")[1]

	# opening the log file 
	result_log = open(prob_log_file, 'w')
	# formatting the result log with Result Log at the top
	result_log.write("Result Log\n")
	result_log.write("Random Seed = " + str(seed) + "\n\n")

	# runs through the program as many times as the config files says to
	for run in range(1, int(num_runs) + 1):
		# highest fitness calculation thus far this run
		highest_fitness = 0

		# Open the current solution file to obtain the fitness value
		solution_file = open(prob_solution_file).read().splitlines()
			
		# grabs the solution file's fitness value
		solution_fitness = solution_file[1].split(" ")[3]

		# Titles each section with Run i, where i is the run number (1-30)
		result_log.write("Run " + str(run) + "\n")

		# run through the given amount of times given by fitness evaluation
		for fitness in range(1, int(evaluations)+1):
			# list of solution locations incase it is the best
			solution_locations = []

			# holders for length of material used
			LargestX = 0
			SmallestX = 156

			# the material sheet being used to cut out shapes
			materialSheet = [[0 for x in range(0, int(maxWidth))] for y in range(0, int(maxLength))]

			# for every shape in the file, choose a position
			for shape in shapes:
				if not shape[0].isdigit():
					valid = False

					# Keep obtaining a new position until it fits on the material
					while not valid:
						# generate random position and rotation
						x_cord = random.randrange(0, int(maxLength))
						y_cord = random.randrange(0, int(maxWidth))
						rotation = random.randrange(0,4)

						# Rotate the shape if needed
						if rotation != 0:
							shape = rotate.rotate_shape(rotation, shape)

						# Check whether the shape fits on the material in the current position
						valid = shapeManipulation.validPlacement(materialSheet, maxLength, maxWidth, x_cord, y_cord, shape)
							
						# if the move was valid and was placed
						if valid:
							shapeManipulation.placeShape(materialSheet, x_cord, y_cord, shape)
							# store the location in a tuple if it worked
							placementLocation = (x_cord, y_cord, rotation)
							# append it to the list
							solution_locations.append(placementLocation)

			# obtains the smallest and largest position in the material array
			for i in range(len(materialSheet)):
				if 1 in materialSheet[i]:
					if i < SmallestX:
						SmallestX = i
					elif i > LargestX:
						LargestX = i

			# Determines the Length of the material used by this iteration
			usedLength = ((LargestX - SmallestX) + 1)
			#print(usedLength)
			current_fitness = fitnessCalc(maxLength, usedLength)
			if highest_fitness < current_fitness:
				highest_fitness = current_fitness
				result_log.write(str(fitness + 1 ) + "	" + str(current_fitness) + "\n")

			# If the current solution is the best, replace the info in the file with the new solution
			if int(solution_fitness) < highest_fitness:
				solution_file = open(prob_solution_file, 'w')

				solution_file.write("Solution File\n")
				solution_file.write("Fitness Calculation = " + str(highest_fitness) + "\n\n")

				for i in range(len(solution_locations)):
					solution_file.write(str(solution_locations[i])[1:-1] + "\n")

		# formatting the result log with a space after each run block
		result_log.write("\n")

	result_log.close()


def fitnessCalc(maxLength, usedLength):
	# determine the fitness of the evaluation
	fitness_calculation = maxLength - usedLength

	return fitness_calculation


if __name__ == '__main__':
	main()