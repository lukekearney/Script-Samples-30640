import sys

# this script uses python 2. For python 3, see recursive_countdown_py3.py
# Run this script from the command line using "python recursive_countdown.py #" where # is replaced with an integer number of your choosing
# Note that you will need to cd into the same directory as this file. You can also call this script using "python /path/to/this/file.py #"
# Once you understand this script you should be able to write up to step 3 of the In an Indian File


def chain(n):
	print "n is " + str(n)
	if n >= 1:
		k = n - 1;
		print "there are " + str(k) + " more functions to execute"
		chain(k)
	else:
		print "No more chain to create. End of sequence"
	print "Finishing function n = " + str(n)




if __name__ == "__main__":
	print sys.argv
	if len(sys.argv) > 1:
		chain(int(sys.argv[1]))