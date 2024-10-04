import requests

my_response = requests.get("https://reqres.in/api/users?page=2")
# print(my_response)
# print(type(my_response))
# print(dir(my_response))

# status_code = my_response.status_code
# assert status_code == 200, "response code does't match"
# print(status_code)

# print(my_response.text)
# print(my_response.content)
# print(my_response.json())

# print(my_response.headers)
# print(type(my_response.headers))

print(my_response.cookies)
print(type(my_response.cookies))

print(my_response.encoding)
print(my_response.url)
