import requests
import os

ACTIONS_RUNTIME_TOKEN = os.environ.get("ACTIONS_RUNTIME_TOKEN")
CACHE_URL = os.environ.get("CACHE_URL")
print(CACHE_URL)

response = requests.get(url = CACHE_URL, headers = {"Authorization": "Bearer " + ACTIONS_RUNTIME_TOKEN})

print(response.text)

archiveLocation = response.json()["archiveLocation"]

response2 = requests.get(url = archiveLocation)

print(response2.headers, response2.status_code)

with open("cache.tzst", "wb") as f:
  f.write(response2.content)
