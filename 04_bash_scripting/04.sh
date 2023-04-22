#!/bin/bash
# Case statements

case ${1,,} in
	hereliesadvaith | admin)
		echo "Hi chief welcome home"
		;;
	help)
		echo "Enter your username"
		;;
	# else symbol	
	*)
		echo "Who the hell are you ?"
esac
