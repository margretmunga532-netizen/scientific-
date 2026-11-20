"""L. Task 13: Interpolation

Modified real-world case: missing soil-moisture reading
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

day=np.arange(1,11,dtype=float)
sm=np.array([32,30.5,29,np.nan,26.5,25,24.5,30,29.5,28])
ok=~np.isnan(sm)
lin=interp1d(day[ok],sm[ok])
cub=CubicSpline(day[ok],sm[ok])
print(f"Soil moisture on missing day 4: linear {float(lin(4)):.2f} %, cubic spline {float(cub(4)):.2f} %")
dd=np.linspace(1,10,200)
plt.scatter(day[ok],sm[ok],label="Measured")
plt.plot(dd,lin(dd),label="Linear")
plt.plot(dd,cub(dd),label="Cubic spline")
plt.scatter([4],[float(cub(4))],marker='x',s=80,c='k',label="Estimate, day 4")
plt.xlabel("Day")
plt.ylabel("Soil moisture (%)")
plt.legend()
plt.grid(True)
plt.title("Estimating a missing reading")
plt.show()
