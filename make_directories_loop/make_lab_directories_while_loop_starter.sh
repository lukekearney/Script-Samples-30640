#!/bin/bash
# this bash script uses a while loop to generate a series of lab directories. It prompts the user for 2 numbers and uses them as a starting and ending number. Replace the __ with the appropriate commands, variables etc

echo "What's the first week?"
# read in the first value and save in a variable called counter
__

echo "What is the highest number week?"
# read in the final value
__

while [ __ -le __ ]; do
	# -d checks if the string given matches an existing directory
	if ! [ -d "lab$counter" ]; then
		# make the directory. Format lab# where # is the number
		__
		
	else
		# this is similar to what would be output if we didn't check if the directory already existed or not, but demonstrates use of a command inside a string argument
		echo "$(pwd)/lab$counter already exists and is a directory"
	fi
	# rounded brackets denote arithmetic operations
	((current++))
done

