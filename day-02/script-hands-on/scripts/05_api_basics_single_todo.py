import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/3"
)

data = response.json()

print("type:",type(data))
print()

print("length:",len(data))
print()

print(data)
print()

print("userId: ",(data["userId"]))
print("id: " + str(data["id"]))
print(data["title"])
print(f"completed: {data['completed']}")
print()

for key,value in data.items():
    print(key,value)