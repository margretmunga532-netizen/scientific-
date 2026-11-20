"""C. Task 4: Floating-Point Arithmetic and Numerical Errors

Modified real-world case: adding money in a banking system
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import math

total=0.0
for _ in range(1_000_000): total+=0.10
print(f"Naive sum of 1,000,000 x KES 0.10: {total!r}")
print(f"math.fsum:                         {math.fsum([0.10]*1_000_000)!r}")
print(f"Naive error: {abs(total-100000):.10f}")
print("Naive == 100000 ?", total==100000, "| isclose:", math.isclose(total,100000))
from decimal import Decimal
print("Decimal sum:", sum(Decimal('0.10') for _ in range(1_000_000)))
