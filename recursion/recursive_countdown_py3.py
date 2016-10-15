import sys

# this script uses python 3. For python , see recursive_countdown.py
# Run this script from the command line using "python recursive_countdown.py #" or "python3 recursive_countdown.py #" where # is replaced with an integer number of your choosing
# Note that you will need to cd into the same directory as this file. You can also call this script using "python /path/to/this/file.py #"
# Once you understand this script you should be able to write up to step 3 of the In an Indian File

# a function that takes a number (integer) as a parameter // 10
def chain(n):
	# displays the value of the argument(number) // 10
	print("n is {}".format(n))
	# the following is true as long as the value of n is greater or equal to one // if 10 >= 1
	if n >= 1:
		# variable k subracts 1 from n // k = 9
		k = n - 1;
		# there are 9 more functions to execute
		print("there are {} more functions to execute".format(k))
		# the function calls itself with the previous number as an argument // chain(9)
		# the magic happens here, the function will keep calling itself until line number 13 fails
		chain(k)
	# Once that fails, the following is printed
	else:
		print("No more chain to create. End of sequence")
	print("Finishing function n = {}".format(n))



# this allows us to run the python script from the command line
if __name__ == "__main__":
	# check length of arguments
	if len(sys.argv) > 1:
		# initiate the function using the command line argument, converted to an integer (by default arguments are read as strings)
		chain(int(sys.argv[1]))