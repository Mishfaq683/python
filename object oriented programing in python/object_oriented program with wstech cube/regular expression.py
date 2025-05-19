# the regular expression is used for  the  strin to find and the match fun is  used for the 
# Regular expressions (regex) in Python are handled using the re module. 
# They allow for searching, matching, and manipulating strings based on specific patterns.
# import re
# pattern=r"ishfaq"
# text='''ishfaq marwat you@   have doing  well,   today ishfaq marwat
# '''
# repalce='amjad'
# match=re.search(pattern,text)# the value everywhere is found in the  text
# match=re.match(pattern,text)#the used for beginnig values
# match=re.findall(pattern,text)#the return all match in the form of list
# match=re.finditer(pattern,text)#return the iteration of the object
# match=re.sub(p,text,repalce)# the help to remove the 
# match=re.sub(r"[^/w/s]","",text)
# print(match)
# if match==pattern:
#     print("found him the value ")
# else:
#     print("not found him the value ")
# import re

# text = "Hello! How's it going? #Python @AI"
# clean_text = re.sub(r"[^\w\s]", "", text)  # Remove anything that's not a word or space

# print(clean_text)  # Output: Hello Hows it going Python 

# import re
# text="the value ,of the equations;"
# match=re.split(r"[,;]+",text)
# print(match)