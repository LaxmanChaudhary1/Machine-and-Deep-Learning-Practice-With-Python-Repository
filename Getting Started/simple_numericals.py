#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:00:43 2023

@author: laxman
"""

print('#################################')
print('              1                   ')
print('#################################')

# Find a cube root of an integer.
x = int(input("Enter an integer:"))
ans = 0
while ans**3 < abs(x):
    ans = ans+1
if ans**3!=abs(x):
    print("x has no perfect cube root")
else:
    if x<0:
        ans = -ans
    print(f'The perfect cube root of x is {ans}')

print('#################################')
print('              2                   ')
print('#################################')

# Test if the integer given is prime. Find the smallest divisor also.
x = int(input("Enter an integer > 2:"))
smallest_divisor = None
for guess in range(2,x):
    if x%guess==0:
        smallest_divisor =  guess
        break
if smallest_divisor!=None:
    print(f'The smallest divisor of {x} is {smallest_divisor}')
else:
    print(x, 'is a prime number.')

print('#################################')
print('              3                   ')
print('#################################')

# for largest divisor.
x = int(input("Enter an integer > 2:"))
smallest_divisor = None
for guess in range(2,x):
    if x%guess==0:
        smallest_divisor =  guess
        break
if smallest_divisor!=None:
    largest_divisor = int(x/smallest_divisor)
    print(f'The largest divisor of {x} except itself is {largest_divisor}.')
else:
    print(x, 'is a prime number.')
    
print('#################################')
print('              4                   ')
print('#################################')

# More fast and more efficeint code:

x =  int(input("Enter an enteger greater than 2:"))
smallest_divisor = None
if x%2==0:
    smallest_divisor = 2
else:
    for guess in range(3,x,2):
        if x%guess==0:
            smallest_divisor = guess
            break
if smallest_divisor!=None:
    print("The smallest divisor of",x, "is",smallest_divisor,".")
else:
    print(x,"is a prime number.")
        
"""
Finger exercise: Write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 1 < pwr < 6 and root**pwr is 
equal to the integer entered by the user. If no such pair of integers exists,
it should print a message to that effect.
"""
print('#################################')
print('              5                   ')
print('#################################')  

x = int(input('ENter an integer: '))
root = 0

for pwr in range(2,6):
    if x > 0:
        while root <= x:
            root += 1
        
            if root**pwr == x:            
                print(f'The root and power pair is = ({root},{pwr})')
        root = 0
    elif x < 0:
        while root >= x:
            root -= 1
        
            if root**pwr == x:            
                print(f'The root and power pair is = ({root},{pwr})')
        root = 0
    elif x == 0:
        print('There is no such pair!')
        break

"""
Finger exercise: Write a program that prints the sum of the prime numbers 
greater than 2 and less than 1000. Hint: you probably want to have a loop 
that is a primality test nested inside a loop that iterates over the odd 
integers between 3 and 999.
"""
print('#################################')
print('              6                  ')
print('#################################') 
import numpy as np
pr=[]
for num in range(2,999):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        pr.append(num)
            
print(pr)
print("The sum of prime numbers between 2 and 999 is = ",np.sum(pr))

print('##########################################')
print('Approximate Solutions and Bisection Search')
print('##########################################') 

# Find square root using exhaustic enumeration.
x=float(input("Enter a number:"))
epsilon = 0.01
step = epsilon**2
ans = 0.0
number_guesses = 0.0
while abs(ans**2-x)>=epsilon and ans<=x:
    ans +=step
    number_guesses +=1
print("Number of guesses is", number_guesses)
if abs(ans**2-x)>=epsilon:
    print("Failed to find the square root of",x)
else:
    print(ans, "is close to square root of",x)

##   Above code fails for x=0.25 so,
x=float(input("Enter a number:"))
epsilon = 0.01
step = epsilon**2
ans = 0.0
number_guesses = 0.0
while abs(ans**2-x)>=epsilon and ans*ans<=x:
    ans +=step
    number_guesses +=1
print("Number of guesses is", number_guesses)
if abs(ans**2-x)>=epsilon:
    print("Failed to find the square root of",x)
else:
    print(ans, "is close to square root of",x)

#Above code fails for large x, say x=123456 (The problem is that our step size
# was too large, and the program skipped over all the suitable answers.)
x=float(input("Enter a number:"))
epsilon = 0.01
step = epsilon**3
ans = 0.0
number_guesses = 0.0
while abs(ans**2-x)>=epsilon and ans*ans<=x:
    ans +=step
    number_guesses +=1
print("Number of guesses is", number_guesses)
if abs(ans**2-x)>=epsilon:
    print("Failed to find the square root of",x)
else:
    print(ans, "is close to square root of",x)

print('##########################################')
print('           Bisection Search               ')
print('##########################################') 

# Bisection search for square root.
x = float(input("Enter a number:"))
epsilon = 0.01
num_guesses, low = 0,0
high = max(1,x)
ans = (high+low)/2
while abs(ans**2-x)>=epsilon:
    print("low = ",low,"high = ",high,
          "number of guesses =", num_guesses)
    num_guesses +=1
    if ans**2<x:
        low = ans
    else:
        high =  ans 
    ans = (high + low)/2
print("number of guesses is = ",num_guesses)
print(ans, "is close to the square root of",x)

"""
Bisection search is a huge improvement over our earlier algorithm, which 
reduced the search space by only a small amount at each iteration.
"""
"""
To find the ans=log_2(x), we know, x=2**ans, so first we need to find the
interval in which the the ans lies then do bisection search.
"""
x = float(input("Enter a number:"))
epsilon = 0.01
# for interval 
lower_bound = 0
while 2**lower_bound<x:
    lower_bound +=1
low = lower_bound-1
high = lower_bound+1
# bisection search
ans = (low + high)/2
while abs(2**ans-x)>=epsilon:
    if 2**ans<x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2
print(ans, "is close to the log base 2 of",x)

# Bisection search for square root if x=-25.
x = float(input("Enter a number:"))
epsilon = 0.01
num_guesses, low = 0,0
high = max(1,abs(x))
ans = (high+low)/2
while abs(ans**2-abs(x))>=epsilon:
    print("low = ",low,"high = ",high,
          "number of guesses =", num_guesses)
    num_guesses +=1
    if ans**2<abs(x):
        low = ans
    else:
        high =  ans 
    ans = (high + low)/2
print("number of guesses is = ",num_guesses)
if x<0:
    print(str(ans)+"i", "is close to the square root of",x)
else:
    print(ans, "is close to the square root of",x)
    
# for cube root 
x = float(input("Enter a number:"))
epsilon = 0.01
num_guesses, low = 0,0
high = max(1,abs(x))
ans = (high+low)/2
while abs(ans**3-abs(x))>=epsilon:
    print("low = ",low,"high = ",high,
          "number of guesses =", num_guesses)
    num_guesses +=1
    if ans**3<abs(x):
        low = ans
    else:
        high =  ans 
    ans = (high + low)/2
print("number of guesses is = ",num_guesses)
if x<0:
    ans = -ans 
    print(ans, "is close to the cube root of",x)
else:
    print(ans, "is close to the cube root of",x)

"""
The Empire State Building is 102 stories high. A man wanted to know the
highest floor from which he could drop an egg without the egg breaking.
He proposed to drop an egg from the top floor. If it broke, he would go
down a floor, and try it again. He would do this until the egg did not 
break. At worst, this method requires 102 eggs. Implement a method that 
at worst uses seven eggs.
"""
#no_floor =  int(input("Enter number of floors:"))
no_floor = 102
number_eggs_boken,low = 0,1
high =  max(no_floor-7,no_floor)
max_no_eggs_broken = 7
ans = (low+high)/2
while abs(ans)<=abs(no_floor-max_no_eggs_broken):
    print("low = ",low,"high = ",high,
          "number of eggs broken =", number_eggs_boken)
    number_eggs_boken +=1
    low = ans
    ans = (low+high)/2
print("No of eggs broken =",number_eggs_boken)
print("The highest floor from which the egg does not break is",
      (no_floor-number_eggs_boken))

print('##########################################')
print('      Few Words about Using Floats        ')
print('##########################################')

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')
print("What ???????????")

# What is the decimal equivalent of the binary number 10011?
import numpy as np
x = str(int(input("Enter a binary nummber:")))
n = 0
decimal_no = []
while n<len(x):
    n +=1
    d = 2**(len(x)-n)
    decimal_no.append(d)
print(decimal_no)
pos = []
i=0
while i<len(x):
    b=int(x[i])
    i +=1
    pos.append(b)
print(pos)
z = np.dot(np.array([pos]),(np.array([decimal_no])).T)
print("The decimal of",x,"is",int(z))

print('##########################################')
print('            Newton–Raphson                ')
print('##########################################')

"""
Newton-Raphson method for square root

