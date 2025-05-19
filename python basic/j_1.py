import json
# name=input('enter the your name is ')
# age=int(input('enter the age is'))
d='[{"name":"ishfaq","age":"23" }]'
f=json.loads(d)
print(type(f))
for a in d:
    print(a,d[a])
print(f)