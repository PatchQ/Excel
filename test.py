import numpy as np
import pandas as pd

a = list(range(1,2022,4))
b = list(range(-3,-2020,-4))
ans1 = 0
ans2 = 0


for i in a:
    ans1 = ans1+i

for i in b:
    ans2 = ans2+i

print(ans1+ans2)
print(ans1)
print(ans2)
