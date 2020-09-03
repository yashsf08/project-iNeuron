"""
1. Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

from math import ceil
def draw_pattern(data):

    upper_limit = ceil(data/2)
    print(upper_limit)
    lower_limit = 0
    for i in range(upper_limit):
        print('*'*(i+1))

    for i in range(upper_limit-1,0,-1):
        print('*'*i)
       
number = int(input("Dear User, provide number of lines for you wish to draw pattern: " ))
draw_pattern(number)
