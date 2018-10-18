'''
Created on Sep 19, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
'''
import math
def change(amount, coins):
    """takes in an input amount which a non-negative integer indicating the amount of money to be made and a list coins 
    of coin values with 1 always being in the list when we first call the function. (This ensures that it 
    is always possible to make change for any positive amount.) The function should return a non-negative integer
    indicating the minimum number of coins required to make up the given amount."""
    if amount==0:
        return 0
    if coins == [] or amount < 0:
        return float('inf')
    use_it= change(amount-coins[0],coins) + 1
    lose_it= change(amount,coins[1:])
    return min(use_it,lose_it)
    
