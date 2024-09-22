import os
print(os.getcwd())

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# Change the working directory to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = open('./Text.txt')
print("All File : ", file.read())
file.seek(0)
print("Line one: ", file.readline())
print("Line Two: ", file.readline())

print("**************")
file.seek(0)
line = file.readline()
while line!="":
    print(line)
    line = file.readline()
print("**************readlines***")
file.seek(0)
print(file.readlines())
file.seek(0)
# lines=file.readlines()
# line=lines[0].split("\n")[0]
# print(line)
# # line=line.split("\n")[1]
# # print(line)
# # line=line.split("\n")[2]
# # print(line)
# file.seek(0)
for line in list(file.readlines()):
    line=line.split("\n")[0]
    print(line)
file.close()