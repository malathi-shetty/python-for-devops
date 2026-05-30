# Table once
num = int(input("Enter the number you want the table for: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Loop version
while True:
    choice = input("Enter choice (press q to quit): ")

    if choice == "q":
        print("Exiting program...")
        break

    num = int(choice)

    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

# Greeting
name = input("Enter dost ka name: ")
print(f"Hello Dosto, {name}")