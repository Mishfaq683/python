# class person:
#     name="harray"
#     occ="developer"
#     def info(self):
#         print(f"{self.name} is a{self.occ}")
    
# a=person()
# b=person()
# b.name="ahmad"
# b.occ="hr"
# # print(a.name,a.occ) # the mean things is 
# a.info()# this one is defualt argument parameter is  
# b.info()
class person:
    # def __init__(self):
        # print('hi ishama hoe are you today') # the create a object then after defualt call no need to create a object 
        
    name='haji'
    age=23
    def info(self):
        print(f'hello')  #this is one first create in object then after to call 
        print(f"{self.name},{self.age}") # this self is defualt value gain in the haji and 23 the usage of self arguments 
        
    
a=person()
b=person()
a.name='ahmad'
a.age=34
print(a.name,a.age)
b.info()