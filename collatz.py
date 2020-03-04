# Simple analysis of the Collatz Conjecture

import random 
import matplotlib.pyplot as plt



def collatz_function(n):
    
    if(n % 2 == 0):
        n = n/2
    else:
        n = (3 * n + 1)
    return n

def collatz_several():
    n = random.randrange(1, 1000, 1)
    org = n
    print(n)
    counter = 0
    plt.figure(1)
    while(n != 1):
        n = collatz_function(n)
        print(n)
        plt.plot(counter, n, 'bo');
        counter += 1
    print("Counter: " + str(counter))
    plt.figure(2)
    plt.plot(counter, org, 'bo');


for i in range(100):
    collatz_several()


plt.figure(1)
plt.title('Value of numbers for 100 random values between 0 and 1000')
plt.ylabel('Integer value')
plt.xlabel('Iteration Number')


plt.figure(2)
plt.title('Correspondence of original value to total iteration')
plt.ylabel('Original Value')
plt.xlabel('Total Iterations: ')

plt.show()




