# CALCULATE THE NUMBER OF VOWELS AND CONSTANTS IN A STRING
# VOWELS => a,e,i,o,u

string = input('Enter a string')

vowels = ['a','e','i','o','u']
vowelsCount = 0
consonatsCount =0

for char in string:
    if char in vowels:
        vowelsCount = vowelsCount+1
    else:
        consonatsCount =consonatsCount+1

print('Number of Vowels : {} , Nmber of Consonants : {}'.format(vowelsCount,consonatsCount))