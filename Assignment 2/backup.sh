#!/bin/bash

arguments=$#

fileList=$1
backupDirectory=$2

if [ $arguments -lt 2 ]
then 
    echo "Error : Two arguments required"
    exit
elif [ $arguments -gt 2 ]
then
    echo "Error : Arguments can't be greater than 2"
    exit
fi

if [ ! -f "$fileList" ]
then
	echo "File not found"
    exit
fi

if [ ! -d "$backupDirectory" ]
then
	echo "Backup directory not found"
    exit
fi

input="$fi leList"

while read line
do 
currFile=$line

cp "$line" "${backupDirectory}"/"$line".bak
done <"$input"

echo "Succesfully backed up"