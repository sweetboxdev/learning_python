fhand = open('mbox-short.txt')

count = 0
for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    print(words[2])
