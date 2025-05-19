import pickle
files_name=open("dumps_data.txt","rb")
p=pickle.load(files_name)
print(p)