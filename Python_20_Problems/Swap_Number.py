# PROGRAM TO SWAP NUMBERS USING TEMPORARY VARIABLE

a = 10
b = 23
print("before swaping")
print("a = {} , b = {}".format(a,b))
temp = a
a = b
b = temp
print("after swaping")
print("a = {} , b = {}".format(a,b))

# PROGRAM TO SWAP NUMBERS WITHOUT USING TEMPORARY VARIABLE
a = 21
b = 23
a = a+b
b = a-b
a = a-b
print('this is another example of swap')
print("a = {} , b = {}".format(a,b))