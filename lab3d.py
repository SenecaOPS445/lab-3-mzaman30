#!/usr/bin/env python3
'''Lab 3 Part 2 - functions with system commands'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    # Run the df command to get disk space for root only
    p = subprocess.Popen('df -h | grep " /$" | awk \'{print $4}\'', 
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    
    # Capture and return the free space
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    # Print the free space
    print(free_space())
