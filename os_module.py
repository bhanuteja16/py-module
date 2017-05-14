#!/bin/python3

import os
import time

curDir = os.getcwd()
print (curDir)
os.mkdir('newDir')
time.sleep(2)
os.rename('newDir','newDir!')
