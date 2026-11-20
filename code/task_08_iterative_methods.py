"""G. Task 8: Iterative Methods for Linear Systems

Modified real-world case: temperature along a heated rod
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
import matplotlib.pyplot as plt

def jacobi(A,b,tol=1e-8,mi=500):
    D=np.diag(A)
    R=A-np.diagflat(D)
    x=np.zeros_like(b)
    er=[]
    for _ in range(mi):
        xn=(b-R@x)/D
        e=np.linalg.norm(xn-x,ord=np.inf)
        er.append(e)
        if e<tol: return xn,er
        x=xn
    return x,er

def gs(A,b,tol=1e-8,mi=500):
    x=np.zeros_like(b)
    er=[]
    for _ in range(mi):
        old=x.copy()
        for i in range(len(b)):
            x[i]=(b[i]-A[i,:i]@x[:i]-A[i,i+1:]@old[i+1:])/A[i,i]
        e=np.linalg.norm(x-old,ord=np.inf)
        er.append(e)
        if e<tol: return x,er
    return x,er

n=7
A=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
b=np.zeros(n)
b[0]=80
b[-1]=30
xj,ej=jacobi(A,b,1e-6)
xg,eg=gs(A,b,1e-6)
print("Rod with 7 interior points (ends 80 C and 30 C)")
print("Gauss-Seidel temperatures:",np.round(xg,3))
print("Direct solution:",np.round(np.linalg.solve(A,b),3))
print("Iterations -> Jacobi:",len(ej),"| Gauss-Seidel:",len(eg))
plt.plot(range(1,n+1),xg,marker='o')
plt.xlabel("Interior point")
plt.ylabel("Temperature (C)")
plt.title("Temperature along a rod")
plt.grid(True)
plt.show()
