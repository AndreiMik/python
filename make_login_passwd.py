# This program
# gets new user's list from file 
# creats login and password for each user
# creates new file and writes to the file user's firstname, lastname, id, login and password 
# creates temporary file with user's login's list 
# creates temporary file with user's passwords list
# sets names of temporary files to bash script
# starts bash script which adds new users to computer

import sys # we import the sys object to stop code execution in Python
import os   # we import the os object to remove temporary created files
#import subprocess  # use 'subprocess.call()'
from subprocess import call     #  use 'call()'
#import random as r # to make random part for user's password
import speech_recognition as sr

def talk(words):
   #print(words)
   os.system("say " + words)

talk("Hellow, this is a laptop computer")
talk("budu govorit po russki")
#talk("just a moment please...")
#talk("Ja nachalnik a ti durak")
talk("seitcshaas zapustim etu programmu")
#talk("tiisheee eedesh daaaalshee budesh...")

print("\nThis program adds new users to computer\n")
talk("This program adds new users to computer")
talk("Press any kay to continue...")

input() # just to make pause

def get_users(): # function creates new user's array using file's content 

    global _file_name   # we create this variable as global 
    
    print ("Enter text file name with new users list:\n")
    talk("Enter text file name with new users list:")
    talk("press letter u")
    talk("nazmi  u")

    _file_name = input()    # we try to get name of file

    if len(_file_name) == 0:    # we check if something have been entered

        print("You have entered nothing!\n")
        talk("You have entered nothing!")
        talk("I am sorry")
        talk("by by")

        sys.exit() # we stop code execution and go out of program
    
    _txt = ".txt"   # we set to variable  end part to concatenate to file name if necessary

    if _file_name[-4: ] != _txt:    # we check if we need to concatenate end part to file name
       
        _file_name = _file_name + _txt  # we concatenate end part to file name

        #print("last 4 marks: ", _file_name)    #debug

    try:    # we check if file with the entered name is possible open
       
        _this_file = open(_file_name, "rt") # we try to set to variale content of file               

    except FileNotFoundError:   

        print(_file_name, "- file is not found")
        talk("Sorry, file is not found")
        talk("by by")

        sys.exit() # we stop code execution and go out of program       

    # We continue if everything is okey with the file   
     
    global _users_array #   we create global array

    _users_array = []   # this global array of users  would consist of arrays of user's data per line

    i = 0   # we set counter for lines in the file

    for user in _this_file:         

        if i != 0:  # if current line is not  line with heads

            user = user.strip() # we remove whitespeces just to remove "\n" symbols from end of lines in going _user_arr array

            _user_arr = user.split(" ") # we create array of data for each user

            #print(_user_arr)   # debug

            _users_array.append(_user_arr)   # we append user data array as a line to array of users 
        
        i += 1

    if len(_users_array) == 0:  # we check if array of new users is not empty

        print("No users in " , _file_name)
        talk("No users in " , _file_name)

        exit    # we go out from this program

    _this_file.close() # we close the file

    print("\nThis is content of the file", _file_name, ":\n")
    talk("This is content of the file")       

    _this_file = open(_file_name, "r") # we open the file to read it

    print(_this_file.read())    # we read the file in terminal
   
    _this_file.close()  # we close the file

    talk("press any kay to continue")

    input() # we make pause    

def login_password_create(): #  function creates and appends login and password to each user's array at "_users_array" array

    i = 0 # we set counter for lines and for user's arrays in array of new users

    for user in _users_array:   # we use global array

        _firstname = user[0]    # we set user's first name to variable

        _lastname = user[1]     # we set user's last name to variable

        _idnumber = user[2]   # we set user's id number to variable

        _password_for_user = "user1a3Z_"

        _firstname = _firstname[ :3]    # we leave at "first name" only 3 first symbols

        _lastname = _lastname[ :3]  # we leave at "last name" only 3 first symbols

        _idnumber = _idnumber[-4 : ]  # we leave at "id number" only 2 first symbols

        _login_for_user = _firstname + _lastname  # we make user's login by concatination of modified user's first- and lastname    

        _password_for_user = _password_for_user + _idnumber # we make user's password by concatination of constant and user's id number

        user.append(_login_for_user)    # we add login to each user's array at "_users_array" array

        user.append(_password_for_user) # we add password to each user's array at "_users_array" array

