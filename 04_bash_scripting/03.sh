#!/bin/bash
# if else

# ,, is the parameter expansion it allows us to
# ignore upper and lower cases
if [ ${1,,} = hereliesadvaith ]; then
	echo "Hi chief welcome home"
elif [ ${1,,} = help ]; then
	echo "Enter your username"
else 
	echo "Who the hell are you ?"
#now close it
fi
