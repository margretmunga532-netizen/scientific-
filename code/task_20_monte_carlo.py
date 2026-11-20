"""S. Task 20: Random Numbers and Monte Carlo Methods

Modified real-world case: server-cluster reliability
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

rng=np.random.default_rng(7)
N=200_000
fails=rng.random((N,5))<0.05
down=(fails.sum(axis=1)>=3)
from math import comb
exact=sum(comb(5,k)*0.05**k*0.95**(5-k) for k in range(3,6))
print(f"System down if >=3 of 5 servers fail (p=0.05 each)")
print(f"Monte Carlo estimate: {down.mean():.5%}")
print(f"Exact binomial probability: {exact:.5%}")
fails2=rng.random((N,5))<0.10
print(f"With p=0.10: {(fails2.sum(axis=1)>=3).mean():.4%}")
pts=rng.random((N,2))
print(f"Pi estimate with {N:,} points: {4*np.mean((pts**2).sum(axis=1)<=1):.4f}")
