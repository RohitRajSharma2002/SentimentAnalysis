import string

def loadWords():
    # # # # load words from the file # # # #
    posFile = open("positiveWords.txt", "r")
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
    getSentiment.posCount = 0 
    getSentiment.negCount = 0
    getSentiment.posFlag = {}
    getSentiment.negFlag = {}

    stringToCheck = usrInput.split(" ") # convert user entered string into list
    stringToCheck = [i.rstrip('\n') for i in stringToCheck] #remove newline from user input
    stringToCheck = [i.rstrip(',') for i in stringToCheck]   # remove , from user input
    loadWords.posWords = [i.lower() for i in loadWords.posWords] # normalise words into lowercase
    loadWords.negWords = [i.lower() for i in loadWords.negWords]
    checkDuplicates(stringToCheck)
    checkNegativeContra(stringToCheck)
    checkPositiveContra(stringToCheck)
    checkPositive(stringToCheck)
    checkNegative(stringToCheck)
    print(getSentiment.posCount, getSentiment.negCount)
    try:
        print('postive score ',round(getSentiment.posCount/(getSentiment.posCount+getSentiment.negCount),2))
    except ZeroDivisionError:
        print('positive scroe', 0)
    try:
        print('negative score ',round(getSentiment.negCount/(getSentiment.posCount+getSentiment.negCount),2))
    except ZeroDivisionError:
        print('negative score',0)
    print(getSentiment.posFlag, getSentiment.negFlag)
        
def checkNegativeContra(stringToCheck):
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
        

def checkPositiveContra(stringToCheck):
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

def checkPositive(stringToCheck):
    for word in stringToCheck:
        try:
            int(word[-1])   # check if the word had an inetger label at the end
        except:     # if it does not do this
            for i in loadWords.posWords:
                if word.lower() == i.lower(): # check if words ,atch
                    if word + " " + str(stringToCheck.index(word)) not in getSentiment.posFlag.keys(): # check if this exact word has been already scanned
                        print('found positive at',stringToCheck.index(word))
                        getSentiment.posCount+=1  
                        getSentiment.posFlag[word + " " + str(stringToCheck.index(word))] = 1  # add the flag
             
        else:  # else modify the word to check only letters and compare
            for i in loadWords.posWords:
                if word[0:-1].lower() == i.lower(): # check if words ,atch
                    if word + " " + str(stringToCheck.index(word)) not in getSentiment.posFlag.keys(): # check if this exact word has been already scanned
                        print('found positive at',stringToCheck.index(word))
                        getSentiment.posCount+=1  
                        getSentiment.posFlag[word + " " + str(stringToCheck.index(word))] = 1  # add the flag

def checkNegative(stringToCheck):
    for word in stringToCheck:
        for i in loadWords.negWords:
            try:    # check if thr word has en inetger label
                int(word[-1])
            except:   # if it doesnt comapre the words 
                    if word.lower() == i.lower():
                        if word + " " + str(stringToCheck.index(word)) not in getSentiment.negFlag.keys(): # check if this exact word has been scanned
                            print("found negative at", stringToCheck.index(word))
                            getSentiment.negCount+=1 
                            getSentiment.negFlag[word+" "+ str(stringToCheck.index(word))] = 1   # add the flag
            else:    # if it dows mdofiy thr word and comapre
                if word[0:-1].lower() == i.lower():
                    if word + " " + str(stringToCheck.index(word)) not in getSentiment.negFlag.keys(): # check if this exact word has been scanned
                        print("found negative at", stringToCheck.index(word))
                        getSentiment.negCount+=1 
                        getSentiment.negFlag[word+" "+ str(stringToCheck.index(word))] = 1   # add the flag

        

def checkDuplicates(stringToCheck):
    ''' check if recurrances of words exixtx,
        if they do then add a counter and their end and modify the word     
    '''
    counter = 1
    for i in range(0, len(stringToCheck)):
        if stringToCheck.count(stringToCheck[i]) > 1:
            stringToCheck[i] = stringToCheck[i] + str(counter)
            counter+=1


loadWords()
usrInput= getString()
getSentiment()
