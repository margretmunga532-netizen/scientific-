"""Q. Task 18: Numerical Solution of ODEs Using SciPy

Modified real-world case: SIR epidemic model
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

beta,gamma,N=0.4,0.1,10000.0
def sir(t,y):
    S,I,Rr=y
    return [-beta*S*I/N,beta*S*I/N-gamma*I,gamma*I]
s=solve_ivp(sir,(0,160),[N-10,10,0],t_eval=np.linspace(0,160,641),rtol=1e-8)
I=s.y[1]
print(f"SIR model, N=10000, beta=0.4, gamma=0.1, R0={beta/gamma:.1f}")
print(f"Peak infections: {I.max():.0f} at day {s.t[I.argmax()]:.1f}")
print(f"Total ever infected: {N-s.y[0,-1]:.0f} ({(N-s.y[0,-1])/N:.1%})")
s2=solve_ivp(lambda t,y:[-0.2*y[0]*y[1]/N,0.2*y[0]*y[1]/N-gamma*y[1],gamma*y[1]],(0,160),[N-10,10,0],t_eval=np.linspace(0,160,641),rtol=1e-8)
print(f"With beta=0.2 (distancing): peak {s2.y[1].max():.0f} at day {s2.t[s2.y[1].argmax()]:.1f}")
plt.plot(s.t,s.y[0],label="Susceptible")
plt.plot(s.t,s.y[1],label="Infected")
plt.plot(s.t,s.y[2],label="Recovered")
plt.plot(s2.t,s2.y[1],ls='--',label="Infected (beta=0.2)")
plt.xlabel("Day")
plt.ylabel("People")
plt.legend()
plt.grid(True)
plt.title("SIR epidemic model")
plt.show()
