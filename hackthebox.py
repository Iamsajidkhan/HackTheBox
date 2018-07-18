import requests

import base64

import json

print("[+] Hackthebox invite Code")

print("[+] connect to server hackthebox.eu ...")

print("[+] Invite Code : ",base64.b64decode(requests.post("https://www.hackthebox.eu/api/invite/generate", json={"key": "value"}).json()["data"]["code"]))
