import requests

if __name__=='__main__':
    host = "sandbox-iosxe-recomm-1.cisco.com"
    username = "developer"
    port = 443
    password = "lastorangerestoreball8876"

    url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/ip/domain"
    payload = "{\"name\": \"cisco.com.mx\"}"


    # Encabezados para RESTCONF

    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # enviamos una insercion
    response = requests.request("POST", url, auth=(username, password),
                                data=payload, headers=headers, verify=False)

    # print the json that is returned
    print(response.text)