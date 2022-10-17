# PROGRAM TO CHECK IF TWO STRINGS ARE ANAGRAMS
# TWO STRINGS ARE SAID TO BE ANAGRAM IF WE CAN FORM THE FIRST STRING BY ARRANGING THE....
# ...CHARACTERS OF ANOTHER STRING
# EX : BASHA , HASBA

string1 = input("Enter 1st name ")
string2 = input('Ennter 2nd name')

if len(string1) == len(string2):
    if (sorted(string1) == sorted(string2)):
        print("These are anagrams")
    else:
        print('These are not anagrams')
else:
    print('These are not anagrams')