#!/bin/bash
# exit code

showName(){
	echo Hello $1
	if [ ${1,,} = advaith ]; then
		return 0
	else
		return 1
	fi
}
showName $1
if [ $? = 1 ]; then
	echo "Someone unknown called the function"
fi
