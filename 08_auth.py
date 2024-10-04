import requests

# res = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("abcd", "abc"))

# print(res.status_code) #status code 401

res = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("admin", "admin"))
print(res.status_code) #status code 200