"""E. Task 6: Solution of Systems of Linear Equations

Modified real-world case: two-loop electrical circuit
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

# Mesh currents: 10 I1 - 4 I2 = 12 ; -4 I1 + 9 I2 = -6   (ohms, volts)
A=np.array([[10.,-4],[-4,9]])
b=np.array([12.,-6])
I=np.linalg.solve(A,b)
print("Mesh currents I1, I2 (A):", I)
print("Current through shared 4-ohm resistor (I1-I2):", I[0]-I[1])
print("Residual norm:", np.linalg.norm(b-A@I))
