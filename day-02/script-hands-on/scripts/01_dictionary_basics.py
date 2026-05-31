info = {
    "name" : "Shubham Bhaiya",
    "city" : "Pune",
    "qualification": "Mtech",
    "age" : 29,
    "salary": 22.5,
    "married": True,
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"])
print()

print("I love ", info.get("favourite","Not Found"))
print()

info.update({"channel": "TrainWithShubham"})
for key,value in info.items():
    print(key,value)
print()

print(dir(info))
print()

print(info.items())
print()



print(info.get("country","Not Found")) # This will return "Not Found" as country key is not present in the dictionary
print()

for key,value in info.items():
    print(key,value)
print()

print(info.get("country")) # This will return None as country key is not present in the dictionary
print()

#print(info["country"]) # This will throw an error as country key is not present in the dictionary