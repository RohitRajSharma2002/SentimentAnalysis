import string

def loadWords():
    # # # # load words from the file # # # #
    posFile = open("\positiveWords.txt", "r")
    negFile = open("negativeWords.txt", "r", errors="ignore")
    loadWords.posWords = posFile.readlines()
    loadWords.posWords = [i.rstrip("\n") for i in loadWords.posWords]
    loadWords.negWords = negFile.readlines()
    loadWords.negWords = [i.rstrip("\n") for i in loadWords.negWords] # remove newline charecters from the words
    negFile.close()
    posFile.close()
    print("words imported")

def getString():
    usrString = input("enter string\t")
    return usrString

def getSentiment():
    posCount = 0 
    negCount = 0
    posFlag = {}
    negFlag = {}

    stringToCheck = usrInput.split(" ") # convert user entered string into list
    stringToCheck = [i.rstrip('\n') for i in stringToCheck] #remove newline from user input
    stringToCheck = [i.rstrip(',') for i in stringToCheck]   # remove , from user input
    loadWords.posWords = [i.lower() for i in loadWords.posWords] # normalise words into lowercase
    loadWords.negWords = [i.lower() for i in loadWords.negWords]
        

    for i in range(0, len(loadWords.posWords)-1):
        for j in range(0, len(stringToCheck)-1):
            if loadWords.posWords[i] == stringToCheck[j]: 
                try:                                    # check if a positive word is followed by a negative word
                    if stringToCheck[j+1] in loadWords.negWords:
                        print('found negative contradictory at', j+1)
                        negCount+=1
                        negFlag[stringToCheck[j+1] + " " + str(j+1)] = 1
                except:
                    pass
            else:
                pass
    for i in range(0, len(loadWords.negWords)-1):
        for j in range(0, len(stringToCheck)-1):
            if loadWords.negWords[i] == stringToCheck[j]:
                try:                                     # check if a negative word is followed by a positive word
                    if stringToCheck[j+1] in loadWords.posWords: 
                        print('found positive contacdictory at', j+1)
                        posCount+=1
                        posFlag[stringToCheck[j+1] + " " + str(j+1)] = 1 

                except:
                    pass

    for word in stringToCheck:
        for i in loadWords.posWords:
            if word.lower() == i.lower(): # check if words ,atch
                if word + " " + str(stringToCheck.index(word)) not in posFlag.keys(): # check if this exact word has been already scanned
                    print('found positive at',stringToCheck.index(word))
                    posCount+=1  
                    posFlag[word + " " + str(stringToCheck.index(word))] = 1  # add the flag

    for word in stringToCheck:
        for i in loadWords.negWords:
            if word.lower() == i.lower():
                if word + " " + str(stringToCheck.index(word)) not in negFlag.keys(): # check if this exact word has been scanned
                    print("found negative at", stringToCheck.index(word))
                    negCount+=1 
                    negFlag[word+" "+ str(stringToCheck.index(word))] = 1   # add the flag
            else:
                pass

    print(posCount, negCount)
    try:
        print('postive score ',round(posCount/(posCount+negCount),2))
    except ZeroDivisionError:
        print('positive scroe', 0)
    try:
        print('negative score ',round(negCount/(posCount+negCount),2))
    except ZeroDivisionError:
        print('negative score',0)
    print(posFlag, negFlag)

loadWords()
usrInput= getString()
getSentiment()