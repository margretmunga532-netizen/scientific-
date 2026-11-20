"""K. Task 12: Polynomial and Nonlinear Equation Solving

Modified real-world case: overlapping cell-tower coverage
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.optimize import root

# Two cell towers: T1 at (0,0) radius 5 km; T2 at (6,0) radius 4 km. Where do coverage edges meet?
eq=lambda z:[z[0]**2+z[1]**2-25,(z[0]-6)**2+z[1]**2-16]
for g in ([3.,3.],[3.,-3.]):
    s=root(eq,g)
    print("Guess",g,"-> boundary intersection (km):",np.round(s.x,5),"| residuals",np.round(eq(s.x),10))
