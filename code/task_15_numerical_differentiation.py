"""N. Task 15: Numerical Differentiation

Modified real-world case: acceleration from velocity data
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

t=np.array([0,2,4,6,8,10.])
v=np.array([0,5,12,20,27,31.])  # m/s
a=np.gradient(v,t)
print("Acceleration estimates (m/s^2):",np.round(a,3))
print(f"Peak acceleration {a.max():.2f} m/s^2 at t = {t[a.argmax()]:.0f} s")
