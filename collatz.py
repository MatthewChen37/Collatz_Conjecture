# -*- coding: utf-8 -*-

import random 


n = random.randrange(0, 10^3, 1)
counter = 0;

def collatz_function(n):
    
    if(n % 2 == 0):
        n = n/2
    else:
        n = (3 * n + 1)
    return n


print(n)

while(n != 1):
    n = collatz_function(n)
    print(n)
    counter += 1

