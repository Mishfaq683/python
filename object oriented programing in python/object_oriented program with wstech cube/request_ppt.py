# import requests

# # Define the API URL
# url = "https://www.Google.com/posts/1"

# # Send a GET request
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     data = response.json()  # Convert response to JSON
#     print("Title:", data["title"])  # Print a specific field
#     print("Body:", data["body"])    # Print the body text
# else:
#     print("Failed to fetch data:", response.status_code)
import requests 
import json 
# from bs4 import BeautifulSoup

response = requests.get("https://www.google.com/blogpost/django-cheatsheet/")
r=json.loads(response.text)
print(r)
# r = requests.get(url)
# # print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)
