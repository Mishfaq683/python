# l=[]
# # for a in range(1,10):
#     l.append(a)
#     print('2*','','=',a*2)
# n=[c for c in range(1,34) if c%2==0  ]
# print(n)
# n=int(input("enter the value "))
# m=(n for n in range(n) if n%2==0)
# print(m)
# ******************* list funcation ************************
# l=[10,20,30]
# del l[1]
# print(l)
# print(l.pop(2))
# print(l)
l=[20,30,40,50,60]
# l.remove(40)
# print(l)
# l.clear()
# print(l)
# l.insert(0,10) # the insert methed is different the only value insert length of the list
# l.insert(8,80)
n=[80,90]
# l.append(n)
l.extend(n)


print(l)