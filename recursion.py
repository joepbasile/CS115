'''
Created on Sep 10, 2018

@author: joepb
'''
import math 
import sys
from cs115 import map, reduce, range, filter
from cmath import sqrt
from test.crashers.mutation_inside_cyclegc import lst
sys.setrecursionlimit(10000)
def factorial2(n):
    if n==0:
        return 1
    return n * factorial2(n-1)


def tower(n):
    """takes n raised to the 2"""
    if n == 0:
        return 1
    return 2 ** (tower(n-1))



def tower_reduce(n):
    """compute 2^(2^(2...)) using reduce"""
    def power (x,y):
        return y**x
    return reduce(power,[2]*n, 1)


def length(lst):
    """returns the length of a list"""
    if lst==[]:
        return 0
    return 1 + length(lst[1:])
        

def length_srt(s):
    if s == '':
        return 0
    return 1 + length_srt(s[1:])



def reverse(lst):
    """this will input a list of elements and return it in reverse order"""
    if lst == []:
        return []
    return [lst[-1]]+ reverse(lst[0:-1])


def member(x, lst):
    """returns true if x is contained in the lsit false otherwsie"""
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])


def collapse(lst):
    """collapses a list of possibly nested lists into a single list of values"""
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return collapse(lst[0] + collapse(lst[1:]))
    return [lst[0]] + collapse(lst[1:])


def my_map(f, lst):
    """returns a new list where the function f has been applied to every element in the original list"""
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def sqr(x):
    return x * x

print(my_map(sqr, [1,2,3,4,5]))

def power(x,y):
    """returns x*y"""
    if y == 0:
        return 1
    return x * power(x,y -1)

def power_tail(x, y):
    """computes x*y using tail recursion"""
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y-1, accum*x)
    return power_tail_helper(x, y, 1)
    
def my_reduce(f, lst):
    """reduces the list to a single value as dictated by the predicate f"""
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst == []:
        raise TypeError('my_reduce() cannot take in an emoty list')
    return my_reduce_helper(f, lst[1:], lst[0])

def add(x,y):
    return x+y

def prime(n):
    """returns wether or not an integer is prime"""
    possibleDivisors = range(2, int(math.sqrt(n))+1)
    divisors = filter(lambda X: n % X == 0, possibleDivisors)
    return len(divisors) == 0

def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2,n+1))
    

def fib_of_n(n):
    """return the fibonaci sequence"""
    if n<=1:
        return n
    return fib_of_n(n-1) + fib_of_n(n-2)

def subset(target, lst):
    """determines whether or not it is possible to create target sum using the 
    values in the list can be positive, negative, or 0"""
    if target == 0:
        return True
    if lst == []:
        return False
    #use_it = subset(target- lst[0], lst[1:])
    #lose_it = subset(target, lst[1:])
    return subset(target- lst[0], lst[1:]) or subset(target, lst[1:])

def powerset(lst):
    """returns the power set of the list which is the set of all subsets of the list"""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset:[lst[0]]+ subset, lose_it)
    return lose_it + use_it


def subset_with_values(target, lst):
    """determines whether or not it is possible to create the target sum using 
    values in the list values can be positive negative or 0. the function returns
    a tuple of exactly to items. the first is a boolean that indicates true if the sum is possible false if it is not possible
    the second element in the tuple is a list of all the values that add up to make the target sum"""
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target-lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

print(subset_with_values(5, [3,1,2]))

def LCS(s1, s2):
    """returns the length of the longest common sub sequence in strings s1 and s2"""
    if s1 == '' or s2== '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

print(LCS('spot', 'pot'))

def LCS_with_values(s1, s2):
    if s1 == '' or s2 == '':
        return [0 , '']
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return [1 + result[0], s1[0] + result[1]]
    useS1 = LCS_with_values(s1, s2[1:])
    useS2 = LCS_with_values(s1[1:], s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

print(LCS_with_values('spot', 'pots'))
    