# PROGRAM TO PRINT FIBONACCI SEQUENCE(SERIES)
# 0,1,1,2,3,5,8,13,21,34

num = int(input("Enter a num "))
n1,n2 = 0,1
sum = 0

if num < 0:
    print('Invalid number')
elif num == 1:
    print(n1)
else:
   for i in range(0,num):
       print(sum, end=',')
       n1 = n2
       n2 = sum
       sum = n1 + n2


#  PROGRAM TO PRINT FIBONACCI SEQUENCE(SERIES) USING RECURSSION

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(7))