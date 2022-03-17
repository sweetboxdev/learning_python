hourlyRate = float(input("What's the hourly rate?:"))
hoursWorked = float(input("What's the hours worked?:"))

def computepay(h,r):
    if h > 40:
        npay = 40 * r
        opay = (h - 40) * (r*1.5)
        return(npay + opay)
    else:
        return(h*r)
print("Pay ",computepay(hoursWorked,hourlyRate))

    
