inputString = input("Please enter string:")
inputLetter = input("Please enter letter:")

def letterCounter(string,letter) :
    lc = 0
    for x in string :
        if x == letter :
            lc = lc +1
    return(lc)

print("The word", inputString, "has the letter", inputLetter, letterCounter(inputString,inputLetter), "times in it.")




