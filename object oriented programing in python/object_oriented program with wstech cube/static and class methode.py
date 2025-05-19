#the methode is no pass the self arugment
# def add(a,b):
#     return a+b 



# ************* these program is clear deffernce between the classmethod and staticmethod********************************


class math:
    def __init__(self,num):
        self.num=num
    def _addnum(self,n):
        self.num=self.num+n
        return self.num
    @staticmethod  
    def add(a,b):
        return a+b
    @classmethod
    def multplication(cls,a,b): # they have pass two type of cls,self
        return a*b
        
m=math(5)
print(m.num)
print(m._addnum(5)) # these is protected class  
print(m.add(4,4))
print(m.multplication(5,4))
