# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
# ep=employee('ishfaq',5000)
# print(ep.name,ep.salary)
# str="ahamad-4000"
# ep1=employee(str)
# # print(split.str()[0])
# print(str.split('-')[0])
# print(str.split('-')[1])



# # ep1=employee(str.spli)
# print(ep1.name,ep1.salary)
        
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def fromstr(cls,str):
#         return cls(str.split('-')[0],str.split('-')[1])

# e=employee('haris',5000)
# print(e.name,e.salary)
# str="amad-50000"
# e1=employee.fromstr(str)
# print(e1.name,e1.salary)
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(self,str): # these case is show error 
        return self(str.split('-')[0],str.split('-')[1])
    
e=employee('ahamad',4000)
print(e.name,e.salary)
str='amajd-2005'
e1=employee.fromstr(f'{str}')
print(e1.name,e1.salary)
        