def create_file_with_users():  # function creates file and writes to it list of users with their login and password    
       
    _new_file_name = _file_name # we get name of file from global variable

    _new_file_name = _new_file_name[ :-4]   # we temporarly remove from file name ".txt"

    _new_file_name = _new_file_name + "_modified"    # we append to file name part with name of "_modified"

    _new_file_name = _new_file_name + ".txt"    # we append back to file name part ".txt"    

    _this_new_file = open(_new_file_name, "w")  # we create new file or rewrite an old one at present directory

    _this_new_file.write("Firsname Lastname Personal_ID Login Password")    # we write to created file head string    

    _this_new_file.write("\n----------------------------------------------")    # we set to new line such strips to decor

    for line in _users_array:   # we use global array

        _string = " "   # we define string variable to keep user's data
        
        _word_counter = 0   # we set counter of words in each string

        _this_new_file.write("\n\n")    # we set new line and empty line above each line with user's data

        while _word_counter < len(line):    # for each word in line

            _string = line[_word_counter]   # we set variable as the next word in current line

            _string = _string + " " # we add space after word

            _this_new_file.write(_string)   # we write word with space after it to the file's line
            
            _word_counter += 1     

    _this_new_file.write("\n----------------------------------------------")    # we make dekor line under last string

    _this_new_file.close()  # we close the file

    _this_new_file = open(_new_file_name, "r") # we open the file to read it

    print("\nThis is content of created file", _new_file_name, ":\n")
    talk("This is content of created file")    

def create_file_with_logins(): # function

    print(_this_new_file.read())    # we read the file in terminal
   
    _this_new_file.close()  # we close the file

    input() # we make pause    

def create_file_with_logins(): # function creates temporary file and writes in it user's logins

    global _logins_file_name  # we create this variable as global

    _logins_file_name = _file_name # we get name of file from global variable

    _logins_file_name = _logins_file_name[ :-4]   # we temporarly remove from file name ".txt"

    _logins_file_name = _logins_file_name + "_logins_temp"    # we append to file name part with name of "_modified"

    _logins_file_name = _logins_file_name + ".txt"    # we append back to file name part ".txt"    
    
    _this_logins_file = open(_logins_file_name, "w")  # we create new file or rewrite an old one at present directory

    print("\n", _logins_file_name, " - file has been created...\n")

    _string = " "   # we define string variable to keep user's login

    for line in _users_array:   # we use global array

        _string = line[3]   # we set login to variable

        _this_logins_file.write(_string)    # we add variable to the file

        _this_logins_file.write("\n")   # we make new line

    _this_logins_file.close()  # we close the file

    print("Login(s) have(s) been added to", _logins_file_name, "\n")
    talk("Logins have been added ") 
    talk("press any key to make passwords")   

    _this_logins_file = open(_logins_file_name, "r")    # we open the file to read

    print(_this_logins_file.read())    # we read the file in terminal

    input() # we make pause

    _this_logins_file.close()   # we close the file

def create_file_with_passwords(): # function creates temporary file and writes in it user's passwords

    global _passwords_file_name    # we create this variable as global
    
    _passwords_file_name = _file_name # we get name of file from global variable

    _passwords_file_name = _passwords_file_name[ :-4]   # we temporarly remove from file name ".txt"

    _passwords_file_name = _passwords_file_name + "_passwords_temp"    # we append to file name part with name of "_modified"

    _passwords_file_name = _passwords_file_name + ".txt"    # we append back to file name part ".txt"    
    
    _this_passwords_file = open(_passwords_file_name, "w")  # we create new file or rewrite an old one at present directory

    print("\n", _passwords_file_name, " - file has been created...\n")
    talk("file with passwords has been created")

    _string = " "   # we define string variable to keep user's password

    for line in _users_array:   # we use global array

        _string = line[4]   # we set password to variable

        _this_passwords_file.write(_string)    # we add variable to the file

        _this_passwords_file.write("\n")   # we make new line

    _this_passwords_file.close()  # we close the file

    print("Password(s) have(s) been added to", _passwords_file_name, "\n")
    talk("Passwords have been added")
    talk("press any kay to continue")

    _this_passwords_file = open(_passwords_file_name, "r") # we open the file to read

    print(_this_passwords_file.read())    # we read the file to terminal

    input() # we make pause for reading of text

    _this_passwords_file.close()

