# COSC440Assignment2

## RUNNING THE PROGRAM ##

-Create a new user in a linux shell
-Give this user a password that you know is in the dictionary
-Run the program using the following command:

> sudo python assignment2.py [username] [path of shadow file]

NOTE: In this github folder should be a 'dictionary.txt' file with a sample dictionary for the program to use

Errors:

-If a specified file does not exist, the program will exit with an error

Warnings:

-If the user does not exist, the program will exit with a warning

-If the user exists but does not have a password, the program exits with a warning

-If the user exists and has a password, but the password is not in the provided dictionary, the program exits with a warning
