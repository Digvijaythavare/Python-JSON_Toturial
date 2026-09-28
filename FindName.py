import json

data = {
    "name": "Rahul",
    "age": 22,
    "city": "Pune"
}

# Python → JSON
json_data = json.dumps(data)

print(json_data)

# JSON → Python
result = json.loads(json_data)

print(result["name"])
print(result["age"])