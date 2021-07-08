import numpy as np
import math
n=100
y_cap=np.random.rand(n)
y=np.random.randint(0,2,(n))
loss = 0
loss = (-1/n)*np.sum(y*np.log2(y_cap)+(1-y)*np.log2(1-y_cap))
print(loss)  