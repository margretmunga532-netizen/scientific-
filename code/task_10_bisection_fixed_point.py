"""I. Task 10: Root Finding: Bisection and Fixed-Point Methods

Modified real-world case: break-even production
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

f=lambda q:50*q-(2000+20*q+0.05*q**2)
s=root_scalar(f,bracket=[0,200],method="bisect",xtol=1e-8)
print(f"Lower break-even quantity: {s.root:.4f} units")
s2=root_scalar(f,bracket=[300,700],method="bisect",xtol=1e-8)
print(f"Upper break-even quantity: {s2.root:.4f} units")
print(f"Maximum profit near q = 300: {f(300):.2f}")
q=np.linspace(0,600,400)
plt.plot(q,f(q))
plt.axhline(0,lw=.8)
plt.axvline(s.root,ls='--')
plt.axvline(s2.root,ls='--')
plt.xlabel("Units produced")
plt.ylabel("Profit (KES)")
plt.title("Break-even points")
plt.grid(True)
plt.show()
