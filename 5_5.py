humanList = [] 

while True :
    n = input("Enter Number:")
    if n == "done" :
        break

    try :
        int(n)
    except :
        print("Invalid Type")
        continue
    humanList.append(n)
print("Largest number is:", max(humanList))
print("Smallest number is:", min(humanList))
        
