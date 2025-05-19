import json
# cname=input("enter your name pllz:")
# age=int(input("enter the value of age is :"))
x='{"cname":"python","age":"23"}'
y=json.loads(x)
print(type(y))
print(y)

