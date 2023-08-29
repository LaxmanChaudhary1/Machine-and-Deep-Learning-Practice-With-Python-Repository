#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:07:45 2023

@author: laxman
"""
print('#################################')
print('              1                   ')
print('#################################')
#"f-string"
num = 300000
fraction = 1/2 

print(f'{int(num*fraction)} is {fraction*100}% of {num}')

print(f'{{{3*5}}}')
#print(f'{{2*4}}') ??
print('#################################')
print('                2                 ')
print('#################################')
"""
The expression inside an f-string can contain modifiers that control 
the appearance of the output string.These modifiers are separated from 
the expression denoting the value to be modified by a colon. For
example, the f-string ﻿ ﻿f'{3.14159:.2f}' evaluates to the string ﻿'3.14' 
because the modifier .2f instructs Python to truncate the string 
representation of a floating-point number to two digits after the 
decimal point. 
"""
print(f'{3.14159:.2f}')
# And , instructs to give the commas as thausands seperators 
print(f'{num*fraction:,} is {fraction*100}% of {num:,}')
print(f'{num*fraction:,.0f} is {fraction*100}% of {num:,}') # .0f means no digits
# after decimal point.
"""
lines can be made single line by using \ or brackests
"""
print('#################################')
print('               3                  ')
print('#################################')
x = (1111111111+
      2222222222+
      3333333333)
print(x)
# or by
y = 1111111111+\
    2222222222+\
    3333333333
print(y)
print('#################################')
print('               4                  ')
print('#################################')
name = input('Enter your name:')
print(f'Are you really {name} ?')

n = input('Enter an int:')
print(type(n))

print("input always give str tpye even if you enter object like int for instance if you enter 3 it prints '3'")

DOB = input("Enter your date of birth in the mm/dd/yyyy format:")
print(f'you were born in {DOB[6:len(DOB)]}')
#or
from datetime import datetime

birthday = input("Enter your date of birth: ")
bday = datetime.strptime(birthday, '%d/%m/%Y')
print(f'You were born on {bday}')
"""
For many years most programming languages used a standard called ASCII for the internal representation of characters. This standard included 128 characters, plenty for representing the usual set of characters appearing in English-language text—but not enough to cover the characters and accents appearing in all the world's languages.
The Unicode standard is a character coding system designed to support the digital processing and display of the written texts of all languages. The standard contains more than 120,000 characters—covering 129 modern and historic scripts and multiple symbol sets. The Unicode standard can be implemented using different internal character encodings. You can tell Python which encoding to use by inserting a comment of the form

# -*- coding: encoding name-*-
as the first or second line of your program. For example,

# -*- coding: utf-8 -*-
instructs Python to use UTF-8, the most frequently used character encoding for webpages.18 If you don't have such a comment in your program, most Python implementations will default to UTF-8.
When using UTF-8, you can, text editor permitting, directly enter code like
"""
print('Mluvíš anglicky?')
print('क्या आप अंग्रेज़ी बोलते हैं?')

# A generic iteration (also called looping) mechanism
print('#################################')
print('               5                  ')
print('#################################')
# looping 

x = 3
ans = 0 
num_iteration = 0
while (num_iteration<x):
    ans = ans + x
    num_iteration +=1
print(f'{x}*{x} = {ans}')
print('#################################')
print('                6(RR)                ')
print('#################################') 
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)

# Find a positive number that is divisible by both 11 and 12 
x =  1
num_iter = 0
while True:
    if x%11==0 and x%12==0:
        break 
    x += 1
    num_iter +=1
print(f'no.of iteration is {num_iter}')
print(f'{x} is divisible by both 11 and 12')
print('#################################')
print('               7                 ')
print('#################################')
a = []
number = 0
while number < 10:
    x = int(input("Enter an integer:"))
    number +=1
    a.append(x)
largest_odd = None
for i in a:
    if i%2==1:
        if largest_odd is None or i > largest_odd:
            largest_odd = i
print(a)
if largest_odd is None:
    print("No odd number was entered.")
else:
    print("The lagest odd integer entered was :",largest_odd)
print('#################################')
print('               8                  ')
print('#################################')       
for n in range(2,100,7):
    print(n)
for n in range(100):
    print(n)
print('#################################')
print('              9                   ')
print('#################################')
iter=0
x = 4
for j in range(x):
    for i in range(x):
        x = 2
        iter +=1
print(f'No.of iterations is {iter}')
print('#################################')
print('              10                   ')
print('#################################')
total = 0
for c in '12345678':
    total = total + int(c)
print(total)


