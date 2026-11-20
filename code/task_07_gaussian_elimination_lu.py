"""F. Task 7: Gaussian Elimination and LU Decomposition

Modified real-world case: resistive network with five load scenarios
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# 4-node resistive network, conductance matrix G (S), five current-injection scenarios
G=np.array([[ 3.,-1,-1, 0],[-1, 4,-2,-1],[-1,-2, 5,-1],[ 0,-1,-1, 3]])
lu,piv=lu_factor(G)
I=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([1.,1,0,0]),np.array([2.,0,0,1])]
for k,i in enumerate(I,1):
    v=lu_solve((lu,piv),i)
    print(f"Scenario {k}: node voltages =",np.round(v,4),"| residual",f"{np.linalg.norm(i-G@v):.1e}")
