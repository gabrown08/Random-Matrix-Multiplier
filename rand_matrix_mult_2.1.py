#random matrix multiplier 2.1
#by Greg Brown
#7/15/2019

#import modules
import random
import datetime

#use current time to randomize seed
time = str(datetime.datetime.now())
seed = int(time[17:19] + time[14:16] + time[11:13] + time[8:10] + time[5:7] + time[0:4])
random.seed(seed)

#print seed
print()
print('seed ', seed)
print()

#define dimensions of matrices
m = random.randint(1, 15)
n = random.randint(1, 15)
p = random.randint(1, 15)

#generate a random m by n matrix as a
a = [[random.randint(-9, 9) for i in range(n)] for j in range(m)]

#generate a random n by p matrix as b
b = [[random.randint(-9, 9) for i in range(p)] for j in range (n)]

#print a
print('matrix a =')
for i in a:
	print(i)
print()

#print b
print('matrix b =')
for i in b:
	print(i)
print()

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
#print()

#calculate product of a and b by pairing rows in a with rows in b transpose (columns of b)
product = [[sum([a * b for a, b in zip(a[i], B[j])]) for j in range(len(B))] for i in range(len(a))]

#print product matrix
print('a * b = ')
for i in product:
	print(i)
print()
	
#ask user to save results
s = input("enter 'save' to log the results in a text file in the current working directory. ")
if s == 'save':

        #open file and write datetime
        file = open("rand_matrix_mult_log.txt", "a+")
        time = str(datetime.datetime.now())
        file.write("-------------------\n")
        file.write(time[0:19])
        file.write("\n")
        file.write("\n")
        
        #write matrix a to file
        file.write("matrix a =\n")
        for i in a:
                file.write(str(i) + "\n")
        file.write("\n")

        #write matrix b to file
        file.write("matrix b =\n")
        for i in b:
                file.write(str(i) + "\n")
        file.write("\n")

        #write product matrix to file
        file.write("a * b =\n")
        for i in product:
                file.write(str(i) + "\n")
        file.write("\n")
        file.write("\n")

        #close file
        file.close()

        print()
        print("file saved as 'rand_matrix_mult_log.txt' in current working directory.")
