import json

data = {
    "judul buku":"bedebah"
}

with open('data.json','w') as file:
    json.dump(data, file, indent=4)