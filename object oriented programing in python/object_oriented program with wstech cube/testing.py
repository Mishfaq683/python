class test:
    def __init__(self,__id):
        self.__id=__id
    def fun(self):
        return self.__id
    def fun(self,new):
        if self.__id>new:
            print("the value is updated")
        else:
            self.__id=new  
    def e_show(self):
            print(f"the value{self.__id} ")
    
t=test(102)
print(t.fun(2000))
t.e_show()
