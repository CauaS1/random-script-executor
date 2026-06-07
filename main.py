import randomname, os, random
from subprocess import run

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
    
def createScriptFile(path):
    with open(f'{path}/script.py', 'w') as file:
        file.write(scriptCode)

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
            createScriptFile(mainPath)
        case 2: 
            os.makedirs(subPath)
            createScriptFile(subPath)
        case 3:
            os.makedirs(subSubPath)
            createScriptFile(subSubPath)
    i=i+1


run("find /tmp/audit_lab -type f -name 'script.py' -exec python3 {} \; ", shell=True)





    


  

 