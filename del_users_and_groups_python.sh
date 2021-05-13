#!/bin/bash

# This file is modified to work with program in Python

echo "This script removes users and groups"

read -p "To continue press any key..."; echo

logins_file_name="u_logins_temp.txt" 

# functions

function read_users {

echo; echo "You have entered: $logins_file_name."

echo; echo; cat /etc/passwd|tail	# print users list tail part

# read file's content line by line

i=0	# set counter of lines 

echo; echo "The next users are to be deleted:"

while read line; do

echo "Line No. $n : $line"

i=$((i+1))

done < $logins_file_name

}

function delete_users {

echo; read -p "To delete the users and their folders press any key..."

while read line; do

sudo userdel -r $line

i=0	# set counter of lines 

i=$((i+1))

done < $logins_file_name

cat /etc/passwd|tail # look the users list tail part

echo; echo "Defined users and their folders have(s) been deleted"

}

function delete_group {

cat /etc/group| tail			# print bottom of list of groups

echo; echo; read -p "Enter name of group to be deleted: " group_name; echo

if [[ -z $group_name ]]; then exit	# finish this programm if now group entered

fi #if [[ -n $group_name ]]; then

sudo groupdel $group_name

cat /etc/group| tail			# print bottom of list of groups

echo; echo "Group with name '$group_name' has been deleted"; echo

}

# call functions

read_users
delete_users
delete_group


