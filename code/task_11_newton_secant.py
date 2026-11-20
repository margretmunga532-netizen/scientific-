"""J. Task 11: Root Finding: Newton–Raphson and Secant Methods

Modified real-world case: true interest rate of a loan
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

from scipy.optimize import root_scalar

def make_npv(cf):
    npv=lambda r:sum(c/(1+r)**t for t,c in enumerate(cf))
    d=lambda r:sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cf) if t>0)
    return npv,d

cf=[100000]+[-14000]*8       # receive loan, repay 8 monthly instalments
npv,_d=make_npv(cf)
s=root_scalar(npv,x0=0.01,x1=0.05,method="secant",xtol=1e-12)
m=s.root
print(f"Monthly rate: {m:.6%}")
print(f"Nominal annual rate (x12): {12*m:.4%}")
print(f"Effective annual rate: {(1+m)**12-1:.4%}")
print(f"Total repaid: {14000*8}, total interest: {14000*8-100000}")
