'''
Created on Sep 26, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
'''

def knapsack(capacity, itemList):
    """takes in an input of how much your knapsack could carry and a list of items that
    contains the weight of the item and the value of said item.  It then returns a list where the first element is the 
    max value you can take and the second item is a list of the items taken"""
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0, []]
    if capacity - itemList[0][0] < 0:
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity-itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    if itemList[0][1] + use_it[0] >= lose_it[0]:
        return [itemList[0][1] + use_it[0]] + [[itemList[0]] + use_it[1]]
    return [lose_it[0]] + [lose_it[1]]