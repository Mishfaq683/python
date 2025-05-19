# json mean that (javascript object notation)
# its is used for storing and transfer data between the browser and server
# api ? two whatsapp user  one user  text is move from  server  to another user the b/w server and user api work is
# joson is text written with javascript object notation
# new app create is use of api to stored data
# python too supports json with a built_in package called json.
# current api develper is here company
# is 6 data type is stored data
# string
# 2 number
# 3 boolean
# 4 object
# 5 null
# 6 array
# the befor user xml is use 
# json is doneted by '{}'
# import json
# p='{"name":"ws","lang":["python","java"]}'
#   json is same of the doctionarystring form 
import json
name=input("enter the name is :")
age=int(input("enter the value is :"))
if age>18:
    print("this is my age:")
else:
    print("this is not my age")
d={
    'name':name ,
    'age':age
}
f=json.dumps(d)
print(type(f))
print(f)