import requests

# put: update/replace
# provide all propeties while making request
# if record exist it will update/replace and if not it will create

data_pl = {
    "name": "Umair",
    "job": "API Testing"
}
# my_response = requests.put("https://reqres.in/api/users/2", data=data_pl)

# print(my_response.status_code)
# print(my_response.json()['name'])
# print(my_response.json())




# patch: Update/Modify
# specify only the properties that has to be update, it will update/modify if record exist

data_pl2 = {
    "name": "Umair Ali",
    "job": "API Testing"
}
my_response2 = requests.patch("https://reqres.in/api/users/2", data=data_pl2)

print(my_response2.status_code)
print(my_response2.json()['name'])
print(my_response2.json())
