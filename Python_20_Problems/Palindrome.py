# WRITE A PROGRAM TO CHECK WHETHER A STRING IS PALINDROME OR NOT

string = input("enter string to check ")
print("Original string is : ",string)
palindrome = string[::-1]
print("Reverse string is : ",palindrome)
if string == palindrome:
    print('palindrome ')
else:
    print('not palindrome')
