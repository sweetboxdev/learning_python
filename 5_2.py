smallest = None
largest = None
while True:
    num = input("Enter number:")
    if smallest == None : 
        smallest = num
    if largest == None : 
        largest = num
    
    if num == "done":
        break
    
    try :
        int(num)
    except : 
        print("Invalid input")
        continue
    if int(num) > int(largest) :
        largest = num
    if int(num) < int(smallest) :
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)
