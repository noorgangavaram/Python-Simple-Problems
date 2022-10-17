# WRITE A PROGRAM TO CHECK WHETHER A NUMBER IS ARMSTRONG
# ARMSTRONG MEANS 153 => 1^3 + 5^3 + 3^3 = 153

num = int(input("Enter a number "))
add = 0
for i in str(num):                  # converting int to string , beacause int can not be iterable
   #sum = int(i) * int(i) * int(i)  # we do  cube the elements in the num one by one
   #sum = pow(int(i),3)             # this is the power built-in function of python
   sum = int(i)**3                  # THE **  IMPIES THAT "POWER"
   add = add + sum
if num == add:
   print(num," is palindrome")
else:
   print(num,' is not palindrome')



n = int(input('Enter a number '))
cube = 0
while n>0:
   num = n%10
   cube = cube + pow(num,3)
   n = n/10
print(cube)