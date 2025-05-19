#the fechting is work on the same like model 
from functools import lru_cache
import time 

@lru_cache(maxsize=5)
def slow_fun(n):
    time.sleep(2)
    return n*n
slow_fun(20)
print("the value of 20")
slow_fun(20)
print("the value of 20")
slow_fun(30)
print("the value of 30")
slow_fun(30)
print("the value of 30")
slow_fun(20)
print("the value of 20")
slow_fun(60)
print("the value of 60")
slow_fun(60)
print("the value of 60")
slow_fun(60)
print("the value of 60")
    