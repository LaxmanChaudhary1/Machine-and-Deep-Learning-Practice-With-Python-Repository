#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:25:00 2023

@author: laxman
"""

"""
FUNCTIONS, SCOPING, AND ABSTRACTION
"""
def max_val(x,y):
    if x>y:
        return x
    else:
        return y
max_val(23,3)

# Root finder.
def find_root(x,power,epsilon):
    if x<0 and power%2==0:
        return None # Negative number does not have even powered root.
    low=min(-1,x)
    high=max(1,x)
    ans=(low+high)/2
    # bisectio rule to find root
    while abs(ans**power-x)>=epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans=(low+high)/2
    return ans

print(find_root(27,3,0.000000000000001))

# testing above function
def test_find_root(x_vals,powers,epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                results = find_root(x,p,e)
                if results == None:
                    val = "No root exist"
                else:
                    val = "Okay"
                    if abs(results**p-x)>e:
                        val = "Bad"
                print(f'x={x},power={p},epsilon={e}:{val}')
x_vals =(0.25,8,-8)
powers =(1,2,3)
epsilons = (0.1,0.001,1)
print(test_find_root(x_vals,powers,epsilons))

"""
Finger exercise: Use the find_root function in above to print the sum of 
approximations to the square root of 25, the cube root of -8, and the 
fourth root of 16. Use 0.001 as epsilon.

"""
def sum_find_root(x_vals,powers):
    results =[]
    for i in range(0,3):
        result = find_root(x_vals[i],powers[i],0.001)
        if result==None:
            result=0
        else:
            results.append(result)
    print(results)
    print(f'The sum is {sum(results)}')
x_vals = (25,-8,16)
powers = (2,3,4)
print(sum_find_root(x_vals,powers))

"""
Finger exercise: Write a function is_in that accepts two strings as 
arguments and returns True if either string occurs anywhere in the 
other, and False otherwise. Hint: you might want to use the built-in
str operator in.

