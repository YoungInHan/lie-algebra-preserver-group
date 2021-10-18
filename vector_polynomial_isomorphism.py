#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sage.all import *
import numpy as np

class vector_polynomial_isomorphism:
    def __init__(self, R, V, indeterminates, d):
        self.R = R
        self.V = V
        N = len(indeterminates)
        i = 0
        elem = 0
        lst = []
        while i < N*d:
            lst.append(indeterminates[elem])
            i += 1
            if i % d == 0:
                elem += 1
        S = Subsets(lst, d, submultiset=True).list()
        self.monomials = [R(np.prod(S[i])) for i in range(binomial(N + d - 1, d))]

    def polynomial_to_vector(self, p):
        if not p in self.R:
            return 0
        coefficient_list = []
        for i in range(len(self.monomials)):
            coefficient_list.append(p.monomial_coefficient(self.monomials[i]))
        return self.V(coefficient_list)

    def vector_to_polynomial(self, v):
        if not v in self.V:
            return 0
        p = 0
        for i, item in enumerate(Sequence(self.monomials)):
            p += v[i]*item
        return self.R(p)

