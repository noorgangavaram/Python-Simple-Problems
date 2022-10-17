# FIND THE COUNT FOR THE OCCURRENCE OF A PARTICULAR CHARCTER IN A STRING
# NOOR => O->2

string = input('Enter a string')
print('your string is :',string)
findChar = input('Enter a char')
print('finding char is :',findChar)
add = 0
for i in string:
    if findChar == i:
        add = add+1
print(findChar,'Repeat ->',add,'times')


# THIS IS THE SIMPLE LOGIC
name = input("enter name")
char = input('enter char')

print(name.count(char))