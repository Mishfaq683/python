# class person:
#     # def __init__(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     # name='ahmad'
#     # age=23
#     def show_fun(self):
#         print({self.name},{self.age})

# ob=person('ahmad',23)
# ob1=person("anas",25)
# print(ob1.name,ob1.age)
# print(ob.name,ob.age)
# ob.show_fun()
# ob1.show_fun()

# # ***************************** THE PUBLICE ACESSER **********************************
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_fun(self):
#         print(f"{self.name},{self.age}")
# object=person('amjad',23)
# object.show_fun()

# ***************************** THE PRIVATE ACESSER **********************************
# class person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#     def show_fun(self):
#         print(f"{self.__name},{self.age}")
# object=person('amjad',23)
# object.show_fun()
# class student:
#     def __init__(self ,name,age):
#         self.name=name
#         self.__age=age
#     # @property
#     def get__age(self):
#         return self.__age
    
#     # @age.setter
#     def set__age(self,new_age):
#         if 0 < new_age > 100:
#             self.__age=new_age
#         else:
        
#            return self.__age
#         # else:
#             # print (f"the invalide no is used 1 between in 100")
#     # def show_fun(self):
#         # print(f"the show fun is the :{self.name},{self.__age}")

# s=student('ahmad', 23)
# print(s.get__age())
# print(s.set__age(78))
# print(s.get__age())
# # s.show_fun(
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age
    
#     def show_fun(self):
#         print(f"the value of the :{self.name},{self._age}")
     
#     @property
#     def age(self):
#         return f"the rerurn orginal values of age {self._age}"
#     @age.setter
#     def age(self,new_age):
#         if 0 <new_age > 100:
#             self._age=new_age
#         else:
#             print(f"the invalide nos is show that")
    
#     def show_fun(self):
#         print(f"the {self._age}")

# p=person('amjad',34)
# print(p.name,p._age)

# class student:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,new_age):
#         if new_age >0:
#             self.__age=new_age
#         else:
#             print("the negative nos is ")
#     def show_fun(self):
#         print(f"the :{self.__name},{self.__age}")

# object=student('ahmad',23)
# print(object.__name,object.age)
# print(object.get_age())
            
