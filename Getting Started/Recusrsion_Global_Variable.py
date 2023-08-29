#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:13:59 2023

@author: laxman
"""

"""
Like strings, tuples are immutable ordered sequences of elements.
The difference is that the elements of a tuple need not be characters. 
The individual elements can be of any type, and need not be of the same 
type as each other.
"""
t1 = ()
t2 = (1, "two", 3)
print(t1)
print(t2)

t3 = ("a", "n", 3)
t4 = 3*t3 # repetition 
print(t4)
#print(t4/3) not  allowed 

t5 = (t2, 1.25)
print(t2 + t5)
print((t2+t5)[3])
print((t2+t5)[2:5])

def intersect(t1,t2):
    """
    

    Parameters
    ----------
    t1 : Tuple
    t2 : Tuple
       t1 and t2 are tuples and 

    Returns
    -------
    Tuple containing elesments that are both in t1 and t2.

    """
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result
intersect(t2, t5)

intersect((1,"a",2), ("b",2,"a"))

"""
Multiple Assignment
"""
"""
If you know the length of a sequence (e.g., a tuple or a string), 
it can be convenient to use Python's multiple assignment statement 
to extract the individual elements. For example, the statement x, y = (3, 4), 
will bind x to 3 and y to 4. Similarly, the statement a, b, c = 'xyz' 
will bind a to 'x', b to 'y', and c to 'z'.
"""
def find_extreme_divisors(n1,n2):
    """
    

    Parameters
    ----------
    n1 : positive int.
    n2 : positve int.

    Returns
    -------
    A tuple containing smallest divsor of both other than 1 and largest common
    divisor of n1 and n2. If no common diviisor other than 1 then it returns
    (None,None).

    """
    min_val,max_val = None, None
    for i in range(2,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            if min_val==None:
                min_val = i
            max_val = i
    return min_val,max_val
find_extreme_divisors(100, 200)

"""
Ranges and Iterables
"""
range(10)[2:6][2]

range(0, 7, 2) == range(0, 8, 2)

range(0, 7, 2) == range(6, -1, -2)# occur in different order

"""
In Python 3, range is a special case of an iterable object. 
All iterable types have a method, __iter__ that returns an 
object of type iterator.
""" 
help(range)

"""
Finger exercise: Write an expression that evaluates to the mean of a 
tuple of numbers. Use the function sum.
"""
mean = sum(range(101))/len(range(101))

mean

"""
Lists and Mutability
"""
l = ["I did it all",4,"love"]
for e in l:
    print(e)

#slicing 
l1 = [1,2,3]
l2 = l1[-1::-1]
for i in range(len(l1)):
    print(l1[i]*l2[i])
print(l2)

l3 = [4,8,11]
l4 =l3[-1:0:-2]
l4
l4 =l3[-1::-2]
l4
l4 =l3[-2::-1]
l4

"""
Lists differ from tuples in one hugely important way: lists are mutable.
In contrast, tuples and strings are immutable.
"""

Techs = ["MIT","Caltech"]
Ivys  = ["Harvard","Yale","Brown"]

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print("Univs = ",Univs)
print("Univs = ",Univs1)
print(Univs==Univs1)
####################################################
print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print(Univs is Univs1) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))

Techs.append('RPI')
Techs
Univs
"""
append method mutate Techs but nothing to Univs! 
"""
L1 = [[]]*2
L2 = [[], []]
for i in range(len(L1)):
    L1[i].append(i)
    L2[i].append(i)
print('L1 =', L1, 'but', 'L2 =', L2)

"""
Finger exercise: What does the following code print? 

﻿L = [1, 2, 3]
L.append(L)
print(L is L[-1])
"""
L = [1,2,3]
L.append(L)
print(L is L[-1])

def append_val(val, list_1 = []): 
    list_1.append(val)
    print(list_1)

append_val(3)
append_val(4)

"""This happens because, at function definition time, a new object of type 
list is created, with an initial value of the empty list. Each time 
append_val is invoked without supplying a value for the formal parameter 
parameter list_1, the object created at function definition is bound to 
list_1, mutated, and then printed.

"""
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

L = ['a','love','e','manu','majnu','s','m','m','love']
L.append('e')
L.count('e')
L.insert(0,'e')
L.extend(L1)
L.remove('e')# removes first occurance of e
L.index('e')
L.pop(-1) # if nothing inside pop() it is -1 as default.
L2.sort() # ascending order.
L.reverse() 

"""
Cloning
"""

def remove_dups(L1,L2):
    """
    

    Parameters
    ----------
    L1,L2 : Assumes lists.

    Removes any element that is in both L1 and L2.

    """
    for e in L1:
        if e in L2:
            L1.remove(e)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print("L1 = ",L1)

L.copy()
L.copy()==L[:]

"""
Both slicing and copy perform what is known as a shallow copy. A shallow 
copy creates a new list and then inserts the objects (not copies of 
the objects) of the list to be copied into the new list.
"""
L = [2]
L1 = [L]
L2 = L1[:] 
L2 = L2.copy.deepcopy(L1)
L.append(3)
print(f'L1 = {L1}, L2 = {L2}')

"""
The method deepcopy creates a new list and then inserts copies of the 
objects in the list to be copied into the new list.
"""
L1 = [2]
L2 = [L1,L1] 
L3 = L3.copy.deepcopy(L2)
L3[0].append(3)
print(L3)


"""
List Comprehension
"""
# It is an expression of the form
# [expr for elemin iterable if test] is equvalent to:

"""def f(expr,old_list,test=lambda x:True):
    new_list = []
    for e in iterable:
        if test(e):
                new_list.append(expr(e))
    return new_list
