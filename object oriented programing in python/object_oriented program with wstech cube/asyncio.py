# import asyncio
# import aiohttp

# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.text()
#             print(f"Fetched {url}: {len(data)} characters")

# async def main():
#     urls = ["https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?auto=compress&cs=tinysrgb&w=600"]
#     await asyncio.gather(*(fetch(url) for url in urls))  # Runs all tasks concurrently

# asyncio.run(main())  # Start async execution
# import time
# import asyncio 
# import requests


# async def function1():
#   print("func 1") 
#   URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
#   response = requests.get(URL)
#   open("instagram.ico", "wb").write(response.content)
   
#   return "Harry"
  
# async def function2():
#   print("func 2") 
#   URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram2.jpg", "wb").write(response.content)
  
# async def function3():
#   print("func 3")
#   URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram3.ico", "wb").write(response.content)

# async def main():
#   # await function1()
#   # await function2()
#   # await function3()
#   # return 3
#   L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#   print(L)
#   # task = asyncio.create_task(function1())
#   # # await function1()
#   # await function2()
#   # await function3()

# # asyncio.run(main())
# import time 
# import asyncio
# async def fun_1():
#     await asyncio.sleep(2)
#     print("the good mornining")
# async def fun_2():
#     await asyncio.sleep(3)
#     print("the lunch")
# async def fun_3():
#     await asyncio.sleep(4)
#     print("the evening ")

# async def main():
#     task1=asyncio.create_task(fun_1())
#     task2=asyncio.create_task(fun_2())
#     task3=asyncio.create_task(fun_3())
#     await task1
#     await task2
#     await task3
    
# asyncio.run(main())
import asyncio

async def fun_1():
    await asyncio.sleep(2)
    print("Good morning!")

async def fun_2():
    await asyncio.sleep(3)
    print("Lunch time!")

async def fun_3():
    await asyncio.sleep(4)
    print("Good evening!")

async def main():
    task1 = asyncio.create_task(fun_1())  # Create task
    task2 = asyncio.create_task(fun_2())  # Create task
    task3 = asyncio.create_task(fun_3())  # Create task

    await task1  # Corrected: Removed parentheses
    await task2  # Corrected: Removed parentheses
    await task3  # Corrected: Removed parentheses

# Run the event loop
asyncio.run(main())  # Corrected: asyncio.run() instead of async.run()
