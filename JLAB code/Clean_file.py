# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:23:06 2021

@author: mayne
"""
d = "shms-2017-26cm-monte_q1_1018_q2_1027_q3_1018_forward.dat.txt"
my_file = open(d, "r")
string_list = my_file.readlines()
l = len(string_list)

new_strings = []
new_new_strings = []
for string in string_list:
        newstring = string.replace('-0.','  -0.')
        new_strings.append(newstring)
"""
for newstring in new_strings:
    newnewstring = newstring.replace('0 ', '0 ,')
    newnewstring = newstring.replace('1 ', '1 ,')
    newnewstring = newstring.replace('2 ', '2 ,')
    newnewstring = newstring.replace('3 ', '3 ,')
    newnewstring = newstring.replace('4 ', '4 ,')
    newnewstring = newstring.replace('5 ', '5 ,')
    newnewstring = newstring.replace('6 ', '6 ,')
    newnewstring = newstring.replace('7 ', '7 ,')
    newnewstring = newstring.replace('8 ', '8 ,')
    newnewstring = newstring.replace('9 ', '9 ,')
    new_new_strings.append(newnewstring)
"""
"""print(new_strings)"""

my_file = open(d, 'w')
new_file_contents = "".join(new_strings)
my_file.write(new_file_contents)
my_file.close()

readable_file = open(d)
read_file = readable_file.read()
print(read_file)
