# l=[10,20,30,[56,67,78]]
# l[2]='hello'
# print(l[-3::-1])
l=[10,20,30,40,'hello',[23,34,67]]
# print(l[:3:])
j=len(l)
print(j)
for a in range(j-1,-1,-2):
    print(l[a])
    