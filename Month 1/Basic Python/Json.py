import json 
import os
from pathlib import Path

# json.dumps(user)  # Dictionary -> JSON String

user = {
    "name" : "uday",
    "age" : 22
}

json_data = json.dumps(user)  #Dictionary -> JSON String  its like JSON.Stringify(user)
print(json_data)  #json data 
print(type(json_data))  #<class 'str'>



normal_Data = json.loads(json_data) #its like JSON.parse(user -> object name)
print(normal_Data)
print(type(normal_Data)) #<class 'dict'>



# try:
#     with open("Month 1/Basic Python/demo.json", "r") as file:
#         data = json.load(file)

#     print(data)
# except FileNotFoundError:
#     print("File not found")

 
# --------reading the json file with help json.load -------- 
# this is for same directory = same folder 

print("--------this is for same directory = same folder ")
current_dir = os.path.dirname(__file__) # reading the json file with help json.load

file_path = os.path.join(current_dir, "demo.json")

with open(file_path, "r") as file:
    data = json.load(file)

print(data)
print(data["_id"]["$oid"])


print("-----------")

current_file = Path(__file__)

# project_root = current_file

jsonFile = current_file / "demo.json"

with open(jsonFile , "r") as file:
    data = json.load(file)
print(data)