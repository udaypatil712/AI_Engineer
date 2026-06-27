# import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users"
# )

# data = response.json()
# print(data)

# -------------
# import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users")

# data = response.json()

# print(data)
# print(type(data))


import requests


params = {
    "userId":1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.json())