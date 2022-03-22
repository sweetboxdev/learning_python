hoursWorked = float(input("Hours worked:"))
hoursRate = float(input("Hourly rate:"))
overtimeRate = (hoursRate * 1.5)
hoursOvertime = hoursWorked - 40

if hoursOvertime > 0:
    print((((hoursWorked - hoursOvertime) * hoursRate) + (hoursOvertime * overtimeRate)))
else:
    print(hoursWorked * hoursRate)

