'''
Created on Sep 5, 2018

I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
'''
from math import * 
import math
from cs115 import map, reduce, range

def add(x, y):
    """returns the sum of x + y"""
    return x+y

def inverse(n):
    """This will take a number n as an input and returns its reciprocal 1/n
    """
    return 1/n

def e(n):
    """approximates the mathematical value e using a Taylor expansion 
    1 + 1/1! + 1/2! ... 1/n!"""
    return reduce(add, map(inverse, map(factorial ,range(0,n+1))))

def error(n):
    """this returns the absolute value of the difference between the "actual" value of e 
    and the approximation from the e(n) function assuming that n terms(beyond the leading 1) are used)"""
    return abs(math.e - e(n))


    