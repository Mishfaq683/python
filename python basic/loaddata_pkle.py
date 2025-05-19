import pickle
file=open("pickledata.pkl","rb")
p=pickle.load(file)
print(p)