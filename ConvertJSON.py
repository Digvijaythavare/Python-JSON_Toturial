import json

data = {
    "name" : "Vijay",
    "age" : 22,
    "isStudent" : True,
    "Courses" : ["Python","Javascript"]
}

Json_string = json.dumps(data)

print(Json_string)