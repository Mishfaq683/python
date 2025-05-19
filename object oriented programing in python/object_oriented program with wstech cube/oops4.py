class Employee:
    def __init__(self,name,salary,min):
        self.name=name
        self.salary=salary
        self.min=min
    def give_bonuse(self,amount):
        self.salary +=amount
    def display_salary(self):
        print(f"the show current salary with bonuse {self.name},{self.salary}")
        
    def minimium_salary_diplay(self):
        print(f"the minmium slary,{self.min},{self.min}")
        
object1=Employee('ahmad',5000,1000)
object1.give_bonuse(500)
object1.display_salary()
object1.minimium_salary_diplay()