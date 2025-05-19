# # class family:
# #     def __init__(self,p_name,p_age):
# #         self.parent_name=p_name
# #         self.parent_age=p_age
# #     def parent_name(self):
# #         print(f"the name of parents is {self.parent_name},{self.parent_age}")
# # class child(family):
# #     def __init__(self, name, age):
# #         super().__init__(family)
# #         self.childname=name
# #         self.childage=age
# #     def parent_child(self):
# #         print(f"the name of child  is {self.name},{self.age}")
        


# # object=child('ahmad',34)   
# # object.parent_name()   
# class Parent:
#     def __init__(self, name):
#         self.name = 'amjad'

#     def show_message(self):
#         print(f"Hello, I am {self.name}, and I am the parent.")

# # Child class inheriting from Parent
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Calling the Parent constructor
#         self.age = age

#     def display_info(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Creating an object of Child class
# child_obj = Child("Alice", 12)

# # Calling methods
# child_obj.show_message()  # Inherited from Parent
# child_obj.display_info()  # Defined in Child
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def show_student(self):
#         print(f"the personal info in university is {self.name},{self.rollno}")
# class marks_student(student):
#     def __init__(self,name,rollno, marks,grade):
#         super().__init__(name, rollno)
#         self.marks=marks
#         self.grade=grade
#     def info_student(self):
#         print(f"the show information of marks is {self.marks},{self.grade}")
    
# mk=marks_student('ahmad',232506,1100,'A')
# mk.show_student()
# mk.info_student()
# class person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show_fun(self,age):
#         self.age
#         print(f"the name  of user  :{self.name},and the age chek the cholosatrole level is :{self.age},then show :{self.address}")
# class delivery_men(person):
#     def __init__(self, name, age, address,delivery_men_name,motorcycle_no,gps_locatiion):
#         super().__init__(name, age, address) 
#         self.delivery_men_name=delivery_men_name
#         self.motorcycle_no=motorcycle_no
#         self.gps_loction=gps_locatiion
#     def delivery_info(self):
#         print(f"the name of {self.delivery_men_name},{self.motorcycle_no},{self.gps_loction}")       

# dm=delivery_men('ishfaq',45,'board bazar','tatto',4567,'saddar to borad bazar')
# dm.show_fun()
# dm.delivery_info()