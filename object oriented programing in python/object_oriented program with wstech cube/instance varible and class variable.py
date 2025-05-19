class employee:
    companyname='apple'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def fun(self):
        print(f"the class varible name {self.companyname},and the instance varible name is {self.name},{self.age}")
    # def employee.noofemployee +=1
    @classmethod
    def new_fun(cls,new_name):
        cls.companyname=new_name
ep=employee("ahmad",23)
# ep.name='kashif'
print(ep.name,ep.age)
print(ep.companyname) # the assign class varible 
ep1=employee("rohan",25)
# ep.name='kashif'
# ep1.companyname='apple indai'
print(ep1.name,ep1.age)
ep1.companyname='apple indai' #the existing of instance variable to assign but no instance variable existing 
print(ep1.companyname)
ep1.new_fun('tech') # thise is class methode for usage
print(employee.companyname)