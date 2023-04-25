#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 4
#April 22, 2023

print("*********************************************************")
print("READING INTEGERS (SQUARE AND CUBE)")
print("Programmed by: John Carlo Ablay")
print("*********************************************************")

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
#open a file to store all numbers in even numbers list
