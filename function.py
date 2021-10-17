def countWords():
    fileName=input("enter the file name: ")
    print(fileName)
    numberOfWord=0
    file=open(fileName)
    for i in file:
        word=i.split()
        numberOfWord=numberOfWord+len(word)
    print(numberOfWord)
countWords()