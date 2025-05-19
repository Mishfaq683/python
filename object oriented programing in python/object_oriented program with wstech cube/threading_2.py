# 🔹 What is Threading in Python?
# Threading allows a program to run multiple tasks concurrently within the same process. It is used to improve performance when dealing with tasks that wait for external resources (like I/O operations).

# ✅ Best for I/O-bound tasks (e.g., file reading, API calls)
# ✅ Uses threads to run tasks in parallel
# ✅ Runs within a single process, so it shares memory

# 🔹 Why Use Threading?
# ✔ Speeds up I/O-bound tasks (file operations, network requests)
# ✔ Prevents UI freezing in GUI applications
# ✔ Efficiently handles multiple tasks at once

# ⚠️ Not ideal for CPU-heavy tasks (Use multiprocessing instead)




# import threading
# import time
# def fun(second):
#     print("the value of one  seconds:{second}")
#     time.sleep(second)
# time1=time.perf_counter()  
# # the normal code 
# # fun(1)
# # fun(2)
# # fun(4)
# # fun(5)
# # t2=time.perf_counter()
# # print(t2-t1)
# # the threading code is used for the code
# t1=threading.Thread(target=fun,args=[2])
# t2=threading.Thread(target=fun,args=[2])
# t3=threading.Thread(target=fun,args=[1])
# t1.start()
# t2.start()
# t3.start()
# t1.join() # the show on the end fun1 and next of fun2 cap 
# t2.join()
# t3.join()
# time2=time.perf_counter()
# print(time2-time1)
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
  time1 = time.perf_counter()
  # Normal Code
  # func(4) 
  # func(2)
  # func(1)
  
  
  # Same code using Threads
  t1 = threading.Thread(target=func, args=[4])
  t2 = threading.Thread(target=func, args=[2])
  t3 = threading.Thread(target=func, args=[1])
  t1.start()
  t2.start()
  t3.start()
  
  t1.join()
  t2.join()
  t3.join()
  # Calculating Time 
  time2 = time.perf_counter()
  print(time2 - time1)


def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()