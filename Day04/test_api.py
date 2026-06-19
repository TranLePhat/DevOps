import requests

response = requests.get(
    "https://api.github.com/users/kubernetes"
)

data = response.json()

print(data["login"])
print(data["followers"])
print(data["public_repos"])