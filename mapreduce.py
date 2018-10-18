'''
Created on Sep 5, 2018

@author: joepb
'''
from cs115 import map, reduce, range


def span(lst):
    """returns the diff beteen the max and min numbers in a list"""
    return reduce(max, lst) - reduce(min, lst)

def add(x, y):
    """returns the sum of x + y"""
    return x+y
def gauss(n):
    """takes as input a positive integer n and returns the sum 1 + 2 + 3...
    """
    return reduce(add, range(1, n+1))

def square(x):
    """multiplies x by itself x*x"""
    return x*x
def mult(x, y):
    """returns the product of x*y"""
    return x*y

def sum_of_squares(n):
    """takes as input a positive integer a and returns the sum
    1^2 + 2^2 + 3^2...n^2"""
    return reduce(add, map(square,range(1, n+1)))

#def factorial():

print(span([3, 1, 42, 7]))
print(span([42, 42, 42, 42]))
print(gauss(5))
print(sum_of_squares(3))

list_of_ints = [1,2,3,4,5]
print(reduce(mult, list_of_ints))

list_of_strings = ['hello', 'my', 'name', 'is', 'is', 'Brain']
print(reduce(max, map(len, list_of_strings)))