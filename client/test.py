import requests

response = requests.post("http://127.0.0.1:1234/main/", {"questions_num": 1})
print(response.json())