'''
Created on Sep 12, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
'''

from cs115 import map, range, reduce

def add(x,y):
    """this will take integer x and y as input and output he sum of x+y"""
    return x + y

def dot(L, K):
    """this take lists L and K as input then it will return the dot product of the lists L and K"""
    if L == [] or K==[]:
        return 0.0
    return (L[0]*K[0]) + dot(L[1:], K[1:])


def explode(S):
    """it will take a string S as input and return a list of the characters in that string."""
    if S == '':
        return []
    return [S[0]] + explode(S[1:])



def ind(e, L):
    """takes in an element e and a sequence L then return the index at which e is first found in L or return the length of l if e is not found."""
    if L == [] or L =='':
        return 0
    if e == L[0]:
        return 0
    return  ind(e, L[1:]) + 1


def removeAll(e, L):
    """"takes in an element e and a list L then returns another list where all instances of e have been removed"""
    if L == []:
        return []
    if e != L[0]:
        return [L[0]] + removeAll(e, L[1:])
    return removeAll(e, L[1:])
print(removeAll('e', ['e','e','f','e']))

def even(X):
    """with will take a number x as input and return true if it is even or false therwise"""
    if X % 2 == 0 :
        return True
    return False

def myFilter(funcF, L):
    """takes an input of function f that takes as input a single input and returns eitherTrueor False. The second input is a list L. 
    It returns a new list that contains all of the elements of L for which the predicate returns True"""
    if L == []:
        return []
    if funcF(L[0])== True:
        return [L[0]] + myFilter(funcF, L[1:])
    return myFilter(funcF, L[1:])

def deepReverse(L):
    """this will take in a list L as input and return the reverse of that list and if elements in the list are lists it will reverse those as well."""
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]


        
        
