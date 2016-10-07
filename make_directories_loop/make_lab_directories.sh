#!/bin/bash

# this takes a list of numbers and creates a lab directory for each
for i in 2 3 4 5 6 7 8 9 10 11 12; do
	# -d checks if its a directory. ! inverts (so a condition that would evaluate to true then becomes false
	if ! [ -d "lab$i" ]; then
		mkdir "lab$i"
	else
		echo "lab$i already exists and is a directory"
	fi
done
