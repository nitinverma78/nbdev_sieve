# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_sieve.ipynb.

# %% auto 0
__all__ = ['sieve']

# %% ../nbs/00_sieve.ipynb 3
from fastcore.utils import *

# %% ../nbs/00_sieve.ipynb 4
def sieve(N=10):
    "sieve of Eratosthenes"
    N = int(N)
    prime = [True]*(N+1)
    for i in range (2,N+1):
        if prime[i]:
            yield (i)
            for j in range(i*i,N+1,i):
                prime[j] = False
