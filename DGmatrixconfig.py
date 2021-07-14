import numpy as np
###############################

"This is Matthew Maynes' Matrix configuration for JLab's github's .txt matrix to python array "

###############################


"Name of the file you wish to analize"
data = r"shms-2017-26cm-monte_q1_1018_q2_1027_q3_1018_hb80_forward.dat.txt" #this is your file


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
        newstring = string.replace('-0.','  -0.')
        new_strings.append(newstring)
    my_file = open(data, 'w')
    new_file_contents = "".join(new_strings)
    my_file.write(new_file_contents)
    my_file.close()

"Initilizing the increment variable and array names for matrix"
n = 0
b = 0

M_0 = []
M_1 = []
M_2 = []
M_3 = []
M_4 = []
M_5 = []
M_6 = []
M_7 = []
M_8 = []
M_9 = []
M_10 = []
M_11 = []
M_12 = []
M_13 = []
M_14 = []
M_15 = []
M_16 = []
M_17 = []
M_18 = []
M_19 = []
M_20 = []
M_21 = []
M_22 = []
M_23 = []
M_24 = []
M_25 = []
M_26 = []
M_27 = []
M_28 = []
M_29 = []
M_30 = []
M_31 = []
M_32 = []

"This finds how many matrixes are in the file"
with open(data, "r") as f:
    for i, dash in enumerate(f):
        dash = dash.strip()
        if "-------------" in dash:
            b += 1
            
"This is some failed code that I didn't want to delete"
"""
for i in range (0,b):
    M_i = []
for i in range (0,b):
    Matrix.append(M_i)
for i in range (0,b):
    Ms['M_{0}'.format(i)] = []
for x in range(0, b):
    globals()['M_%s' % x] = []
for i in range (0,b):
    Matrix.append("M_{0}".format(i))
for i in range (0, b):
    Ms.append(Matrix[i].strip('""'))
print(Ms)
"""

"Creates a list of arrays so that they can be called upon during the loop"
Matrix = (M_0, M_1, M_2, M_3, M_4, M_5, M_6, M_7, M_8, M_9, M_10, M_11, M_12, M_13,
          M_14, M_15, M_16, M_17, M_18, M_19, M_20, M_21, M_22, M_23, M_24,
          M_25, M_26, M_27, M_28, M_29, M_30, M_31, M_32)
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
M_0 = np.array(M_0)
M_1 = np.array(M_1)
M_2 = np.array(M_2)
M_3 = np.array(M_3)
M_4 = np.array(M_4)
M_5 = np.array(M_5)
M_6 = np.array(M_6)
M_7 = np.array(M_7)
M_8 = np.array(M_8)
M_9 = np.array(M_9)
M_10 = np.array(M_10)
M_11 = np.array(M_11)
M_12 = np.array(M_12)
M_13 = np.array(M_13)
M_14 = np.array(M_14)
M_15 = np.array(M_15)
M_16 = np.array(M_16)
M_17 = np.array(M_17)
M_18 = np.array(M_18)
M_19 = np.array(M_19)
M_20 = np.array(M_20)
M_21 = np.array(M_21)
M_22 = np.array(M_22)
M_23 = np.array(M_23)
M_24 = np.array(M_24)
M_25 = np.array(M_25)
M_26 = np.array(M_26)
M_27 = np.array(M_27)
M_28 = np.array(M_28)
M_29 = np.array(M_29)
M_30 = np.array(M_30)
M_31 = np.array(M_31)
M_32 = np.array(M_32)

M_0 = M_0.astype(float)
M_1 =  M_1.astype(float)
M_2 =  M_2.astype(float)
M_3 =  M_3.astype(float)
M_4 =  M_4.astype(float)
M_5 =  M_5.astype(float)
M_6 =  M_6.astype(float)
M_7 =  M_7.astype(float)
M_8 =  M_8.astype(float)
M_9 =  M_9.astype(float)
M_10 =  M_10.astype(float)
M_11 =  M_11.astype(float)
M_12 =  M_12.astype(float)
M_13 =  M_13.astype(float)
M_14 =  M_14.astype(float)
M_15 =  M_15.astype(float)
M_16 =  M_16.astype(float)
M_17 =  M_17.astype(float)
M_18 =  M_18.astype(float)
M_19 =  M_19.astype(float)
M_20 =  M_20.astype(float)
M_21 =  M_21.astype(float)
M_22 =  M_22.astype(float)
M_23 =  M_23.astype(float)
M_24 =  M_24.astype(float)
M_25 =  M_25.astype(float)
M_26 =  M_26.astype(float)
M_27 =  M_27.astype(float)
M_28 =  M_28.astype(float)
M_29 =  M_29.astype(float)
M_30 =  M_30.astype(float)
M_31 =  M_31.astype(float)
M_32 =  M_32.astype(float)

Matrix = (M_0, M_1, M_2, M_3, M_4, M_5, M_6, M_7, M_8, M_9, M_10, M_11, M_12, M_13,
          M_14, M_15, M_16, M_17, M_18, M_19, M_20, M_21, M_22, M_23, M_24,
          M_25, M_26, M_27, M_28, M_29, M_30, M_31, M_32)

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