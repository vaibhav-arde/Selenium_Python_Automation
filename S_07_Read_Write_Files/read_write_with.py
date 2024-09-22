import os
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# Change the working directory to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open('./Text.txt', 'r') as reader:
    content = reader.readlines()
    print(content)
    
with open('./Text.txt', 'w') as writer:
    for line in reversed(content):
        line = line.split('\n')[0]
        writer.write(line + '\n')