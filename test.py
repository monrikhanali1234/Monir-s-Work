age = int(input('Wrte down your age: '))
aex = input('Wrte down your Gender: ')
day = int(input("Input day : "))


if (age >= 18 and age<30) and aex.upper()=='M':
	wage = 700*day
	print(wage)
elif (age >= 18 and age<30) and aex.upper()=='F':
	wage = 750*day
	print(wage)
elif (age >= 30 and age<40) and aex.upper()=='M':
	wage = 800*day
elif age >= 18 and age<30 and aex.upper()=='F':
	wage = 850*day
	print(wage)
else:
	print("error")

month = int(input('Enter number of month(1-12):'))
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if 1<=month<=12:
	print(f'{months[month-1]} has {days[month-1]} days')
else:
	print('Invalid input')

percent = float(input('Enter percentage:'))
if percent<40:
	print('Failed')
elif percent<55:
	print('Fair')
elif percent<65:
	print('Good')
else:
	print('Excellent')


a = float(input('Enter first number:'))
b = float(input('Enter second number:'))
operator = input('Enter operator(+, -, *, /)')

if operator=='+': result = a+b
elif operator=='-': result = a-b
elif operator=='*': result = a*b
elif operator=='/': result = a/b
print(f'Result:{result}')


age = int(input('Wrte down your age: '))
aex = input('Wrte down your Gender: ')
day = int(input("Input day : "))


if (age >= 18 and age<30) and aex.upper()=='M':
	wage = 700*day
	print(wage)
elif (age >= 18 and age<30) and aex.upper()=='F':
	wage = 750*day
	print(wage)
elif (age >= 30 and age<40) and aex.upper()=='M':
	wage = 800*day
elif age >= 18 and age<30 and aex.upper()=='F':
	wage = 850*day
	print(wage)
else:
	print("error")