"""O. Task 16: Numerical Integration

Modified real-world case: distance from speed readings
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.integrate import simpson

t=np.array([0,30,60,90,120,150,180.])
v=np.array([0,12,18,22,20,10,0.])  # seconds, m/s
print(f"Distance (trapezoid): {np.trapezoid(v,t):.1f} m")
print(f"Distance (Simpson):   {simpson(v,x=t):.1f} m")
print(f"Average speed: {np.trapezoid(v,t)/180*3.6:.2f} km/h")
