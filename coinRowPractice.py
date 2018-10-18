'''
Created on Sep 21, 2018

@author: joepb
'''
import dis
from cs115 import map
def coinRow(coins):
    """There is a row of n coins whose values are some positive integers c1, c2, . . . , cn, not necessarily 
    distinct stored inside a list. The goal is to pick up 
    the maximum amount of money subject to the constraint that no two coins adjacent in the initial row can be picked up."""
    if coins == []:
        return 0
    use_it= coinRow(coins[2:]) + coins[0]
    lose_it= coinRow(coins[1:])
    return max(use_it,lose_it)



def coin_row_with_values(coins):
    """There is a row of n coins whose values are some positive integers c1, c2, . . . , cn, not necessarily 
    distinct stored inside a list. The goal is to pick up 
    the maximum amount of money subject to the constraint that no two coins adjacent in the initial row can be picked up."""
    if coins == []:
        return [0, []]
    use_it = coin_row_with_values(coins[2:]) #returns a list where cooins[0] is believed to be the max
    new_sum = coins[0] + use_it[0]
    lose_it = coin_row_with_values(coins[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [coins[0]] + use_it[1]]
    return lose_it
def distance(first, second):
    """given two strings how many changes would be needed to made to make the two strings equal"""
    if first == '':
        return len(second) 
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])
    insertion = distance(first, second[1:]) 
    deletion = distance(first[1:], second)
    return 1+ min(substitution, insertion, deletion)
print(map(lambda x: [x, x*x],filter(lambda x: x >= 2 and x<=5, [0,1,2,3,4,5])))
print(coinRow([]))
print(coin_row_with_values([]))
print(coinRow([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coinRow([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(distance("extraordinary", "originality"))
values = [1,2,3,4,5]
        
    
      
      