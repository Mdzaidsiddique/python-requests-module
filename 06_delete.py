import requests

my_response = requests.delete("https://reqres.in/api/users/2")

assert my_response.status_code == 204, "user detaltion failed"

print(my_response.status_code)