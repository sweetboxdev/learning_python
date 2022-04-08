spamScore = 0.0
spamCount = 0

fnameInput = input("Enter file name:")
try:
    fhandle = open(fnameInput)
except:
    print("Wrong file name:", fnameInput)
    quit()

for line in fhandle :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    nline = line.split()
    lscore = float(nline.pop(1))
    spamScore = spamScore + lscore
    spamCount = spamCount + 1

print("Average spam confidence:", spamScore/spamCount)


