import pickle
name=input("enter the name     is:")
age=int(input("enter the value of age"))
d={'name':name,'age':age}
person_write=open("wrtedatatxt.txt","wb")
pickle.dump(d,person_write)
person_write .close()






