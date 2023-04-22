#!/bin/bash
# Arrays

MY_LIST=(one two three four five)
echo $MY_LIST
# to list all
echo ${MY_LIST[@]}
# to get the second element
echo ${MY_LIST[1]}

# for loop
for item in ${MY_LIST[@]};
do echo $item;
done
