# define the methode i
# name="ishfaq-khan!"
# a=10
# b=10.5
# print(dir(name))
# print(name.__add__)
# print(name.strip('-'))
# /
# print(dir(a))
# print(a.__floor__)
# print(dir(b))
# print()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person('amjad',23)
print(p.__dict__)
# print(help(person))