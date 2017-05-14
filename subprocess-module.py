#! /bin/python3

import subprocess

subprocess.call('ls', shell=True)

subprocess.call('ping 4.2.2.2', shell=True)

output = subprocess.check_output('tracert -d 4.2.2.2', shell=True)
print (output)

subprocess.call('./os_module.py', shell=True)
