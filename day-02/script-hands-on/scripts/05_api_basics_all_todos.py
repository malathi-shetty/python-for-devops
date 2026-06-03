import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
)

data = response.json()

print("Type:", type(data))
print()

print("Total Todos:", len(data))
print()

print("First Todo:")
print(data[0])
print()

print("Title of Third Todo: ", data[3]["title"])
print()

count = 0

for todo in response.json():
    print("----------")

    for key,value in todo.items():
        print(key,value)

    count += 1

    if count == 5:
        break
print()

# uncheck comments to see all todos and their details

#for todo in data:
    #print("----------")

    #for key,value in todo.items():
        #print(key,value)
#print()

#print("length:",  len(data))
#print()

# uncheck comments to see all todos' titles
#for todo in data:
    #print("title:", todo["title"])







