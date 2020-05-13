# In Numpy, number of dimensions of the array is called rank of the array
# A tuple of integers giving the size of the array along each dimension is known as shape of the array

import numpy as np

arr1 = np.array([1.0,2.0], dtype=np.int64)

ar = np.array([[1,2,3],
                [4,5,6]])
ak = np.array([[1,2,3],
                [4,5,6]])

arr5 = np.array([[2,2,3],
                [1,5,7]])

arr3 = np.array((1,2,3))

arr4 = np.array([[-1, 2, 0, 4,5],
                [4, -0.5, 6, 0,4],
                [2.6, 0, 7, 8,6],
                [3, -7, 4, 2.0,4]])

sliced = arr4[:4, ::2]

arr = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                [[7, 8, 9],
                 [10, 11, 12]]])

print(arr1.dtype)


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[4, 3],
              [2, 1]])

print(a+b)

print(np.add(a,b))
print(ar+ak)
print(dir(np))