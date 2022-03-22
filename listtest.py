humanList = []

while True :
    try :
        n = int(input("Enter Number:"))
        print(type(n))
        humanList.append(n)
    except :
        print("Invalid Type")
        continue

def humanListTest(x) :
    
    for i in x :
        print(i)
        print(type(i))

humanListTest(humanList)
