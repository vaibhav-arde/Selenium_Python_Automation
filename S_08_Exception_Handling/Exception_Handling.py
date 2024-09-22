import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


ItemsInCart = 0
# if ItemsInCart != 2:
#     raise Exception("Products cart count not matching :(")

# assert ItemsInCart == 2, "count not matching :("
# assert(ItemsInCart == 2)

# *********************
print("**************")
try:
    with open('../S_07_Read_Write_Files/Text123.txt','r') as reader:
        print(reader.read())
    
except:
    print("File not present!!")
    
# *********************
print("**************")
try:
    with open('../S_07_Read_Write_Files/Text123.txt','r') as reader:
        print(reader.read())
    
except Exception as e:
    print(e)
    
print("**************")

try:
    with open('../S_07_Read_Write_Files/Text.txt','r') as reader:
        print(reader.read())
    
except Exception as e:
    print(e)
    
finally:
    print("Resource clean up!!")
    
print("**************")