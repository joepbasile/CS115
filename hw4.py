'''
Created on Oct 1, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
'''

def pascal_row(n):
    """takes in a single number n representing the row number
    then return the values in the row of pascal's triangle"""
    def pascal_helper(n, row):
        """creates the list for the nth row of pascal's triangle"""
        if n == 0:
            return row
        return pascal_helper(n-1, [1] + pascal_helper2(row)+ [1])
    def pascal_helper2(row):
        """takes in the given list and creates the next row in pascal's triangle 
        while leaving out the first and last element"""
        if len(row) <= 1:
            return []
        return [row[0]+row[1]]+ pascal_helper2(row[1:])
  
    return pascal_helper(n, [1])   

def pascal_triangle(n):
    """takes in a single integer as input and returns a list
    of lists containing all the values from all the rows up to an including row n of pascal's triangle"""
    if n < 0:
        return []
    return pascal_triangle(n-1) + [pascal_row(n)]