"""

# example
[e**2 for e in range(6)]

[e**2 for e in range(8) if e%2 == 0]        

[x**2 for x in [2, 'a', 3, 4.0] if type(x) == int]

# List comprehension provides a convenient way to initialize lists.
[[] for _ in range(10)]

[[i] for i in range(10)]

# Multiple for statements
L = [(x, y)
     for x in range(6) if x%2 == 0
     for y in range(6) if y%3 == 0]
L

"""Of course, we can produce the same list without list comprehension, 
but the code is considerably less compact:"""

L = []
for x in range(6):
    if x%2==0:
        for y in range(6):
            if y%3==0:
                L.append((x,y))
print('L = ',L)

# Use list comprehension to print all prime numbers less than 100

[x for x in range(2,100) if all(x%y!=0 for y in range(2,x))]
Le=[x for x in range(2,100) if all(x%y!=0 for y in range(2,x))] 

# And nested function 
def gen_prime():
    prime = []
    for x in range(2,100):
        is_prime = True
        for y in range(2,x):
            if x%y==0:
                is_prime = False
        if is_prime:
            prime.append(x)
    return prime
gen_prime()

"""Finger exercise: Write a list comprehension that generates all 
non-primes between 2 and 100."""

[x for x in range(2,100) if any(x%y==0 for y in range(2,x))]
Lne=[x for x in range(2,100) if any(x%y==0 for y in range(2,x))]
len(Lne)
len(Le)
len(range(2,100))-len(Le)==len(Lne)

"""Some Python programmers use list comprehensions in marvelous and subtle 
ways. That is not always a great idea. Remember that somebody else may need 
to read your code, and “subtle” is rarely a desirable property for a program.
"""
"""
Higher-Order Operations on Lists
"""
def apply_to_each(L,f):
    """
    

    Parameters
    ----------
    L : List.
    f : function.

    Returns
    -------
    for each element e of list L f replaces e and mutates L, 
    f being argument of the function itself.

    """
    for i in range(len(L)):
        L[i]=f(L[i])
        
L = [1, -2, 3.33]
print("L =",L)
print("Apply abs to each element of L.")
apply_to_each(L,abs) 
print("L =",L)
print("Apply int to each element of L.")
apply_to_each(L,int)
print("L =",L)
print("Apply square to each element of L.")
apply_to_each(L,lambda x:x**2)
print("L =",L)


"""
In its simplest form the first argument to map is a unary 
function (i.e., a function that has only one parameter) and the second 
argument is any ordered collection of values suitable as arguments to the 
first argument. It is frequently used in lieu of a list comprehension.
"""

list(map(str, range(10)))

[str(e) for e in range(10)]

# They are equivalent.
list(map(str,range(10)))==[str(e) for e in range(10)]

# map function is usually used with for loop 
for i in map(lambda x:x**2,[2,6,4]):
    print(i)

# First argument being  fuction followed by ordered collection.
L1 = [1,28,36]
L2 = [2,57,9]
for i in map(min,L1,L2):
    print(i)
    
"""Finger exercise: Implement a function satisfying the following 
specification. Hint: it will be convenient to use lambda in the body of 
the implementation."""

def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    total = []
    for i in range(len(L1)):
        s = L1[i]**L2[i]
        total.append(s)
    return sum(total)

f([1,2], [2,3])

"""
Strings, Tuples, Ranges, and Lists
"""

"""Python programmers tend to use lists far more often than tuples. 
Since lists are mutable, they can be constructed incrementally during a 
computation."""

L = range(2,100)
even_elems = []
for e in L:
    if e%2 == 0:
        even_elems.append(e)

even_elems

s = "abcdefghijklmnopqrstuvwxyz   "
s.count('i')
s.find('e') # returns -1 if e is not in s.
s.rfind("e")
s.index('e')
s.rindex('e')
s.lower()
s.replace('e','ee')
s.rstrip()
s.split('d')
s.title()
s.upper()
s.capitalize()
s.casefold()
s.center(2,"h")
s.count('e',3,5)
s.islower()
s.isalnum()
s.partition

print('My favorite professor–John G.–rocks'.split(' '))
print('My favorite professor–John G.–rocks'.split('-'))
print('My favorite professor–John G.–rocks'.split('–'))

"""Sets"""

baseball_teams = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

"""Since the elements of a set are unordered, attempting to index into a set,
 e.g., evaluating baseball_teams[0], generates a runtime error."""
 
baseball_teams[0]

# Like lists, sets are mutable.

baseball_teams.add('Yankees')
football_teams.update(['Patriots', 'Jets'])
print(baseball_teams)
print(football_teams)

"""
The binary methods union, intersection, difference, and issubset have 
their usual mathematical meanings. For example,
"""
print(baseball_teams.union({1, 2}))
print(baseball_teams.intersection(football_teams))
print(baseball_teams.difference(football_teams))
print({'Padres', 'Yankees'}.issubset(baseball_teams))

"""One of the nice things about sets is that there are convenient infix 
operators for many of the methods, including | for union, & for intersect, 
- for difference, <= for subset, and >= for superset. Using these operators 
makes code easier to read. Compare, for example,"""

print(baseball_teams|{1,2})
print(baseball_teams & football_teams)
print(baseball_teams - football_teams)
print({'Padres','Yankees'}<=baseball_teams)

"""
Not all types of objects can be elements of sets. All objects in a set
must be hashable. An object is hashable if it has
• A __hash__ method that maps the object of the type to an int, and the 
value returned by __hash__ does not change during the lifetime of the object,
 and 
