# WRITE A PROGRAM TO FIND FACTORIAL OF A NUMBER

num = int(input("Enter a number "))
fact = 1
if num < 0:
    print('number should be greater than 0 ')
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of {} is {} ".format(num,fact))


