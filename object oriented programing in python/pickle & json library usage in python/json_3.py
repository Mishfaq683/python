import json
name=input("enter the name is :")
age=int(input("enter the age is:"))
if age>18:
    print("the come to the party")
else:
    print("not allow ")
d={"name":name,"age":'agte'}
x=json.dumps(d)
print(x)