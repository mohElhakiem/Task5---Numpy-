import numpy as np


A = [10,20,30,40,50]
B = [5,4,3,2,1]
A = np.array(A)
B = np.array(B)
print (A)
print (B)

SUM = A + B
print(SUM)

Subtract = A - B
print(Subtract)

Multiply = A * B
print(Multiply)

Divide = A / B
print(Divide)


Max = A.max()
Min = A.min()
Mean = A.mean()

print(Max)
print(Min)
print(Mean)

dotProduct = np. dot(A,B)

print(dotProduct)

reshaped_A = A.reshape(5,1)

print(reshaped_A)


