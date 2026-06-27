user = {
    "name" : "uday",
    "age" : 11,
    "city" : "Pune"
}

print(user["age"])

for i in user:  #its print key only
    print(i)

for i in user.values(): #its print values
    print(i)


for key , value in user.items():
    print(key , value)


# nested dictionary 

print("------nested dictionary---------")

user = {
    "name": "Uday",
    "address": {
        "city": "Pune",
        "state": "Maharashtra",
        "marks" : [1,2,3,4],
        "subjects" : {
            "math" : 12,
            "english" : 22
        }
    }
}


print(user["address"]["city"])  #if in javascript we are writing like (user.address.city)

for value in user["address"]["marks"]:
    print(value)


# Methods of dictionary 

print("---------Methods of dictionary-------")


print(user.get("address").get("city"))


for subject , mark in user.get("address" , {}).get("subjects" , {}).items():
    print(subject , mark)
