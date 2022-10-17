#PYTHON PROGRAM TO PRINT SUM OF 1 TO N NUMBERS

num = int(input('Enter n value'))
print("Entered value is ",num)
sum = 0
for i in range(1,num+1):
    sum = sum+i
    print(i,'+ ',end='')
print('= ',sum)