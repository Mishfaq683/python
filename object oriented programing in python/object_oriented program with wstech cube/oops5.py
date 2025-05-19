class bank_account:
    def __init__(self ,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposite_money(self,amount):
        self.balance += amount
        print(f"the show new money of depositor,{self.account_number},{self.balance}:the new balance{self.balance}")
    def withdraw_amount(self,amount):
        if self.balance >= amount:
            self.balance -=amount
            print(f"the new amount show on the screen{self.account_number},{self.balance}:new amount{self.balance}")
    # def display.balance(self):
        # print(f'display current value{}')
object=bank_account(1120195,1000)
object.deposite_money(500)
object.withdraw_amount(1500)