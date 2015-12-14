# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 18:32:41 2015

@author: Shuang

Count inversions
"""


path = "/Users/Shuang/Documents/Python Scripts/algorithm/IntegerArray.txt"  

with open(path) as f:
    A = []
    for line in f:
        A.append(int(line.strip()))



'''
divide the list into half , sort/count the inversion in the first half
...for the second half, ... for the split inversion
'''

def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      C, c = SortCount(A[:n])
      D, d = SortCount(A[n:])
      B, b = MergeCount(C,D)
      return B, b+c+d
   else:
      return A, 0

#count and sort the split inversions
def MergeCount(A,B):
   count = 0
   M = []
   while A and B: #while A&B are not empty
      if A[0] < B[0]: 
         M.append(A.pop(0)) 
      else: 
         count += len(A) # bc A and B are both sorted list
         M.append(B.pop(0)) 
   M  += A + B  #add the left-over elements to M    
   return M, count 