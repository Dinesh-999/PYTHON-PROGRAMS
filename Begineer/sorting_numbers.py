# sorting the numbers

import numpy as np

a = np.array([34, 5, 89, 23, 76])
print(np.sort(a))   # using numpy inbuilt sort function


def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


print(sorting(a))

b = [34, 5, 89, 23, 76]
c = sorted(b)  # using built in functions
print(c)
