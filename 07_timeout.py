import requests

my_response = requests.get("https://httpbin.org/delay/3", timeout=5) #pass
# my_response = requests.get("https://httpbin.org/delay/3", timeout=2) #fail

print(my_response.status_code)