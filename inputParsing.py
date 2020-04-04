import re
import multiprocessing
import searchInput as search
from bsddb3 import db
import time
import datetime

#globalIndex = 0;
#inputArray = []
fullOutput = False
dateArray = []
scoreArray = []
priceArray = []
pTermArray = []
rTermArray = []

def printDatabase():
    database = db.DB()
    database.open("rw.idx")
    curs = database.cursor()
    iter = curs.first()
    while iter:
        print(iter)
        iter = curs.next()
    
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
    #print("made it")
    t = time.mktime(datetime.datetime.strptime(data, "%Y/%m/%d").timetuple())
    #print(" did not made it")
    #print(type(t))
    dateArray.append(t)
    #print(dateArray)


def priceQuery(predicate, data):
    priceArray.append(predicate)
    fd = float(data)
    priceArray.append(fd)
    #print(priceArray)


def scoreQuery(predicate, data):
    scoreArray.append(predicate)
    fd = float(data)
    scoreArray.append(fd)


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
    global dateArray
    global scoreArray
    global priceArray
    global pTermArray
    global rTermArray
    processes = []
    comb = []
    scoreRes = []
    
    manager = multiprocessing.Manager()
    dateRes = manager.list()
    
    manager = multiprocessing.Manager()
    mlist = manager.list()
    
    manager = multiprocessing.Manager()
    priceRes = manager.list()
    
    manager = multiprocessing.Manager()
    pTermRes = manager.list()
    
    manager = multiprocessing.Manager()
    rTermRes = manager.list()
    
    if dateArray:
        #dateRes = search.processDate(dateArray)
        #if dateRes:
        #    comb.append(dateRes)
        p = multiprocessing.Process(target=search.processDate, args=(dateArray,dateRes))
        processes.append(p)
        p.start()
    if scoreArray:
        #scoreRes = search.processScore(scoreArray)
        p = multiprocessing.Process(target=search.processScore, args=(scoreArray,mlist))
        processes.append(p)
        p.start()
    if priceArray:
        #priceRes = search.processPrice(priceArray)
        #if priceRes:
        #    comb.append(priceRes)
        p = multiprocessing.Process(target=search.processPrice, args=(priceArray,priceRes))
        processes.append(p)
        p.start()
    if pTermArray:
        #pTermRes = search.processPterm(pTermArray)
        #if pTermRes:
        #    comb.append(pTermRes)
        p = multiprocessing.Process(target=search.processPterm, args=(pTermArray,pTermRes))
        processes.append(p)
        p.start()
    if rTermArray:
        #print("im here")
        #rTermRes = search.processRterm(rTermArray)
        #if rTermRes:
        #    comb.append(rTermRes)
        p = multiprocessing.Process(target=search.processRterm, args=(rTermArray,rTermRes))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    if mlist[:]:
        comb.append(mlist[:])
        del mlist[:]
        scoreArray[:] = []
    if rTermRes[:]:
        comb.append(rTermRes[:])
        del rTermRes[:]
        rTermArray[:] = []
    if pTermRes[:]:
        comb.append(pTermRes[:])
        del pTermRes[:]
        pTermArray[:] = []
    if priceRes[:]:
        comb.append(priceRes[:])
        del priceRes[:]
        priceArray[:] = []
    if dateRes[:]:
        comb.append(dateRes[:])
        del dateRes[:]
        dateArray[:] = []

    result = list(set.intersection(*map(set,comb)))
    #print("PRINTING RESULT")
    #print(result)

    #search.combineResult(dateArray, priceArray)
    
    return result


if __name__ == '__main__':
    fullOutput = False
    while True:
        inputString = input("Please enter your query: ")
        
        if inputString == "output=full":
           fullOutput = True
           print("Output mode switched to full")
           continue
        elif inputString == "output=brief":
            print("Output mode switched to partial")
            fullOutput = False
            continue
        #print(inputString)
        # inputArray = re.split(r'\s*(:|>|<) \s*', inputString)
        # inputArray = re.findall(r'[^:><\s]+|[:><]', inputString)
        #print(inputArray)
        try:
            splitInput(inputString)
        except:
            print("Error in Query Pasrsing. Please Try Again")
            continue
        try:
            result = processInput()
            search.printResult(result, fullOutput)
        except:
            print("No matching query. Try Again")
                continue

