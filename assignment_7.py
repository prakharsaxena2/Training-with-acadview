#Importing numpy module
import numpy

# Question 1
#Creating numpy array with 10 elements
np = numpy.random.rand(10,1)
#printing numpy Array
print(np)
#Printing mean
print(numpy.mean(np))

'''Q2'''
arr = numpy.random.rand(20, 1)
print(arr)
#Printing Variance of array
print("Variance of array is: ", numpy.var(arr))
#Printing tandard deviation of array
print("Standard deviation of array is: ", numpy.std(arr))

'''Q3'''
a = numpy.random.rand(10,20)
b = numpy.random.rand(20,25)
print("Matrix A is: ", a)
print("Matrix B is: ", b)
#Creating new matrix by matrix multiplication of A and B
c = numpy.matmul(a , b)
print("Matrix Multiplication of A and B is: ", c)
#Printing Sum of elements of New matrix
print("Sum of elements of New Matrix is: ", numpy.sum(c))

'''Q4'''
ary = numpy.random.rand(10, 1)
print(ary)
#Creating new array
func = 1/(1+numpy.exp(-ary))
print("New array: \n",func)