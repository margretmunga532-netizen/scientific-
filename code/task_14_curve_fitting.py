"""M. Task 14: Curve Fitting and Approximation

Modified real-world case: demand forecasting
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

wk=np.arange(1,9,dtype=float)
dem=np.array([120,138,160,185,215,250,290,335.])
ex=lambda x,a,b:a*np.exp(b*x)
p,_c=curve_fit(ex,wk,dem,p0=(100,0.1))
pr=ex(wk,*p)
rm=np.sqrt(np.mean((dem-pr)**2))
print(f"Fitted demand model: y = {p[0]:.2f} * exp({p[1]:.4f} * week)")
print(f"RMSE: {rm:.2f} units")
print(f"Weekly growth factor: {np.exp(p[1]):.4f} (about {100*(np.exp(p[1])-1):.1f}% per week)")
print(f"Forecast week 10: {ex(10,*p):.1f} units")
xp=np.linspace(1,10,200)
plt.scatter(wk,dem,label="Observed demand")
plt.plot(xp,ex(xp,*p),label="Exponential fit")
plt.xlabel("Week")
plt.ylabel("Units sold")
plt.legend()
plt.grid(True)
plt.title("Demand forecasting")
plt.show()
