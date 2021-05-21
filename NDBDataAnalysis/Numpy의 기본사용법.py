import numpy as np
array = np.array([1,2,3])
print(array)
print(array.size)
print(array.dtype)
print(array[2])

# 0~3까지 배열 만들기
array1 = np.arange(4)
print(array1)

#0으로 초기화
array2 = np.zeros((4,4), dtype=float)
print(array2)

#1로 초기화
array3 = np.ones((3,3), dtype=str)
print(array3)

# 0~9 랜덤하게 초기화된 배열 만들기
array4 = np.random.randint(0,10,(3,3))
print(array4)


array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)

print(array)
print(left.shape)
print(left)
print(right.shape)
print(right)
print(right[1][1])