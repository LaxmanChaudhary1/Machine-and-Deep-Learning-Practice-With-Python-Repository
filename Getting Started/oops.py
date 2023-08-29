#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:11:53 2023

@author: laxman
"""

class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    def size(self):
        return len(self._elems)

print(type(Toy))
print(type(Toy.__init__))
print(type(Toy.add))
print(type(Toy.size))

t1 = Toy()
print(type(t1))
print(type(t1.add))

t2 = Toy()
print(t1 is t2)

"""While t.size is initially bound to the size function defined in the class 
Toy, that binding can be changed during the course of a computation. For 
example, you could (but definitely should not!) change the binding by 
executing t.size = 3."""

t1 = Toy()
t2 = Toy()
t1.add([3,4])
t2.add([4])
print(t1.size()+t2.size())
print(t1.add([3,4]))


class IntSet(object):
    """ An IntSet is a set of integers."""
    #Information about the implementation (not the abstraction)
    #Value of set is represented by the set of ints, self.vals.
    #Each int in the set occurs only once in the self.vals.
    
    def __init__(self):
        """create empty set of integers."""
        self.vals = []
    def insert(self,e):
        """Assumes e as an integers and inserts e into self."""
        if e not in self.vals:
            self.vals.append(e)
    def member(self,e):
        """Assumes e an integer and returns True if e in self and False
        otherwise."""
        return e in self.vals
    def remove(self,e):
        """Assumes e an integer and removes e if it is in the slef,
        and returns ValueError if e is not in self."""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'not found')
    def getMembers(self):
        """Returns the list containing the elements in self.
        Nothing can be assumed about the order of elements."""
        return self.vals[:]
    def __str__(self):
        """returns str representation of self."""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{'+result[:-1]+'}' # -1 ommits the trailing comma.

s = IntSet()
s.insert(3)  
print(s.member(3))
print(s.member(2))

s = IntSet()
s.insert(3)
s.insert(4)
print(str(s))
print("The value of s is",s)


"""exercise"""
def union(self, other):
    """other is an Int_set
    mutates self so that it contains exactly the elemnts in self
    plus the elements in other."""
    for e in other.getMembers():
       if not self.member(e):
           self.insert(e)
           
"""
+: __add__
*: __mul__
/: __truediv__
-: __sub__
//: __floordiv__
%: __mod__
**: __pow__
|: __or__
<: __lt__
<<: __lshift__
∧: __xor__
>: __gt__
>>: __rshsift__
==: __eq__
<=: __le__
&: __and__
!=: __ne__
>=: __ge__
"""

class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_slems):
        self._elems +=new_slems
    def __len__(self):
        return len(self._elems)
    def __add__(self,other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    def __eq__(self, other):
        return self._elems == other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
        return id(self)
        
t1 = Toy()
t2 = Toy()
t1.add([1,2])
t2.add([3,4])
t3 =  t1+t2
print("The value of t3 is",t3)
print("The length of t3 is ",len(t3))
d = {t1:"A",t2:"B"}
print("The value ",d[t1],"is related to the key t1 in d.")

"""Finger exercise: Replace the union method you added to Int_set by a 
method that allows clients of Int_set to use the ­+ operator to denote set 
union."""

def __add__(self, other):
    """other is an IntSet
    returns a new IntSet containing all the elements in self and other."""
    result = IntSet()
    for e in self.getMembers():
        result.insert(e)
    for e in other.getMembers():
        result.insert(e)
    return result

"""keeping track of students"""

import datetime
class Person(object):
    def __init__(self, name):
        """Create a person"""
    self.name = name
    try:
        lastBlank = name.rindex(' ')
        self.lastName = name[lastBlank+1:]
    except:
        self.lastName = name
        self.birthday = None
    def getName(self):
        """Returns self's full name"""
        return self.name
    def getLastName(self):
        """Returns self's last name"""
        return self.lastName
    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate
    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        """Returns self's name"""
        return self.name