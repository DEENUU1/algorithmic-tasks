# optimalized solution

from math import ceil

def count_palindromes(a, b):
    def count(n):
        if n<0: return 0
        s = str(n)
        base_length = (len(s)+1)//2
        base, odd = int(s[:base_length]), len(s)&1
        if n < int((str(base)[:-1] if odd else str(base))+str(base)[::-1]):
            base -= 1
        return base + 10**(base_length-odd)
    return max(0, count(int(b)) - count(ceil(a)-1))


# my solution
# didnt passed large tests 

import math

def count_palindromes(a, b):
    a = math.ceil(a)
    b = math.floor(b)
    
    count = 0
    len_a = len(str(a))
    len_b = len(str(b))

    for digits in range(len_a, len_b + 1):
        if digits == 1:
            count += min(b, 9) - max(a, 0) + 1
        elif digits % 2 == 0:
            for prefix in range(10 ** (digits // 2 - 1), 10 ** (digits // 2)):
                num = int(str(prefix) + str(prefix)[::-1])
                if a <= num <= b:
                    count += 1
        else:
            for prefix in range(10 ** (digits // 2 - 1), 10 ** (digits // 2)):
                for middle in range(10):
                    num = int(str(prefix) + str(middle) + str(prefix)[::-1])
                    if a <= num <= b:
                        count += 1

    return count
