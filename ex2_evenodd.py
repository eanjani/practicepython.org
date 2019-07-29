def getNumber():
    num = int(input("type a number: "))

    if num % 2 == 0:
        print("Number ", num, " is even")
    else:
        print("Number ", num, " is odd")


getNumber()
