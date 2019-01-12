#!/usr/bin/env python3
import sys
#third script to print out name

#print ("My name: Femi")
#print ("My favorite color: Blue")
#my_fav_act = "Music"
#my_fav_anim = "Dog"
#print("My favorite activity is playing" , my_fav_act)
#print("My favorute animal:", my_fav_anim)

my_name = sys.argv[1] # get my name from command line
my_favorite_color = sys.argv[2] # get my favorote color from command line parameter
# now print a message to the screen
#print("My name is", my_name, "and my favorite color is", my_favorite_color) #this line of code works well or try the nest line to print
print("My name is " + my_name + " and my favorite color is " + my_favorite_color)
