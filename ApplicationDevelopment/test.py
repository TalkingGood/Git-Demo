import requests

respose = requests.get("https://httpbin.org/get")
print(type(respose))
print(type(respose.text))
print(respose.status_code)
print(respose.json())
print(type(respose.json()))
respose.encoding = 'utf-8'
#print(respose.text)
