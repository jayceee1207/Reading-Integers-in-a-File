#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 4
#April 22, 2023

import pyfiglet
import emoji
import os

print("*********************************************************")
print("\u001b[33;1m","READING INTEGERS (SQUARE AND CUBE)")
print("\u001b[33;1m","Programmed by: John Carlo Ablay")
print("\u001b[37;1m","*********************************************************")

title = pyfiglet.figlet_format("\nREADING INTEGERS (SQUARE AND CUBE)", font = "digital" )
print(title)

#PSEUDOCODE
#Make a file where we will store random numbers
file_open = open("numbers.txt", "r")
#Read every line of numbers
read_content = file_open.readlines()
#Create a list where we store all even numbers
square_even_nums = []
#Create a list where we store all odd numbers
cube_odd_nums = []
#Write a for loop for numbers in number.txt file
for number in read_content:

#   convert numbers into integer
    integer = int(number)
#   if integer is even number
    if integer % 2 == 0:
#       get the square of the even number 
        square_num = integer ** 2
#       we will append that number into the even numbers list
        square_even_nums.append(square_num)
#   if integer is odd number
    else:
#       get the cube of the odd number 
        odd_num = integer ** 3
#       we will append that number into the odd numbers list
        cube_odd_nums.append(odd_num)
#open a file to store all numbers in even numbers list
with open('square_numbers.txt', 'w') as outfile:
    word_title_even = ("\u001b[32;1m","Squared-Even-Numbers\n")
    outfile.write('\n'.join(map(str, word_title_even)))
    outfile.write('\n'.join(map(str, square_even_nums)))
    
#open a file to store all numbers in even numbers list
with open('cube_numbers.txt', 'w') as outfile:
    word_title_odd = ("\u001b[32;1m","Squared-Even-Numbers\n")
    outfile.write('\n'.join(map(str, word_title_even)))
    outfile.write('\n'.join(map(str, cube_odd_nums)))

print("\nThank you for using our program!")
print(emoji.emojize('Have a good day! :grinning_face:'))