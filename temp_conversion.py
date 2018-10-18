'''
Created on Aug 31, 2018

@author: joepb
'''
from Tools.scripts.objgraph import definitions
from test.test_binascii import a2b_functions
from pip._vendor.colorama.ansi import Back
"""
put the function at the top of the program
"""

def fahrenheit(celsius):
    """this will convert a celsius temp to a fahrenheit temp"""
    return (9/5)*celsius+32


def celsius(fahrenheit):
    """this will convert a fahrenheit temp to a celsius temp"""
    return (5/9)*(fahrenheit-32)


"""
call the functions below the function definitions
"""

c = float(input('Enter degrees in Celsius: '))
f = fahrenheit(c)

# you can print multiple items in one statement.  If you put a comma after each
# item, it prints a space then goes on t print the next item
print(c, 'C=', f, 'F')

# you can print this way too, by allowing exactly two decimal places by using %.2f we are forcing it to end at two decimal places
print('%.2f C = %.2f F' % (c, f))

f = float(input('Enter degrees in Fahrenheit'))
c = celsius(f)
print(f, 'F =', c, 'C')
print('%.2f F = %.2f C' % (f, c))

"""
try composition of functions
Converting a fahrenheit temp to celcius temp and back to fahrenhiet should give the original fahrenheit temp Back
"""

print()#print by itself on a new line
f = float(input('Enter degrees in fahrenheit: '))

#user assert to check the returned value is equal to the expected value
assert fahrenheit(celsius(f))==f
#no output should be produced, unless the assertion fails, which means you
#have an error(either in code or expectations)