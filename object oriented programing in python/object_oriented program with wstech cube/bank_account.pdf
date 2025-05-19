class bank_account:
    def __init__(self,account_no,balance):
        self._account_no=account_no
        self._balance=balance
    def deposite(self,amount):
        self.amount=amount
        self._balance +=amount
        return self._balance
    @property
    def balance(self):
        return self._balance
    def with_draw(self,amount):
        self.amount=amount
        if self._balance > amount:
            self._balance-= amount
            return f"the current amount is {self._balance}"
    @balance.setter
    def balance(self,new_balance):
        self.new_balance=new_balance
        if self._balance==new_balance:
            print(f"the current amount is zero")
        else:
            self._balance > new_balance
            print(f"the current value ")
    def display(self):
        print(f"the show amount is {self._account_no},{self._balance}")
            
bk=bank_account(101023,50000)
print(bk._account_no,bk._balance) 
print(bk.deposite(50000))
print(bk.with_draw(70000))
bk._balance=40000
print(bk.balance)
print(bk.display())
