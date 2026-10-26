num = int(input('Enter the 3 digit number: '))
num1 = num // 100
num2 = (num//10) % 10
num3 = num % 10
if num1 == 2* num2 and num1 == num3/2:
    print('Yes, you have done it.')
else:
    print('Please try next time.')