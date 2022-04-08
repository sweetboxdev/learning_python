fileName = input("Enter File Name:")

try:
    fhandle = open(fileName)
except:
    print("Incorrect file name:", fileName)
    quit()

for line in fhandle :
    newLine = line.rstrip()
    print(newLine.upper())
