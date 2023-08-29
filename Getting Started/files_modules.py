#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 08:57:10 2023

@author: laxman
"""

"""
FIles
"""
name_handle =open('kids','w')
for i in range(3):
    name = input("Enter a name:")
    name_handle.write(name+'\n')
name_handle.close()

# open the written file above 
with open('kids','r') as name_handle:
    for l in name_handle:
        print(l)
# another ex.
with open('pythonplan') as pyplan:
    for n in pyplan:
        print(n)

# another way to use write method
name_handle =open('kids','w')
name_handle.write('Michael')
name_handle.write('Mark')
name_handle.close()
name_handle = open('kids', 'r')
for line in name_handle:
    print(line) 

# we can open the file for appending
name_handle = open('kids', 'a')
name_handle.write('David')
name_handle.write('Andrea')
name_handle.close()
name_handle = open('kids', 'r')
for line in name_handle:
    print(line)
    
"""
Finger exercise: Write a program that first stores the first ten numbers in 
the Fibonnaci sequence to a file named fib_file. Each number should be on a 
separate line in the file. The program should then read the numbers from the
file and print them.
"""

fib_file = open('fib_file','w')
def fib(n):
    """n is a positve integer, it returns fibonacci of n."""
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(10):
    nu = str(fib(i))
    fib_file.write(nu +'\n')
# open
with open('fib_file') as fib_file:
    for l in fib_file:
        print(l)