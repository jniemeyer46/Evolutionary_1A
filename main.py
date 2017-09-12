import sys
import string
import random
import time
import Length



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
	maxWidth = shapes[0].split(" ",1)[0]
	maxLength = Length.getLength(shapes)

	# opening the log file 
	result_log = open(prob_log_file, 'w')
	# formatting the result log with Result Log at the top
	result_log.write("Result Log\n")
	result_log.write("Random Seed = " + str(seed) + "\n\n")

	# runs through the program as many times as the config files says to
	for run in range(1, int(num_runs) + 1):
		# Titles each section with Run i, where i is the run number (1-30)
		result_log.write("Run " + str(run) + "\n")

		# the material sheet being used to cut out shapes
		materialSheet = [[0 for x in range(0, int(maxWidth))] for y in range(0, int(maxLength))]

		for fitness in range(0, int(evaluations)):
			solution = []
			result_log.write(str(fitness + 1 ) + "	" + "score\n")

		# formatting the result log with a space after each run block
		result_log.write("\n")

	result_log.close()

if __name__ == '__main__':
	main()