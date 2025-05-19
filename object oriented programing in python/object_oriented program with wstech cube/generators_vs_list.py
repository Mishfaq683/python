# #the generators is used for the to momery save  
# def my_generator():
#     for i in range(10):
#         yield i

# gen=my_generator() # the  have no cosuming the momery 
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#  list first of all the excuate all no the get the specific nos 
l=[x for x in range(10)] # the x is the first 1,2,3,...10 the get the  value
print(l[:10])