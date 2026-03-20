import os
# Opeining a file in Python
# file = open("/home/rahul/Documents/coding/Python/data.json","r")
# print(file.read())

# with open("/home/rahul/Documents/coding/Python/data.json","r") as fo:
#     data = fo.read()
#     print(data)
# fo.close()

# print ("Name of the file: ", fo.name)
# print ("Closed or not: ", fo.closed)
# print ("Opening mode: ", fo.mode)

# modes to open a file
''' 
r  = read mode
w =  write mode
b = binary mode
rb,wb are for read binary mode,write binary mode
a = opening in append mode
x = create a file and open in writing mode
+ = update mode
'''

############## Reading a file in Pyhton ############
'''
read() − Reads the entire file.

readline() − Reads one line at a time.

readlines − Reads all lines into a list.
'''

# with open("/home/rahul/Documents/coding/Python/data.json", "r") as file:
#    line = file.readline()
#    while line:
#       print(line, end='')
#       line = file.readline()

# print("########################### Using Read lines ############################")
# with open("/home/rahul/Documents/coding/Python/data.json", "r") as file:
#    lines = file.readlines()
#    for line in lines:
#       print(line, end='')

# ###################  Writing to a file ############
# # using a write()
# with open("/home/rahul/Documents/coding/Python/data1.txt","w") as file:
#    file.write("\n Hello Rahul")
# file.close()

# with open("/home/rahul/Documents/coding/Python/data1.txt","r") as file:
#    lines = file.readlines()
#    for line in lines:
#       print(line , end='\n')
# print(len(lines))

# # 2. using writelines to add multiple lines
liness =["Your are in first line \n","You are in second line\n","You are in Third line \n"]
with open("/home/rahul/Documents/coding/Python/data1.txt", "w") as file:
   file.writelines(liness)

with open("/home/rahul/Documents/coding/Python/data1.txt", "r") as file:
   linesss = file.readlines()
   for line in linesss:
      print(line,end='\n')
print(len(linesss))


################## using seek method ################
# seek() is used to goto specific part of line in a file or it works as pointer in file
filee = open("/home/rahul/Documents/coding/Python/data1.txt","r+")
filee.seek(1)
data11 = filee.read(1)
print(len(data11))
filee.close()
print(data11)

################# Donot use w or w+ if data already exist in file because it wipes data of file instead of it use a = append

''' Renaming file '''
#os.rename(current_name,new_name)

'''Deleting a file'''
#os.remove(file_path)

''' Creating a Directory'''
# new_dir = "New_folder"
# # os.makedirs(new_dir)

# try:
#    os.makedirs(new_dir)
#    print("New Directory created")
# except OSError as e:
#    print("can't create directory")

'''Get current working directory'''
current_dir = os.getcwd()
print(current_dir)

contents = os.listdir('/home/rahul/Documents/coding/Python')
for item in contents:
   print(item)

os.rmdir('/home/rahul/Documents/coding/Python/New_folder')

################ ALL other types of inbuilt function should be read from tutorialsPoint" Becuase the functions are too much 
