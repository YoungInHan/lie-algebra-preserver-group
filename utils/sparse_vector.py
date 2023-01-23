#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data processing cell to flatten sparse vectors over V. We also create an optimized inner product function on such vectors.

# V => V
def sparsify(v):
    flattened_list = []
    for index, value in enumerate(v):
        if v[index] != 0:
            flattened_list.append((index,value))
    return flattened_list

# <V,V> => QQ
def sparse_inner_product(a,b):
    i = 0; j = 0
    result = 0
    while i < len(a) and j < len(b):
        if a[i][0] == b[j][0]:
            result += a[i][1]*b[j][1]
            i += 1
            j += 1
        elif a[i][0] < b[j][0]:
            i += 1
        else:
            j += 1
    return result

