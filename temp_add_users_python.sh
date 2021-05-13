#!/bin/bash

echo
echo
echo "This is an 'add_users' script "
echo "It adds new users, and sets  their passwords, and"
echo "it can create new group and add users to that group."
echo
read -p "To continue press any key..."
echo
echo

# variables

number_of_users_in_file=0		# number of users in file

p_new=0			# number of new users added to System

group_name=""		# name of entered user's group

length_of_new_users=0	# number of lines in NEW_USERS array

logins_file_name=u_logins_temp.txt

passwords_file_name=u_passwords_temp.txt

#logins_file_name=u_logins_temp.txt

#passwords_file_name=u_passwords_temp.txt

# functions

function read_logins {

echo "You have entered: $logins_file_name. The next users are to be added by logins:"

i=0	# set file line's counter to null

while read line; do

NEW_USERS[i]=$line		# add to array all users from file

echo "Line No. $n : $line"	# print line by line that file's content

i=$((i+1))			# counting lines in the file

done < $logins_file_name		#while read line; do

number_of_users_in_file=$i		# set number of users in file to variable

}

function add_users {

echo; read -p "To add $number_of_users_in_file user(s) and create user's folders press any key..."

# check if user already exists and than adding new users

i=0	# line counter for new user's array

new_users_counter=0	# set people's counter for new user's array

j=0	# line counter for exist user's array

exist_users_counter=0 # user's counter for exist user's array

length_of_new_users=${#NEW_USERS[@]}	# check for how many lines are in the file 

# echo "length_of_new_users= $length_of_new_users"	# for debug

while [ $i -lt $length_of_new_users ]; do

new_users_counter=$[ new_users_counter+1 ]	# people's count for new user's array

if [[ -n ${NEW_USERS[i]} ]] && id ${NEW_USERS[i]} >/dev/null 2>&1; then		# checking if user already exists. This code I need to study with

EXIST_USERS[j]=${NEW_USERS[i]}	# create new array and add to it just found already exist users 

j=$[ j+1 ]	# line count for exist user's array

exist_users_counter=$[ exist_users_counter+1 ]	# people's count for exist user's array

unset NEW_USERS[i]	# remove exist user from new user's array

new_users_counter=$[ new_users_counter-1 ]	# subtract user from new user's count

else

sudo useradd -m ${NEW_USERS[i]}	# add to System new user and create folders for it

fi	#if [[ -n ${NEW_USERS[i]} ]] && id {$NEW_USERS[i]} >/dev/null 2>&1; then	

i=$[ i+1 ]		# line counter for new user's array

done 	#while [ $i -lt $length_of_new_users ]

cat /etc/passwd|tail		# print bottom part of user's list

if (( ${#EXIST_USERS[@]} )); then	# check if array of exist users has been created

echo; echo "Attention! $p_exist user(s)  ${EXIST_USERS[*]} already exist(s)!" # print users that are already exist

fi	# if (( ${#EXIST_USERS[@]} )); then

if (( ${#NEW_USERS[@]} )); then		# check if new user's array is still not empty because of removing from that exist users

echo; echo "$new_users_counter user(s) ${NEW_USERS[*]} are added"	# print users that are added to System

else

echo; read -p "No users to add..."

exit	# finish this programm if now users to add

fi	# if (( ${#NEW_USERS[@]} )); then

}

function set_passwords {

echo; read -p "To set password for each $new_users_counter added user(s) press any key..."

# we set passwords from the file to array

i=0	# set file line's counter to null

echo
echo "Users and their passwords to be set..."
echo

while read line; do

PASSWORDS[i]=$line		# add to array all passwords from file

echo ${NEW_USERS[i]} ": " ${PASSWORDS[i]}
echo

i=$((i+1))			# counting lines in the file

done < $passwords_file_name		#while read line; do

# creating user's passwords at computer

i=0	# set counter of lines of new users array

i_add_users=0	# set counter of added to System users

while [ $i -lt $length_of_new_users ]; do

if [[ -n ${NEW_USERS[i]} ]]; then	# check if current string length is grater than zero

echo ${NEW_USERS[i]}:${PASSWORDS[i]} | sudo chpasswd	# set to each user the same password

i_add_users=$[ i_add_users+1 ]	# count added to System users

fi	#if [[ -n ${NEW_USERS[i]} ]]; then

i=$[ i+1 ]	# count lines  of array

done 	#while [ $i -lt $length_of_new_users ]; do

echo; read -p "Passwords for $i_add_users user(s) have been set"

}

function create_group {

echo; read -p "To choose group or create new group, please enter group name: " group_name		# get entered group name

if [[ -z $group_name ]]; then exit 1	# finish this programm if now group entered

fi #if [[ -n $group_name ]]; then

if grep -q $group_name /etc/group; then		# check if this group alraedy exists

cat /etc/group| tail				# print bottom of list of groups

echo "Group with name '$group_name' already exists."; else	

sudo groupadd $group_name		# if group does not exist add it to System

cat /etc/group| tail			# print bottom of list of groups
    	
echo; echo "Group with name '$group_name' has been created."
        
fi	#grep -q $group /etc/$group_name

}

function add_users_to_group {

echo; read -p "To add users to group '$group_name' press any key..."

i=0 	# set array line's counter

i_users_to_group=0	# set counter of users added to group

while [ $i -lt $length_of_new_users ]; do

if [[ -n ${NEW_USERS[i]} ]]; then	# check if current string length is grater than zero

sudo usermod -aG $group_name ${NEW_USERS[i]}

cat /etc/group| tail

i_users_to_group=$[ i_users_to_group+1 ]	# count added to group users

fi	#if [[ -n ${NEW_USERS[i]} ]]; then

i=$[ i+1 ]	# count lines  of array

done 	#while [ $i -lt $length_of_new_users ]; do

echo; echo "$i_users_to_group user(s) have(s) been set to group '$group_name'"; echo

}

# call functions

read_logins
add_users
set_passwords
create_group
add_users_to_group






