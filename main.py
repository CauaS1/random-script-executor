import randomname, os, random

# Code that executes some linux commands | tested on script_test.py
scriptCode = """
from subprocess import run
from random import randint

command_options = ['whoami', 'ip addr', 'ls /', 'id', 'pwd', 'env', 'uname',
                   'ip', 'arp -a', 'ls -l', 'ps aux', 'top', 'arp a', 'ss -tnlp', 'systemd-detect-virt']

command_length = len(command_options) - 1

rd = randint(0, command_length)  
run(command_options[rd], shell=True)              
"""

# It checks if the main tmp path exists
pathExist = os.path.exists('/tmp/audit_lab')

# Create a temporary folder to keep our folder tree
if pathExist == False:
    os.mkdir('/tmp/audit_lab')
    

for i in range(3):
    print("voltaws")
    # Creating values with random name for the random folder creation
    getNameFunction = randomname.get_name(noun='gaming')
    mainFolder, subFolder, subSubFolder = randomname.get_name(noun='gaming'), randomname.get_name(noun='gaming'), randomname.get_name(noun='gaming')

    # Paths
    mainPath = f'/tmp/audit_lab/{mainFolder}'
    subPath = f'/tmp/audit_lab/{mainFolder}/{subFolder}'
    subSubPath = f'/tmp/audit_lab/{mainFolder}/{subFolder}/{subSubFolder}'

    folderSize = random.randint(1,3)
    match folderSize:
        case 1:
            os.mkdir(mainPath)
        case 2: 
            os.makedirs(subPath)
        case 3:
            os.makedirs(subSubPath)
    i=i+1
    print(f'The option was: {folderSize}')

    with open('./script.py', 'w') as file:
        file.write(scriptCode)



  

 