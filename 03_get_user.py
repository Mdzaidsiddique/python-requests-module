# get using params

import requests

parameters = {
    "page" : 2
}
my_response = requests.get("https://reqres.in/api/users", params=parameters)
print(my_response.url)

json_response = my_response.json()

print(json_response["support"]["url"])