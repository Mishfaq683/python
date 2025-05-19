class cat:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def fun(self):
        print(f"the name {self.name} and {self.species}")
class add_cat(cat):
    def __init__(self, name, species,sound):
        super().__init__(name, species)
        self.sound=sound
    def show(self):
        print(f"the sound of the cat{self.sound}")
cl=add_cat('catblue','hybride','mavia mavia')
print(cl.name,cl.species,cl.sound)