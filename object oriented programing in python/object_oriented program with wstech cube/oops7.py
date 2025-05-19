class online_pharmacy:
    def __init__(self):
        self.drog= {}       
    def add_up(self,name,price):
        self.drog[name]=price
        print(f"the add of name of drog is {name}")
    def remove_drog(self,name):
        if name in self.drog:
            del self.drog[name]
            print(f'remove the drog {name}')
        else:
            print(f"not found in{name}")
    def total_price(self):
        return sum(self.drog.values())
    def show_pharmacy_menu(self):
        if not self.drog:
            print('not delivery today the market sorroy other one choice is same formule')
        else:
            print("it present in the  ")
            for i,(drogs,price) in enumerate(self.drog.drog(),1):
                print(f"the {i}. {drogs} - {price}")

ph=online_pharmacy()
ph.add_up('paracetmole',50)
ph.add_up('bronchole syrap',150)
ph.add_up('postina',120)
ph.show_pharmacy_menu()
print('toatal price',ph.total_price())
        