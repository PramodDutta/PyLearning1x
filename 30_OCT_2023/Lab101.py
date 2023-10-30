api_response = {
    "first_name": "Pramod",
    "age": 34,
    "last_name": "Dutta",
    "email": "pramoddutta{{$randomInt}}@live.com",
    "password": "Test@4321",
    "commission": 10,
    "roles": [
        4
    ]
}

print(api_response)
print(type(api_response))

print(api_response.get('password'))

print(api_response['roles'])
print(api_response.get('roles'))

api_response['age'] = 43
print(api_response)

for key, value in api_response.items():
    print(key, value)
