import requests

URL = "https://artifactcache.actions.githubusercontent.com/NHtGqffqobkG22BvxkwjZ50krG053v2tfi839LARA7jZONk0ux/_apis/artifactcache/cache?keys=Linux-3182001628&version=db813e27660a005fc99305e68352e9609af9eb801d1200177174a28cce3a7bc9"

response = requests.get(url = URL)

print(response.json())