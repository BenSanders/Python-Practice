# Exam Review 2023 June 17
import math

# Do those LABS
# CH 2-14...  ALL labs
# Ch 25-32 just ADDITIONS LABS, but imporant practice!
# Prac tests. Ch 33 and 34
# Use submit mode and get them to 100%!!! And PAY ATTENTION to the unit tests!

# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Comp 2: Control Flow
# Comp 3: Modules and Files

# Watch your string input and output
# Input...
# myInput = input().strip()
# output/print()
# print() # same as print(end="\n")
# print("Something I'm printing.", end=" ") # if we override end...
# # we gotta put the exepcted \n back
# print()
# print("Clean new line!")

# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Comon Data Types
# int
# float
# bool # True, False... print(x > 5)
# str # ""
# list # [ ]
# dict # {key: value}
# set # { } all unique values/no duplicates, no order... no indices, no sorting, no slicing
# tuples # ( ) immutable (think databases), Python sees any x,y,z as (x,y,z) --> return x, b --> return (a,b)
# range object # range()... range(0,5) --> [0, 1, 2, 3, 4]

# Operators
# = # Assignment
# == # Equality... ASKING if these are equal
# +
# -
# *
# /
# % # Modulo... gives an int remainder, "How many whole things didn't fit (since the last even division)?"
# // # Floor division the last even division
# < # less then
# > # greater then
# <= # less or equal too
# >= # greater then or equal to
# += # x += 1 --> x = x + 1
# -= # x -= 1 --> x = x - 1
# ** # raise to power... pow() and math.pow()
# != # NOT
# # keywords that we use like operators
# in # if x in myList
# not # if not x in myList
# and
# or # any one True condition makes the combines condition True... limit OR to 2 conditions

# Comp 2
# Control Flow! The HOW stuff
# IF statements... if, if/else, if/elif, if/elif,else...
# LOOPS
# WHILE - an IF that repeats
# FOR - looping over a container, or a known number of times... hence range()
# # # Check out my [Jerry's] For Loops webiner in The Gotchas
# for ___ in __someContainer__:
# for item in myList:
# for char in myString:
# for keys in myDict: # myDict[key] gets the value for that key
# for key, value in myDict.items()
# for num in range(0,12):
# for i, item in enumerate(myList)
# for i in range(len(myList)): # myList[i]

# FUNCTION
# defining/writing vs calling
# a function has ONE particular job
# parameter is a special var for the function... not like a "regular" variable
#parameter vs arguments

# def someFunction(x,y):
#     return x // y
#
# if __name__ = "__main__": # is this script the one that's being run from?
#     # we're solving THIS question
#     myInput = int(input())
#     myOther = int(input())
#     myNum = someFunction(myInput,myOther)
#     print(myNum)


# See "tasks" in the last section of Ch 18, 11, 13, 14 for function writing practice
# # CodingBat also has good function-based Python questions:
# # https://codingbat.com/python

# BUILT-IN FUNCTIONS
# input()
# print()
# range()
# len()
# min()
# max()
# sum()
# enumerate()
# round() # cousins math.cell() and math.floor()
# type()
# sorted()
# reversed()
# pow() # compare to ** or math.pow()
# abs() # compare to math.fabs()
# int()
# float()
# list()
# tuple()
# set()
# dict()
# open()
# help() # help(str), help(str.isspace)
# dir() # print(dir(str))

# STRINGS
# be able to slice
#myStr = "abcdef"
# revStr = myStr[::-1]
# print(revStr)

# KNOW YOUR WHITESPACE
# " "
# a lot of spaces in Unicode
# "\n"
# "\t"
# "\r" # carriage return

# STRING METHODS
# myStr.format() # "stuff I want to put together {:2f}".format(var)
# myStr.strip()
# myStr.split() # returns a list of smaller strings
# myStr.join() # " ".join(listOfStrings)
# myStr.replace(subStr, newStr) # "remove"...myStr = myStr.replace(subStr, "")
# myStr.find(subStr) # return int index, or -1
# myStr.count(subStr) # return int number of occurrences
# case: myStr.lower(), myStr.upper(), myStr.title(), myStr.capitalize()
# is/Boolean: myStr.isupper(), .islower(), isspace(), isalpha(), isnumeric(), isdigit(), isalnum()
# myStr.startswith(subStr), myStr.endswith(subStr)

# LISTS
# be able to use indices, slice

# LIST METHODS
# +
# myList.append(item)
# myList.insert(i, item)
# myList.extend(anotherList)
# # -
# myList.pop(i) # by index, or last
# myList.remove(item) # pop by index, remove by value
# myList.clear()
# # other
# myList.count(item)
# myList.sort()
# myList.reverse()
# myList.copy()
# myList.index(item)

# DICT
# use the key like an index []
# myDict[key] # retreieve value for that key
# myDict[key] = value # assign value to key
# myDict.keys()
# myDict.values()
# myDict.items()
#
# # MODULES
# # math and csv
#
# # MATH MODULE
# import math_ # FULL IMPORT
# math.factorial(x)
# math.ceil(x.yz)
# math.floor(x.yz)
# math.pow(x,y)
# math.sqrt(x)
# math.fabs(x) # built-in abs()
# math.pi
# math.e
#
# # PARTIAL IMPORT
# from math import factorial # --> factorial(x)
# from math import ceil, sqrt_ # --> ceil(x,yz), sqrt(x)
# from math import * --> floor(x,yz)
#
# # ALIAS IMPORT
# import math as m # --> m.floor(x,yz)

# FILES
with open("test.txt","r") as f:
    # f.read() # returns entire file as one string
    # f.readline # goes one line ahead and returns that line
    contents = f.readlines() # list of strings... each line in the files is one string
print(contents)
# for line in contents:
#     line = line.strip()
#     print(line)

# CSV module
import csv
with open("mock_data.csv","r") as f1:
    contents = csv.reader(f1) # csv.reader(f1, delimiter="\t")
# print(contents)
for row in contents[0:20]:
    print(row)


# READ MODE

# WRITE MODE
with open("output_data20.csv","w") as f2:
    for row in contents:
        # only write into this new file if email ends in .edu
        # email is position 3
        if row[3].endswith(".edu"):
            # write a str to file
            f2.write()

# APPEND MODE
# with open("append_to_this.txt","r") as f3:
#    contents = f3.readlines()
# print(contents) # ['Frodo\n', 'Sam\n', 'Merry\n']
# with open("append_to_this.txt","a") as f3:
#         f3.write("Pippin\n")








