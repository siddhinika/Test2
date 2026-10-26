year=int(input('Enter the Year:'))
if (year % 4 == 0):
    print('The Year is Leap Year.')
elif (year % 100 == 0):
    print('Not a leap year.')
elif (year % 400 == 0):
    print('The year is leaf year.')
else:
    print('Not a leap year.')