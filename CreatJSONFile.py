import json

data = {
    "name" : "Vijay",
    "age" : 22,
    "isStudent" : True,
    "Courses" : ["Python","Javascript"]
}
with open('output.json', 'w') as file:
    json.dump(data,file,indent= 4) 