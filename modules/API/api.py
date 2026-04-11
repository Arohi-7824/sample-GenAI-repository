import requests
import json

print("="*60)
print("Working with APIs")
print("="*60)

url="https://jsonplaceholder.typicode.com/posts"

payload={}
headers={}

response=requests.request("GET",url,headers=headers,data=payload)

print(response.text)

print(response)