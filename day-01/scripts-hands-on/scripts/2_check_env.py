# Get the Environment from User and print it

env = input("Enter the Environment: ") # taking input from the user (Keyboard) in env variable
print()

print("The User input Env is: ",env)
print()
# conditional statement simple if else

# == != > < >= <=

if env == "prd": # True or False
    print("Don't Deploy on Friday")
elif env == "stg": # True or False
    print("Take backup & Test well")
elif env == "test":
    print("Test it well")
else: # False
    print("Safe to deploy any day")
print()

# Type Casting - conversion of 1 data type to another
a = int(input("Enter the num 1: ")) # input() always takes string as input, so we need to convert it to int using int()
print("Raw input:", a)
print("Type:", type(a))

b = int(input("Enter the num 2: "))
print("After typecasting:", b)
print("Type:", type(b))
print()
print(type(a)) # <class 'int'>
print(type(b))
print()

print("Multiplication is: ",a*b)
print("Addition is: ",a+b)
print("Subtraction is: ",a-b)
print("Division is: ",a/b)

