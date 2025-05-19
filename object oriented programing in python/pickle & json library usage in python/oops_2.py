# methode through call the object 
# constuctor is automatically call
# 
class Demo:
    # num1=int(input("enter the number is :"))
    # num2=int(input("enter the value of second number is :"))
    def sumvalue(self ,a,b):
           self,num1=int(input("enter the number is :"))
           self,num2=int(input("enter the value of second number is :"))
           print(a+b)
        
obj=Demo()
obj.sumvalue(12,22)