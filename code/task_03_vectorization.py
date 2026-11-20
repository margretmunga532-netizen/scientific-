"""B. Task 3: Mathematical Functions and Vectorization

Modified real-world case: VAT on retail transactions
Source: BIT2118_Group_Work_Tasks_A-S.docx
"""

import numpy as np

rng = np.random.default_rng(1)
gross = rng.uniform(50, 20000, 1_000_000)      # KES
net = gross/1.16
vat = gross-net
print(f"Total gross: KES {gross.sum():,.2f}")
print(f"Total net (ex-VAT): KES {net.sum():,.2f}")
print(f"Total VAT: KES {vat.sum():,.2f}")
print(f"VAT share of gross: {vat.sum()/gross.sum():.4%}")
