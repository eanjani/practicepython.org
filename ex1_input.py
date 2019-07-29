import datetime

def getData():
    age = int(input("What's your age? "))
    name = input("what's your name?")
    another = int(input("Give me another number: "))
    
    now = datetime.datetime.now()
    currYear = now.year

    hundredYears = (100 - age)+currYear
    print(another*" Dear {nickname} You'll get into 100 yrs old in a {year} \n".format(nickname = name, year = hundredYears))


getData()
