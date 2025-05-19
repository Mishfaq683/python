# the class instance and methode 
# class employee:
#     company_name='apple'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # @classmethod
#     # def change_name(cls,new_name):
#     #     cls.company_name=new_name

#     def fun(self):
#         print(")
    
#     def name(cls,new_name):
#         cls.name=new_name

# e=employee('ahmad',34)
# print(e.name,e.age)
# print(e.name('france'))
# print(e.company_name)
# e.fun()
class employee:
    company_name='apple'
    def show(self):
        print(f"the name of company:{self.company_name},{self.name}")
    # @classmethod
    def change_name(cls,new_company):
        cls.company_name=new_company
        
e=employee()
e.name='harray'
print(e.name)
e.show()
# e.change_name='tech'
e.change_name('tech')
e.show()
print(employee.company_name) # the comment of the class methode the show class varible
print(employee.company_name) # the not comment out of class methode show as instance of the class is 
