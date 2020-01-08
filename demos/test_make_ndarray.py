"""
1. 生成 ndarray
"""
import numpy as np

data01 = [6, 7.5, 0, 9, 3]
arr01 = np.array(data01)

data02 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr02 = np.array(data02)

arr03 = np.zeros((3, 4))

arr04 = np.ones((3, 4))

arr05 = np.ones_like(arr01)


print("arr01\n", arr01)
print("arr02\n", arr02)
print("arr03\n", arr03)
print("arr04\n", arr04)
print("arr05\n", arr05)
