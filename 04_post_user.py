# create new user
import requests
import json

# payload = {
#     "name": "zaid alif",
#     "job": "SDET"
# }
# my_response = requests.post("https://reqres.in/api/users", data = payload)

# payload_data = open("05_payload.json", "r").read()
# my_response = requests.post("https://reqres.in/api/users", data = json.loads(payload_data))
my_response = requests.post("https://reqres.in/api/users", data = json.loads(open("05_payload.json", "r").read()))

print(my_response)
assert my_response.status_code==201

json_response = my_response.json()
# print(json_response["name"])

# print(my_response.headers.get("Content-Type"))


data2 = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp = requests.post('https://reqres.in/api/register', data=data2)
print(resp.json()['token'])