"""
def is_in(str1,str2):
    if type(str1)==str and type(str2)==str: 
        if str1 in str2:
            print(f'{str1} is in {str2}')
        elif str2 in str1:
            print(f'{{{str2}}} is in {{{str1}}}')
        else:
            print("None of the strings entered in anywhere in the other.")
    else:
        print("One of the arguement entered is not str type!")

str1 = "Hello my name is laxman chaudhary. I live in Kirtipur."
str2 = "name"

print(is_in(str1,str2))

# correct one is 
def is_in(str1,str2):
    if type(str1)==str and type(str2)==str: 
        if str1 in str2:
            return True
        elif str2 in str1:
            return True
        else:
            return False
    else:
        print("One of the arguement entered is not str type!")
        
is_in("g","ram is strong")
is_in("l", "ram is strong")

"""
Finger exercise: Write a function to test is_in.
"""
## Remaining 


"""
Keyword Arguments and Default Values
"""

def print_name(first_name, last_name, reverse): 
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)
        
print_name('Laxman','Chaudhary',False)

print_name('Laxman','Chaudhary',True)
"""
Default values allow programmers to call a function with fewer than the
specified number of arguments.for example:
"""
def print_name(first_name, last_name, reverse=False): 
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)
print_name('Laxman','Chaudhary')
print_name('Laxman','Chaudhary',True)
print_name(last_name = 'Chaudhary', first_name = 'Laxman')
print_name(last_name = 'Chaudhary', first_name = 'Laxman',reverse=True)
print_name(last_name = 'Chaudhary',reverse=True, first_name = 'Laxman')


"""
Finger exercise: Write a function mult that accepts either one or two ints
as arguments. If called with two arguments, the function prints the product 
of the two arguments. If called with one argument, it prints that argument.
"""
def mult(*ints):
    if len(ints)==1:
        print("The entered integer is",str(ints[0])+".")
    elif len(ints)==2:
        mul = ints[0]*ints[1]
        print(f'The product of {ints[0]} and {ints[1]} is {mul}.')
    else:
        print("The function takes only one arg or two args.")
mult(3)
print(mult(3,6,5))
print(mult(2,7))
#print(mult("l",2))
mult(2,7)
"""
Variable Number of Arguments
"""
def mean(*args):
    total = 0
    for a in args:
        total +=a
    return total/len(args)
mean(1,3,8)

"""
Scoping
"""    

def f(x): #name x used as formal parameter
    y = 1
    x = x + y
    print('x =', x)
    return x
x = 3
y = 2
z = f(x) #value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)

"""
static or lexical scoping.
"""
def f(x):
    def g():
        x = 'abc'
        print('x =',x)
    def h():
        z = x
        print('z =',z)
    x = x+1
    print('x =',x)
    h()
    g()
    print('x =',x)
    return g
x = 3
z = f(x)
print('x =',x)
print('z =',z)
z()

print("STILL CONFUSED WITH SCOPING ???")

"""
Specifications
"""

"""
The text between the triple quotation marks is called a docstring in Python.
By convention, Python programmers use docstrings to provide specifications 
of functions. These docstrings can be accessed using the built-in function 
help.
"""
help(abs)

def find_root(x,power,epsilon):
    """
    Parameters
    ----------
    x : int or float
        x assumes int or float values and if x is negative
        for even power it returns None.
    power : int
        Power assumes the positive integer values and power>=1.
    epsilon : int or float
        returns float y such that y**power is within the epsilon of x and
        epsilon>0.

    Returns
    -------
    float or 
    None.

    """
    # Find the interval containing ans.
    if x<0 and power%2==0:
        return None
    low = min(-1, x)
    high = max(1, x)
    # Use bisection rule 
    ans = (low + high)/2
    while abs(ans**power-x)>=epsilon:
        if ans**power<x:
            low = ans 
        else:
            high = ans 
        ans = (low + high)/2
    return ans 

find_root(45, 3,0.0001)

help(find_root)

"""
Exercise
""" 
def log(x, base, epsilon):
    """
    

    Parameters
    ----------
    x : int or float
        x>1.
    base : int
        power >= 1.
    epsilon : int or float
        epsilon >0.

    Returns
    -------
    returns float y such that base**y is within epsilon of x. 

    """
    # for interval 
    lower_bound = 0
    while base**lower_bound<x:
        lower_bound +=1
    low = lower_bound - 1
    high = lower_bound + 1
    # Bisection search 
    ans = (low + high)/2
    while abs(base**ans-x)>=epsilon:
        if base**ans<x:
            low = ans 
        else:
            high = ans 
        ans = (low + high)/2
    return ans 

log(10,10,0.001)

"""
Using Functions to Modularize Code
"""

"""As we implement more complicated functionality, it is convenient 
to split functions into multiple functions, each of which does one 
simple thing. To illustrate this idea we, somewhat superfluously, 
split find_root into three separate functions, as shown bellow:
"""
def find_root_bound(x,power):
    """
    x a float power a positive int.
    returns low and high such that low**power<=x and high**power>=x.
    """
    low = min (-1,x)
    high = max(1,x)
    return low, high

def bisection_solve(x,power,epsilon,low,high):
    """
    x, epsilon, low and high are floats and 
    epsilon>0.
    low <= high and there is ans in between low and high such that 
    ans**power is within the epsilon of x.
    returns ans s.t. ans is within the epsilon of x.
    """
    ans = (low + high)/2
    while abs(ans**power-x)>=epsilon:
        if ans**power<x:
            low = ans 
        else:
            high = ans 
        ans = (low + high)/2 
    return ans 
def find_root(x,power,epsilon):
    """
    Assumes x and epsilon int or float and power int.
    epsilon<0 & power >=1.
    returns float y such that y**power is within the epsilon of x.
    if such float does not exist it returns None.
    """
    if x<0 and power%2==0:
        return None # negative number has no even powered roots.
    low, high = find_root_bound(x, power)
    return bisection_solve(x, power, epsilon, low, high)

find_root(25,2, 0.01)

"""
Functions as Objects
"""
type(find_root)
type(abs)

"""
Using functions as arguments allows a style of coding called higher-order 
programming. It allows us to write functions that are more generally useful.
"""

def bisection_solve(x,eval_ans,epsilon,low,high):
    """
    x, epsilon, low and high are floats and 
    epsilon>0.
    low <= high and there is ans in between low and high such that 
    ans**power is within the epsilon of x.
    returns ans s.t. ans is within the epsilon of x.
    """
    ans = (low + high)/2
    while abs(eval_ans(ans)-x)>=epsilon:
        if eval_ans(ans)<x:
            low = ans 
        else:
            high = ans 
        ans = (low + high)/2 
    return ans 

# if we want to find the square root of 99.
def square(ans):
    return ans**2
low, high = find_root_bound(99,2)
print(bisection_solve(99, square, 0.01, low, high))

"""
Going to the trouble of defining a function to do something as simple as 
squaring a number seems a bit silly. Fortuitously, Python supports the 
creation of anonymous functions (i.e., functions that are not bound to a 
name), using the reserved word lambda. The general form of a lambda 
expression is

lambda sequence of variable names: expression

"""
"""
For example, the lambda expression lambda x, y: x*y returns a function that 
returns the product of its two arguments.
"""
lambda x, y: x*y

print(bisection_solve(99,lambda ans:ans**2,0.001,low,high))
"""
Finger exercise: Write a lambda expression that has two numeric parameters. 
If the second argument equals zero, it should return None. Otherwise it 
should return the value of dividing the first argument by the second 
argument. Hint: use a conditional expression.
"""
lambda x, y: x/y if y!=0 else None 

x=[1,2,3]
lambda x: [print(i**2) for i in x]

"""
Since functions are first-class objects, they can be created and returned 
within functions. For example,
"""
def creat_eval_ans():
    power = input("Enter a positive integer:")
    return lambda ans:ans**int(power)
eval_ans = creat_eval_ans()
print(bisection_solve(99, eval_ans, 0.001, low, high)) 

"""
Methods, Oversimplified
"""

s = 'abcbc'
s.find('bc')

sub = "ph"
s.find(sub)

def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    if sub in s:
        return(s.find(sub))
    else:
        return None
find_last(s, sub)
