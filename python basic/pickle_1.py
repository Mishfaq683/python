import pickle
s={1,2,3,4,1,'ishfaq','ahmad'}
file=open("pickledata.pkl","wb")
pickle.dump(s,file)
file.close()