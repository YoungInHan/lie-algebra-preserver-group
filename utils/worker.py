#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def worker(start, end):
    E_action_fl = [[0 for j in range(N)] for i in range(N)]
    for l in range(start, end):
        print(l)
        grad_fl = vp_iso.vector_to_polynomial(W.gen(l)).gradient()
        for i in range(N):
            for j in range(N):
                E_action_fl[i][j] = sparsify(vp_iso.polynomial_to_vector(E_action(i,j,grad_fl)))
        for k in range(q):
            for i in range(N):
                for j in range(N):
                    M_f[(q*l) + k,(N*i) + j] = sparse_inner_product(E_action_fl[i][j], g_sparse[k])

