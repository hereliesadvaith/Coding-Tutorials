#!/bin/bash
# functions

showupTime(){
	# making it a local variable
	local up=$(uptime -p | cut -c4-)
	local since=$(uptime -s)
	cat << EOF
-----------
Hello $1
This machine has been up for ${up}
It has been running since ${since}
-----------
EOF
# functions can also take positional arguments
}
showupTime Advaith