def search_replace():   # function changes in the script defined strings with names of files where there are logins and passwords

    _bash_script_name = "/home/work/Documents/koulut/python/add_users_python.sh"    # script to open

    _logins_string_to_find = "#logins_file_name" # string we search for 

    _logins_string_to_set = "logins_file_name=" + _logins_file_name      # string to set 

    _passwords_string_to_find = "#passwords_file_name"  # string we search for 

    _passwords_string_to_set =  "passwords_file_name=" + _passwords_file_name    # string to set

    _this_bash_script_read = open(_bash_script_name, "rt")    # 'read' variable 

    ''' #This code's part no need to use, but it works with "replace" function    

    _this_bash_script_store = _this_bash_script_read.read()     # keep contents of the file 

    _this_bash_script_store = _this_bash_script_store.replace(_logins_string_to_find, _logins_string_to_set)  

    _this_bash_script_store = _this_bash_script_store.replace(_passwords_string_to_find, _passwords_string_to_set)

    _this_bash_script_read.close()      # close file after getting its content 

    _this_bash_script_write = open(_bash_script_name, "wt")    # 'write' variable  

    _this_bash_script_write.write(_this_bash_script_store)

    _this_bash_script_write.close()

    print("Variables with logins and passwords have been set to the script..")    

   input()

'''

     # logins and passwords files path setting into the list

    _strings_exist = 0    # create variable as flag for search in list

    _list_of_lines = []    # to this list we write file's content

    _logins_found_counter = 0  # count found 'logins' 

    _passwords_found_counter = 0   # count found 'passwords'
   
    for line in _this_bash_script_read:  

        _list_of_lines.append(line)    # we create a list and add line by line file's content to it

        if _logins_string_to_find in line:

            _logins_found_counter += 1     # we count found 'logins'  

        if _passwords_string_to_find in line:

            _passwords_found_counter += 1   # we count found 'passwords'                      
            
            #sys.exit() # we stop code execution and go out of program    
            
    if _logins_found_counter > 0 and _passwords_found_counter > 0:

        _strings_exist = 1  #  found both 'logins' and 'passwords' strings that we have been looking for in the script
                           

    _this_bash_script_read.close()      # close file after getting its content 

    print(_logins_found_counter,"string(s) with 'logins' and", _passwords_found_counter, "string(s) with 'passwords' are found")   

    if _strings_exist == 1:     # in created list we replace the string to another one that we need

        # looking for in the list and replacing string with 'logins'

        for i, element in enumerate(_list_of_lines):

            if element == '#logins_file_name\n':

                _list_of_lines[i] = "logins_file_name=u_logins_temp.txt\n"

                break    # we replace only the first string from the found ones  

        # looking for in the list and replacing string with 'passwords'

        for i, element in enumerate(_list_of_lines):

            if element == '#passwords_file_name\n':

                _list_of_lines[i] = "passwords_file_name=u_passwords_temp.txt\n"

                break    # we replace only the first string from the found ones  

        print("\n'logins' and 'passwords' file pathes have been set to the script\n")
        talk("logins and passwords file pathes have been set to the script")
        talk("press any key to run the script")

        input() # pause to read message        

        listToStr = ''.join([str(elem) for elem in _list_of_lines]) # changing list to string

        _file_to_write = open("add_users_python_temp.sh", "w")   # we create or reload a temp bash script which would be started tu run

        _file_to_write.write(listToStr)     # writing changed content to temp script

        _file_to_write.close()          
  
    #sys.exit() # we stop code execution and go out of program
    
def run_bash_script():  # function runs bash script which adds new users to computer

    talk("now I try to run the script")   

    _path_to_script = os.getcwd() + "/temp_add_users_python.sh" # we get path to script and set it to variable

    os.chmod(_path_to_script, 0o755) # we set rights to run the script

    rc = call(_path_to_script) # we start script to run   

def delete_temporary_file():   # function removes temporary file with user's passwords

    os.remove(_passwords_file_name)    # we remove file with user's passwords

    print("\nFile '",_passwords_file_name,"' has been removed\n")

get_users() # we call function

login_password_create() # we call function

create_file_with_users()   # we call function

create_file_with_logins() # we call function

create_file_with_passwords()  # we call function

search_replace()

run_bash_script()
talk("thank you")
talk("kiitos")
talk("spasibo")

#delete_temporary_file()    # we do not call function because to use created files