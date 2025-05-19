# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     @property
#     def name(self):
#         return {'age':self._age,'name':self._name}
#     # these mean that return at time one type but the return the two or more in list and dic
    

# name=input('enter the name is :')
# p=person(name,23)
# print(p.name)
# class fmaily:
#     def __init__(self,name,age,salary,occ):
#         self._name=name
#         self._age=age
#         self._salary=salary
#         self.occ=occ
#     @property
#     def name(self):
#         if self._name=='ishfaq':
#             return [self._name,self._salary/100,self._age]
#         else:
#             print('incorrect info')
        
    
    
# name=input('entee your name:') 
# age=int(input('enter the age'))
# salary=int(input('enter the value of a salary is :'))
# occ=input('enter your occupition brother')
 
    
# f=fmaily(name,age,salary,occ)
# print(f.name)
# print(f._age)
# print(f._salary)
# print(f.occ)
# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def new_age(self,new_age):
#         if new_age <0:
#             print("the have negative nos")
#         else:
#             self._age=new_age
            
            
            
# p=person('alice',25)
# print(p._name,p.age)
# p.age=-1
# print(p.age)
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age  # Private attribute

#     @property
#     def age(self):  # Getter
#         return self._age  # Only retrieves the value

#     @age.setter
#     def age(self, new_age):  # Setter
#         if new_age < 0:
#             print("Age cannot be negative!")
#         else:
#             self._age = new_age  # Updates the value

# # Creating an object
# p = Person("Alice", 25)

# # Using Getter
# print(p.age)  # ✅ Output: 25 (retrieved via getter)

# # Using Setter
# p.age = 30  # ✅ Updates age successfully
# print(p.age)  # ✅ Output: 30

# p.age = -5  # ❌ Invalid, setter prevents negative age

# class my_info:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def show_fun(self):
#         print(f"the vcalue is {self._name},{self._age}")
    
#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self,new_age):
#         if new_age<0:
#             print('the value is negative bro')
#         else:
#             self._age==new_age
    
    
    
# m=my_info('ahmad',23)
# print(m._name)
# print(m._age)


# m.age=45
# print(m._age)

# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def show_funcation(self):
#         print('the value of name and age,{self._name},{self.age}')
#     @property
#     def age(self):
#         return self._age
    
    
#     @age.setter
#     def age(self,new_age):
#         if new_age < 0:
#             print('the negative nos ')
#         else:
#             self._age==new_age
        
            
# p=person('ahmad',23)
# print(p._name,p._age)
# # p.name='alamjan'
# # p.age=12
# p.show_funcation()

# p._age=45
# print(p._age) # the before error show is that _age
# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def show(self):
#         print(f"the show value is {self._name},{self._age}")
    
    
# p=person('ishfaq',34)
# print(p._name,p._age)
# p._name='amad'
# p._age=44
# p.show()
