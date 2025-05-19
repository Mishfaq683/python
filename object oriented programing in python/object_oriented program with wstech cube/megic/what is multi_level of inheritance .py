# class grandefather:
#     def __init__(self,name):
#         self.name=name
#     def show_mother(self):
#         print(f"the name of grandfather{self.name}")
# class father(grandefather):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name=name
#     def show_father(self):
#         print(f"the name of father is {self.name}")
# class child(father):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name=name
#     def show(self):
#         print(f"the name of child{self.name}")
        
# cl=child('ishfaq ')
# print(cl.name)
# cl.show()
# cl.show_father()
# cl.show_mother()