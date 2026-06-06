from subprocess import run
from random import randint

# Commands available
command_options = ['whoami', 'ip addr', 'ls /', 'id', 'pwd', 'env', 'uname',
                   'ip', 'arp -a', 'ls -l', 'ps aux', 'top', 'arp a', 'ss -tnlp', 'systemd-detect-virt']

# Size of the options available
command_length = len(command_options) - 1

# A random number
rd = randint(0, command_length)
print(command_options[13])

#Shell must be true, other than that will cause error for 2+ word commands, to solve it use it shell
# or create an array for each word like: ss -tnlp => [...['ss', '-tnlp'], ...]
run(command_options[rd], shell=True)    


