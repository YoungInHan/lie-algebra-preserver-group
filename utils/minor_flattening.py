#!/usr/bin/env python
# coding: utf-8

# In[81]:


from sage.all import *
import numpy as np

def form_indeterminates(nlst):
    res = []
    def recursive_form(passedvar, lst):
        if len(lst) == 1:
            for i in range(lst[0]):
                res.append("".join([passedvar, str(i)]))
        else:
            for i in range(lst[0]):
                newvar = "".join([passedvar, str(i)])
                recursive_form(newvar, lst[1:])
                
    recursive_form("", nlst)
    return [var("".join(["x_",s])) for s in res]

def form_flattening_pairs(n):
    res = []
    C = Combinations(range(len(n)))
    for i in range(int(len(C.list())/2)):
        c = C.list()[i]
        if len(c) == 0 or len(c) == len(n):
            continue
        for m in Combinations(range(len(n)), len(n) - len(c)):
            if len(set(c).union(set(m))) == len(n):
                res.append([c, m])
    return res

def form_flattening_pairs_MPS(n):
    res = []
    fp = form_flattening_pairs(n)
    for p in fp:
        left = all(i == j-1 for i, j in zip(p[0], p[0][1:]))
        right = all(i == j-1 for i, j in zip(p[1], p[1][1:]))
        if left and right:    
            res.append(p)
    return res

def indexer(n, dimensions, indexlst):
    if len(dimensions) == 0:
        return 0
    return n[dimensions[-1]]*indexer(n, dimensions[:-1], indexlst[:-1]) + indexlst[-1]
  
def flattening(pair, n):
    nrows = 1
    ncols = 1
    for i in pair[0]:
        nrows *= n[i]
    for i in pair[1]:
        ncols *= n[i]
    A = [[0 for i in range(ncols)] for j in range(nrows)]
    def recursive_form(passedvar, lst):
        if len(lst) == 1:
            for i in range(lst[0]):
                finalvar = "".join([passedvar, str(i)])
                indexes = [int(t) for t in list(finalvar)]
                indexesrow = [indexes[w] for w in pair[0]]
                indexescol = [indexes[w] for w in pair[1]]
                A[indexer(n, pair[0],indexesrow)][indexer(n, pair[1],indexescol)] = var("".join(["x_", finalvar]))
                
        else:
            for i in range(lst[0]):
                newvar = "".join([passedvar, str(i)])
                recursive_form(newvar, lst[1:])
                
    recursive_form("", n)
    return A

def get_flattening_minors(R, n, degree):
    minors = []
    res = form_flattening_pairs(n)
    for pair in res:
        A = flattening(pair, n)
        nrows = len(A)
        ncols = len(A[0])
        M = MatrixSpace(R, nrows, ncols)
        A_ = M(A)
        minors = minors + A_.minors(degree)
    return minors

def get_flattening_minors_MPS(R, n, degree):
    minors = []
    res = form_flattening_pairs_MPS(n)
    for pair in res:
        A = flattening(pair, n)
        nrows = len(A)
        ncols = len(A[0])
        M = MatrixSpace(R, nrows, ncols)
        A_ = M(A)
        minors = minors + A_.minors(degree)
    return minors

