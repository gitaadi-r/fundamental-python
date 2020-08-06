import requests

url = "https://www.detik.com/"

try:
    response = requests.get(url)
    print(response)
    print(f"Content: {response.text}")
except Exception as e:
    print(f"Error message, {e}" )

print("Program executed")