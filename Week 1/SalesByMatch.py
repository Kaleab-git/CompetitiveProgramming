#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockNumPair = {} #sockType-Number pair
    sockType = []  #to keep count of types of socks
    pairs = 0
    #count type of colors
    print ('ar: ', ar)
    for i in ar:
        if i not in sockType: 
            sockType.append(i)
    print ('sockType:', sockType)
    #count number of each color and store in a sockType-number pair format
    for i in sockType:
        sockNumPair[i] = ar.count(i)
    print ('sockNumPair:',sockNumPair)
    #count pairs
    for sock in sockNumPair:
        pairs += sockNumPair[sock]//2
    return pairs
            
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
