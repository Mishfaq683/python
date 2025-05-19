import pickle 
l=[10,20,30,40]
files_name=open("dumps_data.txt","wb")
pickle.dump(l,files_name)
files_name.close()