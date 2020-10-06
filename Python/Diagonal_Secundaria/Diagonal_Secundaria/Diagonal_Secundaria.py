#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    somar1 = 0
    somar2 = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                somar1 += arr[i][j]

            if n - 1 == i + j:
                somar2 += arr[i][j]

    if somar2 > somar1:
        return somar2 - somar1
    else:
        return somar1 - somar2



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()

