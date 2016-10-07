#!/bin/bash
# complete version of make_lab_directories_while_loop_starter.sh (yeah, that's a mouthful isn't it!)
# this bash script uses a while loop to generate a series of lab directories. It prompts the user for 2 numbers and uses them as a starting and ending number. Maybe as an improvement/practise problem try using command line arguments instead?

echo "What's the first week?"
# read in the first value and save in a variable called counter
read counter

echo "What is the highest number week?"
# read in the final value
read final

while [ $counter -le $final ]; do
	# -d checks if the string given matches an existing directory
	if ! [ -d "lab$counter" ]; then
		# make the directory. Format lab# where # is the number
		# note the use of $counter within the string. 
		mkdir "lab$counter"
	else
		# this is similar to what would be output if we didn't check ifthe directory already existed or not, but demonstrates use of a command inside a string argument
		echo "$(pwd)/lab$counter already exists and is a directory"
	fi
	# rounded brackets denote arithmetic operations
	((counter++))
done

