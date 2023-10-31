#!/usr/bin/env python3
# Python program to display the Fibonacci sequence
# by using recursion.

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = (int(input("Enter the number of terms you want: ")))

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# by using loop
'''
num = int(input("Enter any number: "))
n1, n2 = 0, 1
sum = 0
if num<=0:
    print('please enter number greater then 0')
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
'''