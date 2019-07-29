def getDivisors():
    num = int(input("give me a number: "))
    result = []
    
    #for i in range(1, num):
    #   if num % i == 0: result.append(i)

    #shorter and more elegant version
    result = [i for i in range(1,num) if num % i == 0]

    print(num, " divisor's :", result)


getDivisors()
        
