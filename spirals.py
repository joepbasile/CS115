'''
Created on Oct 3, 2018

@author: joepb
'''
import turtle

def square_spiral(walls):
    def square_spiral_helper(walls, distance, initial, count):
        if walls == count:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(walls, distance + initial * (count%2), initial, count + 1)
    square_spiral_helper(walls, 20, 20, 0)
    
#square_spiral(100)

def octoganal_spiral(walls):
    def oct_spiral_helper(walls, distance, initial, count):
        if walls == count:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            oct_spiral_helper(walls, distance+initial*(count%2), initial, count+1)
    oct_spiral_helper(walls,20,1,0)


octoganal_spiral(300)