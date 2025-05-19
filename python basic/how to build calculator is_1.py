c=int(input('''
    1 + ADD
    2 - SUBTRACTION
    3 * MULTIPLACTION
    4  / DIVSION
      '''))
num1=int(input("enter the number is :"))
num2=int(input("enter the value is"))
opr=input("enter the operator is ")
if opr=='+':
    print(num1+num2)
elif opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
elif opr=='%':
    print(num1%num2)
else:
    print("you have no select the op........................")