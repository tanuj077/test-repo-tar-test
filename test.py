import requests
import os

ACTIONS_RUNTIME_TOKEN = os.environ.get("ACTIONS_RUNTIME_TOKEN")
print(ACTIONS_RUNTIME_TOKEN)

URL = "https://artifactcache.actions.githubusercontent.com/NHtGqffqobkG22BvxkwjZ50krG053v2tfi839LARA7jZONk0ux/_apis/artifactcache/cache?keys=cache-3240252986&version=3a594552ed0aa82f373e587ff9934771fc4bb57cccb5172b10b40979e8e9d248"

response = requests.get(url = URL, headers = {"Authorization": "Bearer " + ACTIONS_RUNTIME_TOKEN})

print(response.json())

archiveLocation = response.json()["archiveLocation"]

response2 = requests.get(url = archiveLocation)

print(response2.content, response2.headers, response2.status_code)
