import requests

# with wrong username and password
# res = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("abcd", "abc"))

# print(res.status_code) #status code 401

# with correct username and password
res = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("admin", "admin"))
print(res.status_code) #status code 200