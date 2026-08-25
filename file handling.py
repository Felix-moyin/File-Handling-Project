"""
What is a File?
A File is a named location on a computer used to store data permanently.

Unlike variables, the data inside a file remains available even after the program has been closed

Examples of file include:
students.txt
scores.csv
setting.json
report.pdf

"""

# Reading Files (The Manual Way)
# Open (filename/filepath, mode)
# if the file is not in your current working directory: open(filepath, mode)


# The open() function takes two main arguments:
# filename: The name(or path) of the file you want to open.
# mode: What you want to do with this file. They include r, w, a, x

# r = read
# w = write
# a = append
# x = create

# file = open("FUNCTION ASSI.txt", "r")
# content = file.read()
# print(content)
# file.close()
# 
# Kinds of reads(r)
# readlines()
# readline()
# read()



# Reading file from filepath

# file = open(r"C:\Users\USER\OneDrive\Pictures\student-tool.txt", "r")    # add r to avoid escape character.
# content = file.read()
# print(content)
# file.close()


# Writing to a file
# use the "w" mmode to write : open (filename/filepath, "w")
# file = open("all_files/Movielist.txt", "w")
# file.write("suits")
# file.close

# file = open("all_files/Movielist1.txt", "w")
# file.write("suits,\n Tie,\n Shoes")
# file.close


file = open("all_files/Movielist2.txt", "w")
file.write("Older,\n Contest,\n Men in Black, \nSacred ")
file.close


# file = open("File ")

# file = open(r"C:\Users\USER\OneDrive\Pictures\student-tool.txt", "w")
# file.write("I changed the existing stuff")
# file.close()



