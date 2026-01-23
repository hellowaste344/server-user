#requests.get(url, params={key: value}, **kwargs)
#requests.post(url, data='')
import requests
response = requests.get("https://en.wikipedia.org/wiki/Mark_Zuckerberg")
print(response.status_code)

# Response Methods
response = requests.get("https://api.github.com/users/naveenkrnl")
print(response.status_code)
print(response.reason)#returns a text corresponding to the status code
print(response.content, '\n')# returns the content of the response, in bytes
print(response.headers)
print(response.cookies)
print(response.history)
print(response.is_permanent_redirect)
print(response.is_redirect)
print(response.json)#returns  a JSON objects if there is otherwise raises an error
print(response.text)#returns the content of the response, in unicode
print(response.raise_for_status())#returns an HTTPError object if an error has occured
print(response.ok)#if 200 <= status_code < 400 returns True
print(response.links)#returns the header links


payload = {'username': 'Ashe', 'password': 'X_Ashe'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)
print(response.status_code)
print(response.reason)

#Authentication using Python requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass')) # user->username pass->password
print(response.status_code)

#SSL Certificate Verification
response = requests.get('https://expired.badssl.com/', verify=False)
print(response.status_code)
response = requests.get('https://github.com/', verify='/path/to/certfile')
print(response.status_code)

#Error Handling with Requests
try:
    response = requests.get("https://www.example.com/", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error: ", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something's off:", err)