# REVERSE A NUMBER
# EX: 263 => 362

# THIS IS ONE OF THE EXAMPLE OF THE REVERSE A NUMBER

num = 845
convert = str(num)
reverse = convert[::-1]
print(reverse)

# THIS IS THE MAIN EXAMPLE OF THE REVERSE A NUMBER
# 346
n = int(input('Enter a number'))
reverse1 = 0
while(n>0):
    number = num % 10
    reverse1 = reverse1*10 + number
    n = n//10

print(reverse1)






