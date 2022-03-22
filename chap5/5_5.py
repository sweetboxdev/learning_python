humanList = [] 

while True :
    n = input("Enter Number:")
    if n == "done" :
        break

    try :
        intn = int(n)
    except :
        print("Invalid Type")
        continue
    humanList.append(intn)

def listMean(x) :
    listSum = 0
    counter = 0
    int(listSum)
    for i in x :
        int(i)
        listSum = listSum + i
        counter = counter + 1
    return(listSum / counter)

def largeNumber(x) :
    num = None
    for i in x :
        if num == None or num < i :
         num = i
    return num

def smallNumber(x) :
    num = None
    for i in x :
        if num == None or num > i :
            num = i
    return num


print("Largest:", largeNumber(humanList), "Smallest:", smallNumber(humanList) , "Average:", listMean(humanList))
    

