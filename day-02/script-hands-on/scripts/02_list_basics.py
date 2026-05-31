a = [100,200,300, True, 4.6]    # LIST banane ka akela tareeka
print(type(a))
print(a) # list me hum alag alag type ke data store kar sakte hain
print(a[0]) # list me index 0 se start hota hai
print() 
a.append(500)
print(a)
print()

clouds = list() # LIST banane ka dusra tareeka
print(type(clouds))
print()

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")
print(clouds)
print()
print("Length of list is:", len(clouds))
print()

print("World Leader for Cloud Service Provider is:",clouds[0])
# list me index 0 se start hota hai, isliye clouds[0] se first element ko access kar sakte hain
print()

print("Indian Cloud Service Provider is:",clouds[-1])
# list me negative index bhi hota hai, -1 se last element ko access kar sakte hain
print()

print(dir(clouds))# list ke andar kaun kaun se method hote hain ye dekhne ke liye dir function ka use karte hain
print()

print(clouds.extend.__doc__)# list me ek se zyada element add karne ke liye extend method ka use karte hain
print()

# iterate a list
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Market Leader + covered in course")
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} DevOps - Zero To Hero Me vo bhi cover karoonga")
    else:
        print(f"{cloud} baaki nahi honge")