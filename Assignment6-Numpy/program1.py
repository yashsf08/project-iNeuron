#! /home/devops/anaconda3/bin/python

"""
Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. 
Specifically, when increasing is False, the i-th output column is the input vector raised 
element-wise to the power of N - i - 1. 

HINT: Such a matrix with a geometric progression 
in each row is named for Alexandre- Theophile Vandermonde.

"""

import numpy as np


def myvander(x, N=0, increasing=False):
	N = len(x) if N == 0 else N
	print(N)
	result = np.zeros((len(x),N))
	for i,j in enumerate(x):
		for k in range(N):
			result[i,k] = j ** k



	print('size of the matrix is :',result[:,-1::-1] if increasing == False else result,sep='\n')
	
myvander([1,2,3,4], increasing=True)

