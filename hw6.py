'''
Created on Oct 14, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Joseph Basile
username: jbasile1
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    return numToBinary(n // 2) + str(n%2)

def numToBinaryPadded(n):
    """will take in a number and padd it so it will be at least a length of 5"""
    s = numToBinary(n)
    return "0" * (COMPRESSED_BLOCK_SIZE - len(s)) + s

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def prefixLen(S):
    """takes in string S and returns how many of the first element in a row are there"""
    if len(S) == 1:
        return 1
    if S[1] == S[0]:
        return 1 + prefixLen(S[1:])
    return 1

def compress(S):
    """takes a binary string S of length 64 as input and returns another 
    binary string as output which is the run length encoding."""
    def compress_help(S,b):
        """helps the compress function compress complete its goal"""
        if S ==  '':
            return ''
        if S[0] != chr(b + ord('0')):
            return numToBinaryPadded(0) + compress_help(S, 1-b)
        prefixlength = min(prefixLen(S) , MAX_RUN_LENGTH)
        return numToBinaryPadded(prefixlength) + compress_help(S[prefixlength:],1-b)
    return compress_help(S, 0)

def uncompress(C):
    """takes in a compressed binary string C and it
     "inverts" or "undoes" the compressing in the compress function."""
    def uncompress_help(C, b):
        """helps the uncompress function complete its goal."""
        if C == '':
            return ''
        n = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])
        return chr(b+ord('0'))*n + uncompress_help(C[COMPRESSED_BLOCK_SIZE:], 1-b)
    return uncompress_help(C, 0)        

def compression(S):
    """will return the ratio of the compressed size to the original size for image S""" 
    return len(compress(S))/len(S)



'''
The largest possible number of bits that my compress algorithm could use is 325. This is because
when the 64-bit string/image switches from 1 to 0 in quick succession it causes the compress file to get bigger and when the 
sequence repeats "10" for the whole 64 bits is when it becomes its largest. Since it will take 5 bits for each 1 and 0 it will be 64*5=320 and 
since it always will assume the first number is a 0 it will add 5 0s to the beginning making the total 325.

Professor Lai's algorithm cannot exist. It cannot exist because if the 64 bit sequence changes from 0s to 1s in succession 
without a long row of repeating 1s or 0s the compressed sequence will be longer than the initial sequence. Like with the situation where the 64 bit string/image
 is repeating '10' for the whole 64 bits it will have lots of "00000" and "00001" making the sequence 325 bits long.
'''