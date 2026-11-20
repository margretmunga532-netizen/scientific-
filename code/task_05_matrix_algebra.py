"""D. Task 5: Matrix Algebra and Matrix Operations

Modified real-world case: placing a floor plan on a map
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

plan=np.array([[0,0],[12,0],[12,8],[0,8.]])   # floor plan in metres
a=np.deg2rad(30)
R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
S=np.diag([0.5,0.5])
M=np.eye(3)
M[:2,:2]=R@S
M[:2,2]=[5,3]          # homogeneous: rotate, scale, translate
H=np.hstack([plan,np.ones((4,1))])
out=(H@M.T)[:,:2]
print("Homogeneous matrix:\n",np.round(M,4))
print("Plotted points:\n",np.round(out,3))
d=lambda p,q: np.linalg.norm(p-q)
print(f"Original side 0-1: {d(plan[0],plan[1]):.2f} m -> {d(out[0],out[1]):.2f} units")
print(f"Original diagonal 0-2: {d(plan[0],plan[2]):.2f} m -> {d(out[0],out[2]):.2f} units")
