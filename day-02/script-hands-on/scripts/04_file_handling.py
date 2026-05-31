file = open("demo.txt") # OPEN
print(file.read())      # OPERATION
#file.write("Hello Dosto, kya haal chaal") # UNCHECK & SEE - ERROR: File not open in WRITE mode




file = open("demo.txt","w") # Open file in WRITE mode Delete existing content Start writing from scratch
file.write("Testing file handling in Python")
print()

file = open("config.txt")
print(file.read())  

file = open("config.txt","a")
file.write("\napp.log.level=DEBUG")
print()

file.close()            # CLOSE