Find a number such x such that x**2-k is within the epsilon of 0.

"""
k = int(input("Enter a the number whoes sqrt is to be found:"))
epsilon = 0.001
guess =  k/2
while abs(guess**2-k)>=epsilon:
    guess = guess-((guess**2-k)/(2*guess))
print("The square root of ",k, "is close to ",guess)

"""
Finger exercise: Add some code to the implementation of Newton–Raphson 
that keeps track of the number of iterations used to find the root. 
Use that code as part of a program that compares the efficiency of 
Newton–Raphson and bisection search. (You should discover that 
Newton–Raphson is far more efficient.)

"""
k = int(input("Enter a the number whoes sqrt is to be found:"))
epsilon = 0.001
no_iter = 0
guess =  k/2
while abs(guess**2-k)>=epsilon:
    guess = guess-((guess**2-k)/(2*guess))
    no_iter +=1
print("The number of iteration is",no_iter)
print("The square root of ",k, "is close to ",guess)

# Bisection method.
k = int(input("Enter a the number whoes sqrt is to be found:"))
epsilon = 0.001
no_iter = 0
low = 0
high = max(1,k)
ans =  (low + high)/2
while abs(ans**2-k)>=epsilon:
    no_iter +=1
    if ans**2>k:
        high = ans
    else:
        low = ans
    ans = (low + high)/2
print("The number of iteration is",no_iter)
print("The square root of ",k, "is close to ",ans)