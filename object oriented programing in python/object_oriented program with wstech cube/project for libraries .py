class libraries:
    def __init__(self):
        self.libries={}
    def add_book(self,item,copies):
        if item in self.libries:
            self.libries[item]+=copies
        else:
            self.libries[item]=copies
            
            return f"the update {self.libries}"
            
    def barrow_book(self,item):
        if item in self.libries and self.libries[item] > 0:
            self.libries[item]-=1
            return f"the item is {item} and then find in the libraries {self.libries[item]}"
        else:
            print('sorroy your item is not avialble ')
    def info(self):
        if self.libries==0:
            print("empty libries")
        for book ,copies in self.libries.items():
            print(f"{book}:{copies}")
lb=libraries()
print(lb.add_book('python',5))
print(lb.add_book('python',5))
print(lb.add_book('java',5))
print(lb.barrow_book('c++'))
lb.info()