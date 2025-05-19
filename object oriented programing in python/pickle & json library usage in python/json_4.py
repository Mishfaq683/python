import json
name=input("enter the name :")
age=int(input("enter the age is :"))
d={'name':name,'age':age}
b=json.dumps(d)
print(b)
 