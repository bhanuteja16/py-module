#!/bin/python3

import sys

sys.stderr.write('This is stderr test\n')
sys.stderr.flush()
sys.stdout.write('this is stdout test\n')

print (sys.argv)

if len(sys.argv) > 1 :
    print (sys.argv[1])
