def sum_of_num():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))

    print("Sum:", num1 + num2)


def take_backup():
    print("Backup script started ...")


env = input("Enter Environment: ")
print("Env is:", env)

if env == "prd":
    sum_of_num()

day = input("Enter day: ")

if day == "Monday":
    take_backup()