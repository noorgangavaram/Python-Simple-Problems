# FIND THE LEAP YEAR

"""
 LEAP YEAR HAS 366 DAYS
 IT COMES AFTER EVERY FOUR YEARS

 CONDITIONS:
    1.A YEAR WHICH IS DIVISIBLE BY 400.
    2.A YEAR DIVISIBLE BY 4 BUT NOT BY 100
     THEN ITS A LEAP YEAR

    OTHERWISE IT IS NOT A LEAP YEAR

"""
# BY OUR OWN LOGIC
def is_leap(year):
    if year % 400 == 0 or year%4 == 0 and year%100 != 0 :
       print('leap year')
    else:
        print('not leap year')

year = int(input('enter a year'))
is_leap(year)


# BY USING BUILT IN FUNCTIONS
import calendar

if calendar.isleap(2012):
    print('leap year')
else:
    print('not leap year')
