import requests
response = requests.get('http://localhost:5000/books')
print(response.json())
