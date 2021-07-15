# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:59:43 2021

@author: matthew maynes
"""

import numpy as np

struct_hms = open('struct_hms.inc.text')
struct_shms = open('struct_shms.inc.text')
spectrometer = open('spectrometers.inc.txt')
constrants = open('constrants.inc.txt')


SHMS = {'shmsSTOP_trials':0,'shmsSTOP_targ_hor':0,'shmsSTOP_targ_vert':0,
        'shmsSTOP_targ_oct':0,'shmsSTOP_FRONTSLIT_hor':0,'shmsSTOP_FRONTSLIT_vert':0,
	    'shmsSTOP_HB_in':0,'shmsSTOP_HB_men':0,'shmsSTOP_HB_mex':0,
	    'shmsSTOP_HB_out':0,'shmsSTOP_DOWNSLIT':0,'shmsSTOP_COLL_hor':0,
	    'shmsSTOP_COLL_vert':0,'shmsSTOP_COLL_oct':0,'shmsSTOP_Q1_in':0,
	    'shmsSTOP_Q1_men':0,'shmsSTOP_Q1_mid':0,'shmsSTOP_Q1_mex':0,'shmsSTOP_Q1_out':0,
	    'shmsSTOP_Q2_in':0,'shmsSTOP_Q2_men':0,'shmsSTOP_Q2_mid':0,'shmsSTOP_Q2_mex':0,
	    'shmsSTOP_Q2_out':0,'shmsSTOP_Q3_in':0,'shmsSTOP_Q3_men':0,'shmsSTOP_Q3_mid':0,
	    'shmsSTOP_Q3_mex':0,'shmsSTOP_Q3_out':0,'shmsSTOP_Q3_out1':0,'shmsSTOP_Q3_out2':0,
	    'shmsSTOP_Q3_out3':0,'shmsSTOP_Q3_out4':0,'shmsSTOP_Q3_out5':0,
	    'shmsSTOP_Q3_out6':0,'shmsSTOP_D1_in':0,'shmsSTOP_D1_flr':0,
	    'shmsSTOP_D1_men':0,'shmsSTOP_D1_mid1':0,'shmsSTOP_D1_mid2':0,
	    'shmsSTOP_D1_mid3':0,'shmsSTOP_D1_mid4':0,'shmsSTOP_D1_mid5':0,
	    'shmsSTOP_D1_mid6':0,'shmsSTOP_D1_mid7':0,'shmsSTOP_D1_mex':0,
	    'shmsSTOP_D1_out':0,'shmsSTOP_BP_in':0,'shmsSTOP_BP_out':0,'shmsSTOP_hut':0,
	    'shmsSTOP_dc1':0,'shmsSTOP_dc2':0,'shmsSTOP_s1':0,'shmsSTOP_s2':0,
	    'shmsSTOP_s3':0,'shmsSTOP_cal':0,'shmsSTOP_successes':0,'shmsSTOP_id':0}

HMS = {'hSTOP_trials':0,'hSTOP_fAper_hor':0,'hSTOP_fAper_vert':0,'hSTOP_fAper_oct':0,
	   'hSTOP_bAper_hor':0,'hSTOP_bAper_vert':0,'hSTOP_bAper_oct':0,'hSTOP_slit':0,
	   'hSTOP_Q1_in':0,'hSTOP_Q1_mid':0,'hSTOP_Q1_out':0,'hSTOP_Q2_in':0,
	   'hSTOP_Q2_mid':0,'hSTOP_Q2_out':0,'hSTOP_Q3_in':0,'hSTOP_Q3_mid':0,
	   'hSTOP_Q3_out':0,'hSTOP_D1_in':0,'hSTOP_D1_out':0,'hSTOP_VP1':0,
	   'hSTOP_VP2':0,'hSTOP_VP3':0,'hSTOP_VP4':0,'hSTOP_hut':0,'hSTOP_dc1':0,
	   'hSTOP_dc2':0,'hSTOP_scin':0,'hSTOP_cal':0,'hSTOP_successes':0,'hSTOP_id':0}



input_file = input('Enter input filename (assumed to be in infiles dir :')
if input_file == 'hut_ntuple':
    hbook_filename = input_file + '.rzdat'
else:
    filename = input_file + '.inp'
    print(filename, " is opened")





"Name of the file you wish to analize"
data = "shms-20,17-26cm-monte_quads_p18_forward.txt" #this is your file


"Process of checking if the matrices are clean and if not then it will clean them"
my_file = open(data, "r")
string_list = my_file.readlines()
l = len(string_list)

new_strings = []
new_new_strings = []


"""
The actual loop that checks if the matrix numbers run into eachother
The loop will add space between numbers of the matrix if it come true
"""
if "0-" or "1-" or "2-" or "3-" or "4-" or "5-" or "6-" or "7-" or "8-" or "9-" in string_list:
    for string in string_list:
        newstring = string.replace('-0.',' -0.')
        new_strings.append(newstring)
    my_file = open(data, 'w')
    new_file_contents = "".join(new_strings)
    my_file.write(new_file_contents)
    my_file.close()

"Initilizing the increment variable and array names for matrix"
n = 0
b = 0


"This finds how many matrixes are in the file"
with open(data, "r") as f:
    for i, dash in enumerate(f):
        dash = dash.strip()
        if "-------------" in dash:
            b += 1
Matrix = []

for i in range (0,b):
    M_i = []
for i in range (0,b):
    Matrix.append(M_i)


"Creates a list of arrays so that they can be called upon during the loop"

names = []
regions = []
offsets = []
lengths = []

"""
 This loop uses the dashed line to know when a new matrix has started and
 increments at that point to keep count of how many matrixes there are and which
 one they are currently at. It also checks to see what the line starts with to 
 create an array of all the names, regions, offsets, and lengths. Lastly if fills
 the array with the matrix that is associated with the other values
"""
with open(data, "r") as d:
    for i, line in enumerate(d):
        line = line.strip()
        if "-------------" in line:
            n += 1  
        elif line.startswith('!N'):
            names.append(line[7:])
        elif line.startswith('!R'):
            regions.append(line[9:])
        elif line.startswith('!O'):
            offsets.append(line[13:])
        elif line.startswith('!L'):
            lengths.append(line[13:])

        else:
            Matrix[n].append(list(line.split()))
print("")

"""
This following portion takes all the matrix list and turns them into arrays. It
then turns those arrays of strings to arrays of float numbers.
"""

for i in range(0,b):
    Matrix[i] = [list(map(float, sublist)) for sublist in Matrix[i]]
for i in range(0,b):
    Matrix[i] = np.array(Matrix[i])

"""
This next portion allows the user to type in the name of the matrix they wish to see.
"""

print("Here are the names of the different Matrices")
print(names)
print("")
print("")
input_name = input("Type full name of matrix you wish to see :")

for i in range(0,b):
    if input_name in names[i]:
        print("Name: ", names[i])
        print("Region: ", regions[i])
        print("Offset: ", offsets[i])
        print("length :", lengths[i])
        print(Matrix[i])

mul = np.dot(Matrix[0], Matrix[1])
print("Matrix 0 and Matrix 1 multiplied together")
print("")
print(mul)

"""
m2 = me2
if p_flag == 0:
    m2 = me2
elif p_flag == 1:
    m2 = mp2
elif p_flag == 2:
    m2 = md2
elif p_flag == 3:
    m2 = mpi2
elif p_flag == 4:
    m2 = mk2
"""

