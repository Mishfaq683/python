# class person: 
#     def __init__(self,n,o): # the object is create dirctly call
#         print(f"hi im person")
#         self.name=n
#         self.occ=o
#     # name='amhmad'
#     # occ='developer'
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
        
        
        
        
# a=person('harray','hr')
# b= person('divya','developer')
# c=person(1,2) #self is automatically call is 
# a.info()
# b.info()
# c.info() # c is self to replace call it 
# # print(a.name,a.occ)
# the constructor to pass the value is 
# the constructor no pass value is defualt constructor 
# a=person_privacy(name,age,gender)
# print(a.name,a.age,a.gender)
class informationt:
    def __init__(self,name,age,id_no,batch):
        self.name=name
        self.age=age
        self.id_no=id_no  
        self.total_student=60
        self.batch=batch
    def checking_student(self):
        self.student=int(input('enter the student name is'))
        if self.student>self.total_student:
            print('your count is incorrect for the counting of student ')
        else:
            print('you hhave a correct counting ')
    # def add(self,universit_name,loaction_university):
        # print(f"{self.universit_name},{self.location_university}")

name=input('enter the name of the student')
age=int(input('enter the age'))
id_no=int(input('enter the id no is '))
batch=input('enter the session ')
for i in range(232501,232560):
    if 232506==i:
        print('ending of the loop plz')
        break
    print(i)
# student=int(input('enter your total student'))

info=informationt(name,age,id_no,batch)
print(info.name,info.age,info.id_no,info.batch,info.total_student )
info.checking_student()


            

