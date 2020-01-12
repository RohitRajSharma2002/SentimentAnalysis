import string

def loadWords():
    # # # # load words from the file # # # #
    posFile = open("C:\\Users\\rohit\\PycharmProjects\\SentimentAnalysis\\__init__\\positiveWords.txt", "r")
    negFile = open("C:\\Users\\rohit\\PycharmProjects\\SentimentAnalysis\\__init__\\negativeWords.txt", "r", errors="ignore")
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
    getSentiment.posCount = 0 
    getSentiment.negCount = 0
    getSentiment.posFlag = {}
    getSentiment.negFlag = {}

    stringToCheck = usrInput.split(" ") # convert user entered string into list
    stringToCheck = [i.rstrip('\n') for i in stringToCheck] #remove newline from user input
    stringToCheck = [i.rstrip(',') for i in stringToCheck]   # remove , from user input
    loadWords.posWords = [i.lower() for i in loadWords.posWords] # normalise words into lowercase
    loadWords.negWords = [i.lower() for i in loadWords.negWords]

    positiveCheck(stringToCheck)
    negativeCheck(stringToCheck)
    checkNegativeContra(stringToCheck)
    checkPositiveContra(stringToCheck)
    print(getSentiment.posCount, getSentiment.negCount)
    try:
        print('postive score ',round(getSentiment.posCount/(getSentiment.posCount+getSentiment.negCount),2))
    except ZeroDivisionError:
        print('positive scroe', 0)
    try:
        print('negative score ',round(getSentiment.negCount/(getSentiment.posCount+getSentiment.negCount),2))
    except ZeroDivisionError:
        print('negative score',0)
        
def positiveCheck(stringToCheck):
    for i in range(0, len(loadWords.posWords)-1):
        for j in range(0, len(stringToCheck)-1):
            if loadWords.posWords[i] == stringToCheck[j]: 
                try:                                    # check if a positive word is followed by a negative word
                    if stringToCheck[j+1] in loadWords.negWords:
                        print('found negative contradictory at', j+1)
                        getSentiment.negCount+=1
                        getSentiment.negFlag[stringToCheck[j+1] + " " + str(j+1)] = 1
                except:
                    pass
            else:
                pass
        

def negativeCheck(stringToCheck):
    for i in range(0, len(loadWords.negWords)-1):
        for j in range(0, len(stringToCheck)-1):
            if loadWords.negWords[i] == stringToCheck[j]:
                try:                                     # check if a negative word is followed by a positive word
                    if stringToCheck[j+1] in loadWords.posWords: 
                        print('found positive contacdictory at', j+1)
                        getSentiment.posCount+=1
                        getSentiment.posFlag[stringToCheck[j+1] + " " + str(j+1)] = 1 

                except:
                    pass

def checkNegativeContra(stringToCheck):
    for word in stringToCheck:
        for i in loadWords.posWords:
            if word.lower() == i.lower(): # check if words ,atch
                if word + " " + str(stringToCheck.index(word)) not in getSentiment.posFlag.keys(): # check if this exact word has been already scanned
                    print('found positive at',stringToCheck.index(word))
                    getSentiment.posCount+=1  
                    getSentiment.posFlag[word + " " + str(stringToCheck.index(word))] = 1  # add the flag


def checkPositiveContra(stringToCheck):
    for word in stringToCheck:
        for i in loadWords.negWords:
            if word.lower() == i.lower():
                if word + " " + str(stringToCheck.index(word)) not in getSentiment.negFlag.keys(): # check if this exact word has been scanned
                    print("found negative at", stringToCheck.index(word))
                    getSentiment.negCount+=1 
                    getSentiment.negFlag[word+" "+ str(stringToCheck.index(word))] = 1   # add the flag
            else:
                pass




loadWords()
usrInput= getString()
getSentiment()
