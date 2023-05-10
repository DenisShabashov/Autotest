import requests
import json

base_url = 'https://petstore.swagger.io/v2/pet'
status = 'available'
headers = {'accept': 'application/json'}
headers2 = {'accept': 'application/json',
            'Content-Type': 'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "bob"
  },
  "name": "cat",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data_put = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
id_del = '9602990142'

res1 = requests.get( f"{base_url}/findByStatus?status={status}", headers=headers)
print(res1.status_code)
print(res1.json())

res2 = requests.post(f'{base_url}', headers=headers2, data=json.dumps(data))
print(res2.status_code)
print(res2.json())

res3 = requests.put(f'{base_url}', headers=headers2, data=json.dumps(data_put))
print(res3.status_code)
print(res3.json())

res4 = requests.delete(f'{base_url}/{id_del}', headers=headers)
print(res4.status_code)



