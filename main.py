import sys
import string
import config


def main():
	print(sys.argv[1])
	print(sys.argv[2])
	print(config.random.randrange(1,21))

	shapes = open(sys.argv[2]).read().splitlines()

	print(shapes)
	print(shapes[0].split(" ",1)[0])


if __name__ == '__main__':
	main()