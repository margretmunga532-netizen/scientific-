"""H. Task 9: Eigenvalues and Eigenvectors

Modified real-world case: office network
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

def centrality(A):
    w,v=np.linalg.eig(A)
    i=np.argmax(w.real)
    d=np.abs(v[:,i].real)
    return w[i].real, d/d.sum()

names=["Router","Server1","Server2","Printer","Laptop"]
A=np.zeros((5,5))
for a,b in [(0,1),(0,2),(0,3),(0,4),(1,2),(2,4)]: A[a,b]=A[b,a]=1
lam,c=centrality(A)
print("Dominant eigenvalue:",round(lam,4))
for n,s in sorted(zip(names,c),key=lambda t:-t[1]): print(f"{n:8s}: {s:.4f}")
