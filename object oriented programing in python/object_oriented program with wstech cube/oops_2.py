# class Number_checker:
#     def nomber(self,num):
#         if num>0:
#             return "the positive nos"
#         elif num<0:
#             return "the is negative number is "
#         elif num==0:
#             return 'this is zero number is :'
# object1=Number_checker()
# print(object1.nomber(5))
# print(object1.nomber(-2))
# print(object1.nomber(0))
# class vote:
#     def checker_voter(self,age):
#         if age<18:
#             return'your are not eligible for voting '
#         elif 18<age<60:
#             return 'you are eligible for voting plz:'
#         elif age>60:
#             return 'your are expired dear'
# object2=vote()
# print(object2.checker_voter(12))
# print(object2.checker_voter(78))
# print(object2.checker_voter(20))
# class bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
        
        
#     def withdraw(self,amount):
#             if amount<=self.balance:
#                 self.balance-=amount
#                 return f"the balance is successful transfer:new balance:{self.balance}"
#             else:
#                 print('insuffcient is :')
# bk=bankaccount(1000)
# print(bk.withdraw(1111))        
# class validtorspassword:
#     def validtor_spassword(self,password):
#         if len(password)<8:
#             return "your password is incorrect:password at least is 8 words"
#         elif not any(char.isdigit() for char in password):
#             return 'the password cotain at least one number:'
#         elif not any(char.isupper()for char in password):
#             return 'the password contain at least one is capital latter :'
#         # elif not any(char .isspecial()for char in password):
#             # return 'the contain one special character is :'
# vs=validtorspassword()
# print(vs.validtor_spassword('Password12'))
# print(vs.validtor_spassword('Asad123'))
# print(vs.validtor_spassword('AS@12'))

# class PasswordValidator:
#     def validate_password(self, password):
#         if len(password) < 8:
#             return "Invalid password. Must be at least 8 characters."
#         elif not any(char.isdigit() for char in password):
#             return "Invalid password. Must contain at least one number."
#         elif not any(char.isupper() for char in password):
#             return "Invalid password. Must contain at least one uppercase letter."
#         else:
#             return "Valid password."

# # Create an object and test
# validator = PasswordValidator()
# print(validator.validate_password("Short1"))       # Output: Invalid password. Must be at least 8 characters.
# print(validator.validate_password("password1"))    # Output: Invalid password. Must contain at least one uppercase letter.
# print(validator.validate_password("Password123"))  # Output: Valid passwor
