import sys
import string
import random
import time
import getLength

seed = time.time()
print(seed)
random.seed(seed)

print(random.random())
def main():

	# obtain the problem file and throw it into a list object
	shapes = open(sys.argv[2]).read().splitlines()
	config = open(sys.argv[1]).read().splitlines()
	
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
		else:
			pass

	print(evaluations + " " + num_runs + " " + prob_log_file + " " + prob_solution_file)

	# Variables that will be used to set the 2d array of material
	maxWidth = shapes[0].split(" ",1)[0]
	maxLength = getLength.getLength(shapes)

	# runs through the program as many times as the config files says to
	for run in range(0, int(num_runs)):

		# the material sheet being used to cut out shapes
		materialSheet = [[0 for x in range(0, int(maxWidth))] for y in range(0, int(maxLength))]


if __name__ == '__main__':
	main()