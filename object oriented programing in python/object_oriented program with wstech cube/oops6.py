# class shopingcart:
#     def __init__(self):
#         self.item={}
#     def add_up(self ,name,price):
#         self.item[name]=price
#         print(f"[name],add to the cart")
#     def remove_item(self,name):
#         if name in self.item:
#             del self.item[name]
#             print(f'the remove item fm cart')
#         else:
#             print('not found in cart')
#     def total_price(self):
#         return sum(self.item.values())
#     def show_cart(self):
#         if not self.item:
#             print('cart is empty :')
#         else:
#             print('show on the item chart')
#             for i,(items,price) in enumerate(self.item.items(),1):
#                 print(f"the {i}.{items}-{price}")


# cart=shopingcart()
# cart.add_up('laptop',4000)
# cart.add_up('mobile',3000)
# cart.show_cart()
# print('the total price',cart.total_price())
# cart.remove_item('mobile')
# cart.show_cart()
# print('the total price',cart.total_price())


            