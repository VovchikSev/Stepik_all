
in_str = "-1., 2.5, -3, 4.9, 5.5, -6, -7.0, 8.8, -9, 10, 11, 12, 13, -14.5"
import numpy as np
lst = list(map(float, in_str.split(", ")))
print(lst)
V1 = np.array(lst)
V2 = np.array([lst[-2]])
V3 = np.array(lst[::-1])
V4 = np.array(lst[::-2])
V5 = np.arange(len(lst))

print(V1.dtype(), V1)
