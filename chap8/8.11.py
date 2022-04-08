fruits = ['banana','apple','orange','watermelon','kiwi']

copyFruits = fruits[:]

def chop(t) :
    del t[0:1]
    del t[-1:-2]

def middle(t) :
    return t[1:len(t)-1]


chop(fruits)
print("After:",fruits)
print("should be unchanged",copyFruits)
