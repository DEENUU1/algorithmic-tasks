#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    data = {}
    pair_count = 0

    for i in range(n):
        if ar[i] not in data:
            data[ar[i]] = 1
        else:
            if data[ar[i]] == 1:
                pair_count += 1
                data[ar[i]] = 0
            else:
                data[ar[i]] += 1

    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
