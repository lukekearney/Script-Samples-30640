import sys

# this script uses python 3. For python , see recursive_countdown.py
# Run this script from the command line using "python recursive_countdown.py #" where # is replaced with an integer number of your choosing
# Note that you will need to cd into the same directory as this file. You can also call this script using "python /path/to/this/file.py #"
# Once you understand this script you should be able to write up to step 3 of the In an Indian File


def chain(n):
	print("n is " + str(n))
	if n >= 1:
		k = n - 1;
		print("there are " + str(k) + " more functions to execute")
		chain(k)
	else:
		print("No more chain to create. End of sequence")
	print("Finishing function n = " + str(n))



# this allows us to run the python script from the command line
if __name__ == "__main__":
	# check length of arguments
	if len(sys.argv) > 1:
		# initiate the function using the command line argument, converted to an integer (by default arguments are read as strings)
		chain(int(sys.argv[1]))