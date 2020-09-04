"""

    1.Introduction
        This assignment will help you to consolidate the concepts learnt in the session.
    
    2.Problem Statement
        1.1 Write a Python Program to implement your own myreduce() function which works exactly
            like Python's built-in function reduce()
        1.2 Write a Python program to implement your own myfilter() function which works exactly
            like Python's built-in function filter()
    

"""


###Solution 2.1.1 Building myreduce() function


def myAddition(a,b):
    return a+b


def myreduce(func, iter):
    result = 0
    for i in range(len(iter)):
        result = myAddition(result, iter[i])
    return result
    





print('Result of MyReduce function is: ',myreduce(myAddition, [1,2,3,4,5]))




###Solution 2.1.2 Developing my Filter function


def vowelFilter(alpha):
    vowels = ['a','e','i','o','u']
    for i in vowels:
        if(alpha in vowels):
            return True
        else:
            return False

def myfilter(func, iter):
    result = []
    for i in iter:
        if vowelFilter(i) == True:
            result += list(i)
    return result



sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

print('Result of myfilter function is: ',myfilter(vowelFilter, sequence))