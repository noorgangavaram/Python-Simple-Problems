# PROGRAM TO DETERMINE THE FACTORS OF A NUMBER
# FACTORS OF 8 ARE 1,2,4,8

n = int(input('enter a number'))

for i in range(1,n+1):
    if(n%i == 0):
        print(i)
