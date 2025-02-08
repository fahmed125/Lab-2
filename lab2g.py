#!/usr/bin/env python3

#Author: Fuad Ahmed
#Author ID: 182853218
#Date Created: 2025/02/07

import sys

if len(sys.argv) == 2:
	Timer= int(sys.argv[1])
else:
	Timer=3
while Timer > 0:
	print(Timer)
	Timer = Timer - 1
print("blast off!")
