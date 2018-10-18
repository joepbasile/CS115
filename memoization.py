'''
Created on Sep 10, 2018

@author: joepb
'''
import time

def fib(n):
    if n <=1:
        return n
    return fib(n-1)+ fib(n-2)

#start_time = time.time()
#print(fib(40))
#print('computation time without memoization: %.2f' % (time.time() - start_time))

def fib_memo(n):
    def fib_helper(n, memo):
        #if key is in memo return memo[n]
        if n in memo:
            return memo[n]
        #do work
        #recursivly compute the next fib number
        #store the result in a local variable
        if n <= 1:
            result = n
        else:
            result = fib_helper(n-1, memo) + fib_helper(n-2, memo)
        #store result in memo and return result
        memo[n] = result
        return result
    return fib_helper(n, {})
    
start_time = time.time()
print(fib_memo(900))
print('fib computation time with memoization: %.2f' % (time.time() - start_time))

def LCS(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2.
    '''
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def fast_LCS(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2.
    Uses memoization to improve performance.'''
    def fast_LCS_helper(S1, S2, memo):
        # If key exists, return value already associated with key.
        if (S1, S2) in memo:
            return memo[(S1, S2)]

        # Do work.
        if S1 == '' or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + fast_LCS_helper(S1[1:], S2[1:], memo)
        else:
            result = max(fast_LCS_helper(S1, S2[1:], memo),
                         fast_LCS_helper(S1[1:], S2, memo))

        # Store and return result.
        memo[(S1, S2)] = result
        return result

    return fast_LCS_helper(S1, S2, {})

def LCS_with_values(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2
    as well as the characters common to S1 and S2.'''
    if S1 == '' or S2 == '':
        return (0, '')
    if S1[0] == S2[0]:  # Do the first symbols match
        result = LCS_with_values(S1[1:], S2[1:])
        return (1 + result[0], S1[0] + result[1])
    use_s1 = LCS_with_values(S1, S2[1:])
    use_s2 = LCS_with_values(S1[1:], S2)
    if use_s1[0] > use_s2[0]:
        return use_s1
    return use_s2

def fast_LCS_with_values(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2
    as well as the characters common to S1 and S2.
    Uses memoization to improve performance.'''
    def fast_LCS_helper(S1, S2, memo):
        # If key exists, return value already associated with key.
        if (S1, S2) in memo:
            return memo[(S1, S2)]

        # Do work.
        if S1 == '' or S2 == '':
            result = (0, '')
        elif S1[0] == S2[0]:
            lose_both = fast_LCS_helper(S1[1:], S2[1:], memo)
            result = (1 + lose_both[0], S1[0] + lose_both[1])
        else:
            use_s1 = fast_LCS_helper(S1, S2[1:], memo)
            use_s2 = fast_LCS_helper(S1[1:], S2, memo)
            if use_s1[0] > use_s2[0]:
                result = use_s1
            else:
                result = use_s2

        # Store and return result.
        memo[(S1, S2)] = result
        return result

    return fast_LCS_helper(S1, S2, {})

start_time = time.time()

# This function call may take up to ~30 seconds.
print(LCS_with_values('SUPERMARDEFKET', 'BOSTONXYZMARKET'))
print('Computation time without memoization:', time.time() - start_time, 'seconds')

start_time = time.time()
print(fast_LCS_with_values('SUPERMARDEFKET', 'BOSTONXYZMARKET'))
print('Computation time with memoization:', time.time() - start_time, 'seconds')

def subSet(target, lst):
    """determines whether or not it is possible to create target sum using the values in the list, values in the list can be positive negative or zero"""
    def subSetHelper(target, lst, memo):
        if (target, lst) in memo:
            return memo[(target, lst)]
        if target == 0:
            result = True
        elif len(lst) == 0:
            result = False
        else:
            result = subSetHelper(target - lst[0], lst[1:], memo) or subSetHelper(target, lst[1:], memo)

        memo[(target, lst)] = result
        return result
    return subSetHelper(target, lst, {})

