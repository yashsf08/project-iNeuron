"""
    
    3. Implement List comprehensions to produce the following lists.
    Write List comprehensions to produce the following Lists

        ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

        ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

        ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

        [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],

        [4, 5, 6, 7], [5, 6, 7, 8]]

        [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

###Solution for List comprehension program


#print  ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

print([x for x in 'ACADGILD'])


#print         ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
print([i*j for j in 'xyz' for i in range(1,5) ] )


#print         ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
print([i*j for i in range(1,5) for j in 'xyz'])


#print [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
print([[j] for i in range(2,5) for j in range(i,i+3) ])

#print [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
print([[i for i in range(j,j+4)] for j in range(2,6) ])

#print         [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
print([(j,i) for i in range(1,4) for j in range(1,4) ])



