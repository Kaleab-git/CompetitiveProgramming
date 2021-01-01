#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    journeyDict = {'mountain':0, 'valley':0}
    nowClimbing = ''
    altitude = 0 
    
    for i in path:
        #Determining if what the current sub-path is: mountain or valley
        if i == 'U' and altitude == 0:
            nowClimbing = 'mountain'
        elif i == 'D' and altitude == 0:
            nowClimbing = 'valley'
        #following the path
        if i == 'U':
            altitude += 1
        else:
            altitude -= 1
        #counting finished sub-journeys:
        if altitude == 0:
            journeyDict[nowClimbing] += 1
    
    return journeyDict['valley']
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
    
    