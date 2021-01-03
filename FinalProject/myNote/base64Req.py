import base64
import requests

encoded_bytes = base64.b64encode("mahesh:Mahe@123".encode())
encoded_str = encoded_bytes.decode()
headers = {'Authorization': f'Basic {encoded_str}'}
resp = requests.get("http://127.0.0.1:8000/api/note/", headers=headers)

print(resp)
if resp.status_code == 200:
    for lst in resp.json():
        print(f"Name : {lst['name']}\nText : {lst['text']}\nAdded_on : {lst['added_on']}\nUdded_on "
              f": {lst['updated_on']}")
elif resp.status_code == 404:
    print("Page Not Found")

elif resp.status_code == 400:
    print("Bad Request")

elif resp.status_code == 204:
    print("No Content")

elif resp.status_code == 201:
    print("Created")
