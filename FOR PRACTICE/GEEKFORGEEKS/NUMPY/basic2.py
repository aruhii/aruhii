import numpy as np

arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]])

print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)

c = np.zeros((3,4))
print(c)
d = np.full((4,4),5,dtype=np.int64)
print(d)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

print(arr.max())
print(arr.max(axis=1))
print(arr.itemsize)
print(arr.newbyteorder())

# 생성할때는 항상 np.array([~~~]) 하거나 , np.arange(1,10).reshape(3,3) 같은 식으로 하자
