class grandfather:
    def __init__(self,g_name):
        self.name=g_name
    def g_show(self):
        print(f"the grandfather {self.g_name}")
class father(grandfather):
    def __init__(self, g_name,f_name):
        super().__init__(g_name)
        self.f_name=f_name
    def f_show(self):
        print(f"the value of the{self.f_name} ")
class combination(father,grandfather):
    def __init__(self,g_name,f_name,c_name):
        super().__init__(g_name, f_name)
        self.c_name=c_name
    def c_show(self):
        print(f"the name of the {self.c_name} ,{self.g_name},{self.f_name}")

cl=combination('bk','khan','ishfaq')
print(cl.c_name,cl.f_name,cl.g_name)
cl.c_show()
cl.g_show()
        
#         # Base class (Parent)
# class A:
#     def show_A(self):
#         print("Class A")

# # Derived class 1 inheriting from A
# class B(A):
#     def show_B(self):
#         print("Class B")

# # Derived class 2 inheriting from A
# class C(A):
#     def show_C(self):
#         print("Class C")

# # Creating objects of child classes
# obj1 = B()
# obj2 = C()

# # Calling methods
# obj1.show_A()  # Accessing method from Class A using object of Class B
# obj1.show_B()  # Method of Class B

# obj2.show_A()  # Accessing method from Class A using object of Class C
# obj2.show_C()  # Method of Class C

