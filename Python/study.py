import numpy as np

a = [1,2,3]
b = np.array(a)
print(b)
print(type(b))
print(b.shape)

d = np.array([[1,2],[1,2],[1,2]])
print(d)
print(d.shape)

# array의 성분을 실수형으로 정의
a = np.array([1,2,3,4], float)
print(a)
print(a.dtype)

c = np.array([[1,2,3],[4,5,6]])
print(c[0,0])
print(c[0,1])
print(c[0,:])
print(c[:2])

mylist = [[1,2,3],[3,4,5]]
myarray = np.array(mylist)
print(myarray)
print(myarray.shape)
print("First row : %s " % myarray[0])
print("Last row : %s " % myarray[-1])
print("Specific row and col : %s " % myarray[0, 2])
print("Whole col : %s" % myarray[:2])

a = np.array([1,2])
b = np.array([3,4])

print(a+b)
print(a%b)

a = np.array([1,2,3])
b = np.array([[0],[4],[2]])

print(a)
print(b)
print(a+b)
print("\n")

a = np.ones(([2,2]))
a[0][0] = -1
a[0][1] = 6
print(a)

a = np.abs(a)
print(a)
print(np.sqrt(a))

import math
c = np.array([math.e, 1,2])
print(c)

c = np.log(c)
print(c)

d = np.array([1.1, 1.5, 1.8])
print(np.floor(d)) # 내림
print(np.ceil(d)) # 올림
print(np.rint(d)) # 반올림

a = np.array([1,2,3])
for x in a:
    print(x)

a = np.array([1,2,3,4,5])
#합
print('sum')
print(a.sum())

#곱
print('production')
print(b.prod())

#최소값과 인덱스
print('min and Index')
print(a.min())
print(a.argmin())

#평균과 표준편차
print('mean')
print(a.mean())
print('standard deviation')
print(a.std())

#매트릭스 트랜스포즈
a = np.array([[1,2],[3,4],[5,6]])
print(a)

a_prime = a.T
print(a_prime)

b = np.array([1,2,3,4])
print(b)

b_prime = b.reshape(-1,1)
print(b_prime)
print(b.shape, ' ==> ', b_prime.shape)

