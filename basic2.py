def fun():
    print("bro")
fun()
bro
def ad(a,b):
    c = a + b
    return c
ad(4,7)
11
a=[2,4,6,7,5]
print(a)
[2, 4, 6, 7, 5]
b="python full stack dev"
b.split()
['python', 'full', 'stack', 'dev']
b="python,full,stack,dev"
ab=b.split(",")

print(ab)
['python', 'full', 'stack', 'dev']
ab[0]
'python'
k=[1,2,3,4,5]
for i in k:
    print(i)
1
2
3
4
5
for m in range (10,14):
    print(m)
10
11
12
13
for p in range (10,1,-1):
    print(p)
5
4
3
2
list1=[]
t=int(input("enter the size array"))
for i in range(0,t):
    i=input("enter the value")
    list1.append(i)
enter the size array4
enter the value2
enter the value5
enter the value7
enter the value9
list1
['2', '5', '7', '9']
import math
r=int(input("enetr radius"))
l=math.pi*r*r
print(l)
enetr radius4
50.26548245743669
import numpy as np
a=np.array([1,2,3])
a
array([1, 2, 3])
z=np.zeros((2,3))
z
array([[0., 0., 0.],
       [0., 0., 0.]])
r=np.arange(0,10,2)
r
array([0, 2, 4, 6, 8])
b=np.array([4,5,6])
a+b
array([5, 7, 9])
np.mean(a)
2.0
np.max(a)
3
c=np.array([
    [1,2],
    [3,4]
])
c
array([[1, 2],
       [3, 4]])
d=np.array([
    [4,8],
    [6,9]
])
c+d
array([[ 5, 10],
       [ 9, 13]])
e=c*d
e
array([[ 4, 16],
       [18, 36]])
f=np.dot(c,d)
f
array([[16, 26],
       [36, 60]])
c.T
array([[1, 3],
       [2, 4]])
c
array([[1, 2],
       [3, 4]])
d
array([[4, 8],
       [6, 9]])
f
array([[16, 26],
       [36, 60]])
f.T
array([[16, 36],
       [26, 60]])
print("\n metrix 1:n",c)
print("\n metrix 2:n",d)
print("\n addition:n",c+d)
print("\n substraction 1:n",c-d)
print("\n multiplication element wise:n",c*d)
print("\n multiplication row X column:n",f)
print("\n Transpose:n",f.T)
 metrix 1:n [[1 2]
 [3 4]]

 metrix 2:n [[4 8]
 [6 9]]

 addition:n [[ 5 10]
 [ 9 13]]

 substraction 1:n [[-3 -6]
 [-3 -5]]

 multiplication element wise:n [[ 4 16]
 [18 36]]

 multiplication row X column:n [[16 26]
 [36 60]]

 Transpose:n [[16 36]
 [26 60]]
