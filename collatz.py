# Simple analysis of the Collatz Conjecture

import random 
import matplotlib.pyplot as plt


n = random.randrange(0, 1000, 1)
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
    plt.plot(counter, n, 'bo');
    counter += 1
    
print("Counter: " + str(counter))



plt.ylabel('Integer value')
plt.xlabel('Iteration Number')
plt.show()


