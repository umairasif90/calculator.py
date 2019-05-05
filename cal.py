print('enter 1 for addition\nenter 2 for multiplication\nenter 3 for subtraction\nenter 4 for division')
c = int(input("please enter number:"))
number1 = int(input('give us a number '))
number2 = int(input('give us second number '))
if   c == '1':
        print(number1 + number2)
elif c == '2':
        print(number1 * number2)
elif c == '3':
        print(number1 - number2)
elif c == '4':7
        print(number1 / number2)
else:
        print('invalid number')