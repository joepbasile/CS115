'''
Created on Aug 29, 2018

@author: joepb

'''
from cs115 import map, range, reduce
print('Hello world')

def prblm1(n):
    myList= range(1,n)
    listSum = sum(myList)
    return listSum

print(prblm1(5))

 

def makeSquare(n):
    n**2


def prblm2(n):
    myList= range(1,n)
    print(myList)
    #squareList = map(makeSquare, myList)
    #print(squareList)
    #listSum = sum(squareList)
    #return listSum

    return reduce(sum, map(makeSquare, range(1,n)))

print(prblm2(5))