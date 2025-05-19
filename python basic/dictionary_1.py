# m={
#     "name":"amjad",
#     "age":"23",
#     "address":"board bazar peshawar "
# }
# print(m)
# print(m["age"])
# for a in m:
#     print(a)
#     print(m[a])
name=input("plz enter your name:")
age=int(input("enter the age is :"))
address=input("enter the address of is:")
if age>=18:
    print("you allowed")
else:
    print("you have not allowed to the funcation is that")
    
    
d={
    "name":name,
  "age":age,
    "address":address
    
}
if d["name"]== name:
    print(name)
elif d["age"] > 18:
     print("most welcome to the party")
elif d["address"] ==address:
     print("you you welcome to party is ")
else:
    print("in pashto we say that ozzza pa izat sara k noor the kharabo ma kha ")

     
     
     
print(d)