• An __eq__ method that is used to compare it for equality to other objects.
"""
"""

Dictionaries
"""
"""Literals of type dict are enclosed in curly braces and each element is 
written as a key followed by a colon followed by a value. For example, 
the code,"""


month_numbers = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,
                 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print(month_numbers)
print('The third month is ' + month_numbers[3])
dist = month_numbers['Apr'] - month_numbers['Jan']
print('Apr and Jan are', dist, 'months apart')

# Example
EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
'eat':'mange', 'drink':'bois', 'John':'Jean',
'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
'mange':'eat', 'bois':'drink', 'Jean':'John',
'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word,dictionary):
    if word in dictionary.keys():
        return dictionary(word)
    elif word!='':
        return '"'+ word + '"'
    return word
def translate(phrase,dicts,direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation\
                + translateWord(word, dictionary) + c
        word = ''
    return translation + ' ' + translateWord(word, dictionary)

translate('I drink good red wine, and eat bread.',
                dicts,'English to French')
translate('Je bois du vin rouge.',
                dicts, 'French to English')


"""
It is, for example, relatively easy to implement a dictionary by using a 
list in which each element is a tuple representing a key/value pair. We can
then write a simple function that does the associative retrieval, e.g.,
"""

def key_search(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

# But is computationaly inefficient.

# for statement chooses the keys in the order they were enterd in dictionary.

capitals = {'France':'Paris','Italy':'Rome','Japan':'Kyoto'}
for key in capitals:
    print('The capital of',key,'is',capitals[key]+'.')
    
# Method value
cities = []
for val in capitals.values():
    cities.append(val)
print(cities,"is the list of capital cities.")

len(capitals) #returns the number of items in d.
capitals.keys() #returns a view of the keys in d.
capitals.values() #returns a view of the values in d.k in d #returns True if key k is in d.
capitals['Italy'] #returns the item in d with key k.
capitals.get('Italy', 'v') #returns d[k] if k is in d, and v otherwise.
capitals['Italy'] = 'v' #associates the value v with the key k in d. If there is already a value#associated with k, that value is replaced.
del capitals['Italy'] #removes the key k from d.for k in d iterates over the keys in d.

cap_vals = capitals.values()
print(cap_vals)
capitals['Japan'] = 'Tokyo'
print(cap_vals)

# Example
for key, val in capitals.items():
    print(val, 'is the capital of', key)


"""
Finger exercise: Implement a function that meets the specification.
"""
def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12."""
    if not d:
        return None
    min_key = min(d.keys())
    return d[min_key]

d = {"x":11,"b":12}
get_min(d)


"""
Dictionary Comprehension
"""

"""
Dictionary comprehension is similar to list comprehension. The general form is

{key: value for id1, id2in iterable if test}
"""

# example 
number_to_word = {1:'one',2:'two',3:'three',4:'four',10:'ten'}

# Using dictionary comprehension

word_to_number = {w:d for d,w in number_to_word.items()}

word_to_number

# book cipher 
gen_code_keys = (lambda book, plain_text:(
                {c: str(book.find(c)) for c in plain_text}))

gen_code_keys('Once upon a time, in a house in a land far away,', 'no is no')

encoder =( lambda code_keys, plain_text:''.join(['*' + code_keys[c] for c in plain_text])[1:])
    
encrypt = (lambda book, plain_text:encoder(gen_code_keys(book, plain_text), plain_text))
Don_Quixote = "In a village of La Mancha, the name of which I have no desire \
 to call to mind, \
 there lived not long since one of those gentlemen that keep a lance in the \
 lance-rack, an old buckler,\
 a lean hack, and a greyhound for coursing."

encrypt(Don_Quixote, 'no is no')

"""
Finger exercise: Remedy the problem described in the previous paragraph. 
Hint: a simple way to do this is to create a new book by appending something 
to the original book.
Finger exercise: Using encoder and encrypt as models, implement the 
functions decoder and decrypt. Use them to decrypt the message

﻿﻿22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*
59*11*23*11*1*57*6*173*7*11
"""

