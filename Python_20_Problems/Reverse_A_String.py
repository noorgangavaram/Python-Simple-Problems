# PYTHON PROGRAM TO REVERSE A STRING
# WE CAN USE "SLICING IN-BUILT PYTHON FEATURE" TO DO THIS TASK
string = input('Enter somethong to reverce')
print(string)
#print(string[::-1])  # THIS IS SLICING IN-BUILT PYTHON FEATURE

# HERE WE DON' USE THE BUILT-IN FEATURE TO DO THIS TASK
# BUT WE WRITE OUR OWN CODE TO DO THIS TASK

print('Before revercing : ',string)
reverce = ''
for letters in string:
    reverce = letters + reverce
print('After revercing : ',reverce)