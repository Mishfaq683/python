class CarClass:
    def __init__(self,model,year,brand):
        self.model=model
        self.year=year
        self.brand=brand
        
    def display_info(self):
        print(f"display information :,{self.model},{self.year},{self.brand}")
        
 
    
ob=CarClass()
ob.display_info('toyota',2022,'corolla')
    
            