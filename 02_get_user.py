import requests

my_response = requests.get("https://reqres.in/api/users?page=2")
json_response = my_response.json()
total_number_of_pages = json_response['total_pages']

print(total_number_of_pages)
print(json_response["total"])

assert total_number_of_pages == 2, "total pages count not matching"

email = json_response["data"][0]["email"]
print(email)

assert email.endswith("reqres.in"), "assertion message if fails"

assert json_response["data"][2]["last_name"] != None