"""R. Task 19: Numerical Optimization

Modified real-world case: minimum-cost vehicle fleet
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.optimize import minimize

def optimise(cA=12,cB=18,kA=100,kB=170,req=1000):
    s=minimize(lambda z:cA*z[0]+cB*z[1],x0=[5,3],method="SLSQP",bounds=[(0,None),(0,None)],constraints={"type":"ineq","fun":lambda z:kA*z[0]+kB*z[1]-req})
    best=None
    for a in range(0,40):
        for b in range(0,40):
            if kA*a+kB*b>=req:
                c=cA*a+cB*b
                if best is None or c<best[0]: best=(c,a,b,kA*a+kB*b)
    return s,best

# Matatus: 14 seats, KES 8000/day; buses: 33 seats, KES 15000/day; need >= 200 seats
s,b=optimise(cA=8000,cB=15000,kA=14,kB=33,req=200)
print(f"Continuous: matatus {s.x[0]:.3f}, buses {s.x[1]:.3f}, cost {s.fun:.0f}")
print("Integer (cost, matatus, buses, seats):",b)
print("Cost per seat: matatu",round(8000/14,1),"| bus",round(15000/33,1))
