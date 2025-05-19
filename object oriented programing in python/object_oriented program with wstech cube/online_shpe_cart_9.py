# class online_shpoe_cart:
#     def __init__(self):
#         self.item={}
#     def add_item(self,name,price):
#         self.item[name]=price
#         return self.item
        
#     def remove_item(self,name):
        
#         if len(self.item)==0:
#             return 0
#         else:
#             del self.item[name]
#     def show_total(self):
#         print(f"show the total item:{self.item}")
        
        
# o=online_shpoe_cart()
# print(o.add_item('laptop',10000))
# print(o.add_item('mobile',40000))
# o.remove_item("mobile")
# o.show_total()