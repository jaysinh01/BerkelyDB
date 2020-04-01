import re
import multiprocessing
import searchInput as search

#globalIndex = 0;
#inputArray = []
fullOutput = False
dateArray = []
scoreArray = []
priceArray = []
pTermArray = []
rTermArray = []


def splitInput(inputString):
    #global globalIndex
    globalIndex = 0
    inputArray = re.findall(r'[^:><\s]+|[:><]', inputString)
    predicateQuery = False
    try:
        while globalIndex <= len(inputArray) - 1:
            element = inputArray[globalIndex]
            if element == "date":
                dateQuery(inputArray[globalIndex + 1], inputArray[globalIndex + 2])
                globalIndex = globalIndex + 2
            elif element == "price":
                priceQuery(inputArray[globalIndex + 1], inputArray[globalIndex + 2])
                globalIndex = globalIndex + 2
            elif element == "score":
                scoreQuery(inputArray[globalIndex + 1], inputArray[globalIndex + 2])
                globalIndex = globalIndex + 2
            elif element == "pterm":
                generalQuery(0, inputArray[globalIndex + 2])
                globalIndex = globalIndex + 2
            elif element == "rterm":
                generalQuery(1, inputArray[globalIndex + 2])
                globalIndex = globalIndex + 2
            else:
                generalQuery(2, element)
            globalIndex = globalIndex + 1

        # result = element.find("<")
        # result = element.find("<") if result == -1:
        # result = element.find("<")     element.find(">")
        # if result != -1:

        # result = element.find("<") if element[-1] == "<" or element[-1] == ">":
        # result = element.find("<")     globalIndex = globalIndex + 1
        # result = element.find("<")     data = inputArray[globalIndex]
        # result = element.find("<")     findPrefix(element[:-1], element[-1], data)
        # result = element.find("<") elif globalIndex != len(inputArray) - 1:
        # result = element.find("<")    globalIndex = globalIndex + 1
        # result = element.find("<")    predicate = inputArray[globalIndex]
        # result = element.find("<")    if predicate == "<" or predicate == ">":
        # result = element.find("<")        globalIndex = globalIndex + 1
        # result = element.find("<")        data = inputArray[globalIndex]
        # result = element.find("<")        findPrefix(element, predicate, data)
        # result = element.find("<")    else:
        # result = element.find("<")        globalIndex = globalIndex - 1
        # result = element.find("<") globalIndex = globalIndex + 1
        # else:
    except:
        print("Error in input query")


def dateQuery(predicate, data):
    dateArray.append(predicate)
    dateArray.append(data)


def priceQuery(predicate, data):
    priceArray.append(predicate)
    priceArray.append(data)


def scoreQuery(predicate, data):
    scoreArray.append(predicate)
    scoreArray.append(data)


def generalQuery(flag, data):
    if flag == 0:
        pTermArray.append(data)
    elif flag == 1:
        rTermArray.append(data)
    elif flag == 2:
        pTermArray.append(data)
        rTermArray.append(data)


def findPrefix(element, predicate, data):
    if element == "date":
        dateArray.append(element)
        dateArray.append(predicate)
        dateArray.append(data)
    elif element == "score":
        scoreArray.append(element)
        scoreArray.append(predicate)
        scoreArray.append(data)
    elif element == "price":
        priceArray.append(element)
        priceArray.append(predicate)
        predicate.append(data)


def processInput():
    #https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba

    processes = []

    if dateArray:
        p = multiprocessing.Process(target=search.processDate, args=(dateArray,))
        processes.append(p)
        p.start()
    if scoreArray:
        p = multiprocessing.Process(target=search.processScore, args=(scoreArray,))
        processes.append(p)
        p.start()
    if priceArray:
        p = multiprocessing.Process(target=search.processPrice, args=(priceArray,))
        processes.append(p)
        p.start()
    if pTermArray:
        p = multiprocessing.Process(target=search.processPterm, args=(pTermArray,))
        processes.append(p)
        p.start()
    if rTermArray:
        p = multiprocessing.Process(target=search.processRterm, args=(rTermArray,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    search.combineResult()


if __name__ == '__main__':
    inputString = raw_input("Please enter your query: ")
    global fullOutput
    if inputString == "output=full":
       fullOutput = True
    elif inputString == "output=brief":
        fullOutput = False
    print(inputString)
    # inputArray = re.split(r'\s*(:|>|<) \s*', inputString)
    # inputArray = re.findall(r'[^:><\s]+|[:><]', inputString)
   #print(inputArray)
    splitInput(inputString)
    # global dateArray
    # global scoreArray
    # global priceArray
    processInput()
    print(dateArray)
    print(scoreArray)
    print(priceArray)
    print(pTermArray)
    print(rTermArray)
