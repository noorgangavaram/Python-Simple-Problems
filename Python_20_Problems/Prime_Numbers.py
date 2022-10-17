# WRITE A PROGRAM TO PRINT PRIME NUMBERS FROM 1 TO 100
# PRIME NUMBER => a number that is divisible only by itself and 1
# 2,3,5,7,11,13
# 1 is not prime number

n = 100

for i in range(2,101):
    for j in range(2,i):
        if (i%j==0):
            brea

"""""
=> THE ELSE BLOCK JUST AFTER FOR/WHILE IS EXECUTED ONLY WHEN THE LOOP IS 'NOT' TERMINATED BY A BREAK STATEMENT

for i in range(1,10):
    print(i)
    if i==5:
     break
else:
    print('else statement')
"""