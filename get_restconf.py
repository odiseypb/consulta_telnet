import requests

url = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/"

payload = {}
headers = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOmxhc3RvcmFuZ2VyZXN0b3JlYmFsbDg4NzY='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)