import json

with open('data.json','r') as file:
    data = json.load(file)

    data['harga'] = 65000,
    data['email'] = 'azahrailla@gmail.com'

    with open('data.json','w') as file:
        json.dump(data, file, indent=4)