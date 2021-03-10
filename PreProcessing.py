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
    
def replaceToUNK(file,TokensList):
    #open the file and get text
    inputFile = open(file, encoding="utf8")
    fileText = inputFile.read()
    pdb.set_trace()##DEBUGGER
    #do replacement on current text 
    for token in TokensList.keys():
            fileText = fileText.replace(token,"<unk>")#TODO:defined its token key and not value we are using
    
    inputFile.close()
    
    #write text changes to file
    inputWriteFile = open(file, "w")
    inputWriteFile.write(fileText)
    inputWriteFile.close()
    return fileText