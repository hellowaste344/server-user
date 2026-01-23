import cupy as cp
import numpy as np

print(cp.__version__)   
x_cpu = np.array([1,2,3])
x_gpu = cp.array([1,2,3])

ln_cpu = np.linalg.norm(x_cpu)
ln_gpu = cp.linalg.norm(x_gpu)

print("Using NumPu: ", ln_cpu)
print("\nUsing Cupy: ", ln_gpu)