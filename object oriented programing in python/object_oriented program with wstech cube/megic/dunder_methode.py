# the megic methode is __init funcation is dunder methode
class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name{self.name}")
    # def __len__(self):
    #     i=0
    #     for c in self.name:
    #         i = i+1
    #     return i
    # # def __str__(self):
    # #     return f"the value of the {self.name} /str"
    # def __repr__(self):
    #      return f"the value of the {self.name} /repr"
    
print(employee('harray'))
# print(e.name)
# print(len(e))