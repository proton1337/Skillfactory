import requests

res_get = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})
res_post=requests.post("https://petstore.swagger.io/v2/user", json={"id":0, "username": "dmitriy", "firstName": "string", "lastName": "string", "email": "string", "password": "string", "phone": "string", "userStatus": 0}, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
res_put=requests.put("https://petstore.swagger.io/v2/user/dmitriy", json={"id":0, "username": "string", "firstName": "Dima", "lastName": "string", "email": "string", "password": "string", "phone": "string", "userStatus": 0}, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
res_delete = requests.delete("https://petstore.swagger.io/v2/user/dmitriy")
print(res_get.status_code, res_get.json())
print(res_post.json())
print(res_put.json())
print(res_delete.json())