#function
def Pad (inputFile):
    inputFile = open(inputFile, encoding="utf8")
    text = inputFile.read()
    lines = text.splitlines()
    str=""
    for line in lines:
        str += ("<s> "+line.lower()+" </s>"+'\n')
    return str
    
def tokenFrequency (stringInput):
    tokens = {}
    words = stringInput.split()
    for word in words:
        if word in tokens:
            tokens[word]+=1
        else:
            tokens[word]=1
    return tokens
    
def replaceToUNK(fileText,tokensDic,file):
    #Replacement on current text 
    tokenList = list(tokensDic.keys())

    for word in fileText.split(): #TODO:Fix issue with spacing when replacing words.
            if word in tokenList:
                fileText = fileText.replace(word+" ","<unk>")
    #pdb.set_trace()##DEBUGGER
    #write text changes to file
    inputWriteFile = open(file, "w")
    inputWriteFile.write(fileText)
    inputWriteFile.close()
    return fileText