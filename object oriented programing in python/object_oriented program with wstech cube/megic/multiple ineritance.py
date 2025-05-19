class father:
    def __init__(self,name,identity):
        self.name=name
        self.identity=identity
    def show(self):
        print(f"the name{self.name}, and the identity of{self.identity} ")
class mother:
    def __init__(self,identity):
        self.identity=identity
    def show(self):
        print(f"the identity{self.identity}")
class child(father,mother):
    def __init__(self, name,derived,identity):
        super().__init__(name, identity)
        self.derived=derived
    def info(self):
        print(f"the the dreived from the mother and father combiation {self.derived}")
ob=child('sherin jan','female','ishfaq')
print(ob.name,ob.identity,ob.derived)
ob.show()
# ob.info()
print(child.mro())

