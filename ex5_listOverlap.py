import random



def getOverlap(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    for j in b:
        if j in a and j not in result:
            result.append(j)
    print("Common elements for a lists ", a," and ", b, " are ",result)

    #or more elegant and shorter:
    #print([i for i in a for j in b if i == j])


a = random.sample(range(15),  random.randint(1,10))
b = random.sample(range(15),  random.randint(1,10))
getOverlap(a,b)
    
