#!/bin/bash

# Description: This script will remove the file, if it finds the word "error" in it.


read -p "Enter the path to file: " path_to_file

#if sed -n /error/p $ptf
if grep -w -o error $path_to_file
then
	rm -i -v $path_to_file
else
	echo "Error messages wasn't found. Terminate..."
fi






