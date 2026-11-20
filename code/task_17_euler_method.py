"""P. Task 17: Ordinary Differential Equations: Euler Method

Modified real-world case: logistic population growth
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
import matplotlib.pyplot as plt

r,K,P0,h=0.4,1000.0,50.0,1.0
t=np.arange(0,31,h)
P=np.zeros_like(t)
P[0]=P0
for i in range(len(t)-1): P[i+1]=P[i]+h*r*P[i]*(1-P[i]/K)
ex=K/(1+(K-P0)/P0*np.exp(-r*t))
print(f"Logistic growth, r=0.4, K=1000, P0=50, h=1")
for d in (0,5,10,15,20,30): print(f"day {d:2d}: Euler {P[d]:.1f}, exact {ex[d]:.1f}")
plt.plot(t,P,marker='o',ms=3,label="Euler")
plt.plot(t,ex,label="Exact")
plt.axhline(K,ls=':')
plt.xlabel("Day")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.title("Logistic growth")
plt.show()
