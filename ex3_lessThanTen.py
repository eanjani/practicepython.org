def lessThanTen(l):
    num = int(input("give me a number: "))
    print("Elements smaller than ", num, " are: ",[i for i in l if i < num])
   


lessThanTen([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
