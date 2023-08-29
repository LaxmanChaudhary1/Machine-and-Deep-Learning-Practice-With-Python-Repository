#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:39:38 2023

@author: laxman
"""

"""
Here is an example of finding factorial of a natural number bot by iterative 
and recursive methods. 
"""
# Iterative method
def fact_iter(n):
    """
    assumes n an int>0
    and returns n!
    """
    result = 1
    for i in range(1,n+1):
        result *= i
    return result 
fact_iter(100)

# Recursive method.
def fact_rec(n):
    """
    Assumes n an int>0
    and returns n!
    """
    if n==1:
        return n
    else:
        return n*fact_rec(n-1)
len(str(fact_rec(100)))
str(fact_rec(100))

"""
Finger exercise: The harmonic sum of an integer, n > 0, can be calculated using
the formula 1+1/2+1/3+....+1/n. Write a recursive function that computes this.
"""

def har_sum(n):
    """
    Assumes n an int>o,
    returns sum 1+1/2+1/3+....+1/n.
    """
    if n==1:
        return n
    else:
        return 1/n + har_sum(n-1)

har_sum(2)

"""
Fibonacci Numbers
"""

def fib(n):
    """
    Assumes n an int>0,
    returns fibonacci of n.
    """
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_test(n):
    for i in range(1,n+1):
        print("fibonacci of",i,"is =",fib(i))
    
fib_test(9)

"""
Though the Fibonacci sequence does not actually provide a perfect model of the
growth of rabbit populations, it does have many interesting mathematical proper
ties. Fibonacci numbers are also common in nature. For example, for most flower
s the number of petals is a Fibonacci number.
"""


"""
Finger exercise: When the implementation of fib is used to 
compute fib(5), how many times does it compute the value of fib(2) on the way
to computing fib(5)?
"""
count = 0
def fib_ex(n):
    global count
    """
    Assumes n an int>0,
    returns fibonacci of n.
    """
    if n==0 or n==1:
        return 1
    else:
        count += 1
        return fib(n-1) + fib(n-2)
fib_ex(5)
print("fib_ex(2) was called",count,"times.")


"""
Palindromes
"""
def is_palindrome(s):
    """
    

    Parameters
    ----------
    s : string

    Returns
    -------
    True if letters in s forms palindrome and false if it does not.
    Non-letters and capitalization are ignored.

    """
    def to_char(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    def is_pal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and is_pal(s[1:-1])
    return(is_pal(to_char(s)))

print(is_palindrome('dogGod'))

"""
GLOBAL VARIABLE 
"""

def fib(n):
    """
    Assumes n an int>=0,
    returns fibonacci of n.
    """
    global num_fib_calls
    num_fib_calls +=1
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
def test_fib(n):
    for i in range(n+1):
        global num_fib_calls
        num_fib_calls = 0
        print("fib of ",i,"is = ",fib(i))
        print("fib called",num_fib_calls,"times")
        
fib(5)
test_fib(5)

