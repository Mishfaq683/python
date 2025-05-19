# class parent:
#     def __init__(self):
#         self.name="harray"
#     def parent_fun(self):
#         print(f"the parent name{self.name}")
# class child(parent):
#     def __init__(self,age):
#         self.age=age
#         self.name="ahmad" # thes is overrinding case
#     def show(self):
#         print(f"the show age of child{self.age},{self.name}")
#         super().parent_fun()
# cl=child(23)
# print(cl.age)
# print(cl.name)
# cl.show()  #the show age of child 23,ahmad
# #the parent nameahmad

# *************************************************** overloading*********************************
# def "the same name funcation or class the different methode and the different parameters"
# class math:
#     def add(self ,a,b=0,c=0):
#         return a+b+c
# m=math()
# print(m.add(5))
# print(m.add(5,10))
# print(m.add(5,10,20)) 

# second example with basic example
class MathOperations:
    def add(self, *numbers):
        return sum(numbers)

# Creating an object
math_op = MathOperations()

print(math_op.add(5))            # Output: 5
print(math_op.add(5, 10))        # Output: 15
print(math_op.add(5, 10, 15))    # Output: 30
print(math_op.add(1, 2, 3, 4, 5)) # Output: 15
