'''
Created on Sep 13, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    """takes as input a single letter string called letter and a list where each element in that list is 
    itself a list of the form[character, value] then returns the value that is connected with the inputed letter."""
    if scorelist == []:
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])


def wordScore(S, scoreList):
    """take as input a string S and a scoreList which will have only lowercase letters,
     and should return as output the scrabble score of that string."""
    if S == '':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def listOfWords(Dictionary, Rack):
    """this will take in a rack and dictionary as input and return the list of words and their values possible with the given Rack"""
    return filter(lambda word: isPossible(word, Rack), Dictionary)
    
def isPossible(word, Rack):
    """it will take in a string words and a rack of characters it will determine if the word is possible with the given rack"""
    if word == "":
        return True
    if word[0] in Rack:
        return isPossible(word[1:], remove(word[0], Rack))
    return False

def remove(letter, Rack):
    """this will remove a letter from the Rack of letters"""
    if Rack == []:
        return []
    if letter != Rack[0]:
        return [Rack[0]] + remove(letter, Rack[1:])#this will add the letter back in the rack then move onto the next letter in the rack and see if it is = to letter
    if letter == Rack[0]:
        return Rack[1:]
    
def scoreList(Rack):
    """takes as input a Rack which is a list of lower-case letters and returns a list of all of the words in the 
    global Dictionary that can be made from those letters and the score for each one"""
    return map(wordScoreList, listOfWords(Dictionary, Rack))

def wordScoreList(word):
    """takes in a word as an input then returns the word and the score of the word in a lsit"""
    return[word, wordScore(word, scrabbleScores)]
    
def bestWord(Rack):
    """takes as input a Rack as above and returns a list with two elements: 
    the highest possible scoring word from thatRack followed by its score"""
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ['', 0]
    return reduce(lambda x,y: x if x[1]>y[1] else y, scorelist) #the lambda function will compare the number values of x and y and return x if it is bigger
    