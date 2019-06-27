#random matrix multiplier 2
#by Greg Brown
#6/26/2019

import random

m = random.randint(1, 15)
n = random.randint(1, 15)
p = random.randint(1, 15)

#generate a random m by n matrix as a
a = [[random.randint(-9, 9) for i in range(n)] for j in range(m)]

#generate a random n by p matrix as b
b = [[random.randint(-9, 9) for i in range(p)] for j in range (n)]

#print a
print('matrix a =')
for i in range(len(a)):
	print(a[i])
	
print()

#print b
print('matrix b =')
for i in range(len(b)):
	print(b[i])

#generate blank matrix for b transpose
B = [[0 for i in range(n)] for j in range(p)]

#generate b transpose
for i in range(p):
	for j in range(n):
		B[i][j] = b[j][i]				

#print b transpose		
#print()
#
#print('b transpose =')
#for i in range(len(B)):
#	print(B[i])					

#calculate product of a and b by pairing rows in a with rows in b transpose (columns of b)
product = [[sum([a * b for a, b in zip(a[i], B[j])]) for j in range(len(B))] for i in range(len(a))]

print()

#print product matrix
print('a * b = ')
for i in range(len(product)):
	print(product[i])

#close on enter
input()
	
