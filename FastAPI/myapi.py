import requests

url = "https://api.restful-api.dev/objects"

# Send GET request to API and display status code
response = requests.get(url, timeout=30)
print("Status code:", response.status_code)

# Convert json() response into python data & print it
data = response.json()
print(f"API response:\n {data}")