print("Using for loop - fixed times")
for i in range(4):
    env = input("Enter Environment: ")

    if env == "prd":
        print("Don't deploy on Friday")
    elif env == "stg":
        print("Take backup & test")
    elif env == "test":
        print("Test it well")
    else:
        print("Safe to deploy")

print()
print("Using while loop - user controlled times") #Run forever until user stops
while True:
    fruit = input("Enter Fruits (q to quit): ")

    if fruit == "q":
        print("Exiting...")
        break

    if fruit == "mango":
        print("Make Mango Juice")
    elif fruit == "mpple":
        print("Make Apple Juice")
    elif fruit == "banana":
        print("Make Banana Juice")
    else:
        print("Take fruit and make juice")

print()
print("Using while-if-else with counter")

i = 0
while i < 3:
    color = input("Enter Color: ")

    if color == "green":
        print("Greenery looks good for Mother Earth")
    elif color == "blue":
        print("Blueberry is good for health")
    elif color == "purple":
        print("Purple butterfly is flying in the garden")
    else:
        print("Choose color and make your day colorful")

    i = i + 1