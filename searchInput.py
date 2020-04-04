from bsddb3 import db
import re
from functools import reduce

dateResult = []
scoreResult = []
priceResult = []
pTermResult = []
rTermResult = []

def printResult(result, fullOutput):
    #review id, the product title and the review score
    database = db.DB()
    database.open("rw.idx")
    curs = database.cursor()
    #print(result)
    #fullOutput = True
    for key in result:
        iter = curs.first()
        while iter:
            it = iter[0].decode("utf-8")
            if key == it:
                if fullOutput:
                    print(iter[0].decode("utf-8"), end =",")
                    print(iter[1].decode("utf-8"))
                    
                else:
                    row = iter[1].decode("utf-8")
                    listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
                    print(iter[0].decode("utf-8"), end =",")
                    print(listRow[1], end =",")
                    print(listRow[6])
            iter = curs.next()
                
    #print(scoreResult)
    curs.close()
    database.close()



def combineResult(dateArray, priceArray):
    #TODO result will be stored in the global variables above
    # find common in all the list and print it
    # TODO result will be stored in the global variables above
    # find common in all the list and print it
    global pTermResult, rTermResult
    #pTermResult.append("fuck")
    combinedList = [pTermResult, rTermResult]
    # common element extraction form N lists
    # using reduce() + lambda + set()
    #result = list(reduce(lambda i, j: i & j, (set(x) for x in combinedList)))
    
    #print(list(set.intersection(*(set(x) for x in [pTermResult, rTermResult] if x))))
    #comb = filter(None, [pTermResult,rTermResult, scoreResult])
    #if comb == None:
       # print("everything empty")
        #parseEverything(dateArray, priceArray)
        
    #else:
        #result = list(set.intersection(*map(set,comb)))
        #parsePartial(dateArray, priceArray, result)
    #parseEverything(dateArray, priceArray)
        
    # printing result
   # print(pTermResult, rTermResult)
    #print ("RESULT: " + str(result) + "\n")
    print("program done")
    
def parsePartial(dateArray, priceArray, result):
    for id in result:
        iter = curs.get(id.encode("utf-8"))
        
        nFlag = False
        cFlag = False
        rFlag = True
        if index >= len(dateArray):
            if index != 0:
                break
        elif index >= len(priceArray):
            if index != 0:
                break
        while iter:
            print("im stuck")
            row = iter[1].decode("utf-8")
            listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
            if len(dateArray) != 0:
                if dateArray[index] == "<":
                    key_to_compare = float(listRow[7])
                    if key_to_compare < dateArray[index + 1]:
                        cFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
                elif dateArray[index] == ">":
                    key_to_compare = float(listRow[7])
                    if key_to_compare > dateArray[index + 1]:
                        cFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
            else:
                cFlag = True
            if len(priceArray) != 0:
                if priceArray[index] == "<":
                    try:
                        key_to_compare = float(listRow[2])
                    except:
                        iter = curs.next()
                        continue
                    if key_to_compare < priceArray[index + 1]:
                        nFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
                elif priceArray[index] == ">":
                    key_to_compare = float(listRow[2])
                    if key_to_compare > priceArray[index + 1]:
                        nFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
            else:
                nFlag = True
            if nFlag and cFlag:
                print("sucess")
                print(iter)
                #index = index + 2
                iter = curs.next()
        index = index + 2
            
    curs.close()
    database.close()

        

def parseEverything(dateArray, priceArray):
    database = db.DB()
    database.open("rw.idx")
    curs = database.cursor()
    
    index = 0

    #row = iter[1].decode("utf-8")
    #listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
    while True:
        iter = curs.first()
        nFlag = False
        cFlag = False
        rFlag = True
        if index >= len(dateArray):
            if index != 0:
                break
        elif index >= len(priceArray):
            if index != 0:
                break
        while iter:
            print("im stuck")
            row = iter[1].decode("utf-8")
            listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
            if len(dateArray) != 0:
                if dateArray[index] == "<":
                    key_to_compare = float(listRow[7])
                    if key_to_compare < dateArray[index + 1]:
                        cFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
                elif dateArray[index] == ">":
                    key_to_compare = float(listRow[7])
                    if key_to_compare > dateArray[index + 1]:
                        cFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
            else:
                cFlag = True
            if len(priceArray) != 0:
                if priceArray[index] == "<":
                    try:
                        key_to_compare = float(listRow[2])
                    except:
                        iter = curs.next()
                        continue
                    if key_to_compare < priceArray[index + 1]:
                        nFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
                elif priceArray[index] == ">":
                    key_to_compare = float(listRow[2])
                    if key_to_compare > priceArray[index + 1]:
                        nFlag = True
                    else:
                        #index = index + 2
                        iter = curs.next()
                        continue
            else:
                nFlag = True
            if nFlag and cFlag:
                print("sucess")
                print(iter)
                #index = index + 2
                iter = curs.next()
        index = index + 2
            
    curs.close()
    database.close()

def processDate(inputArray, dateRes):
    database = db.DB()
    #global dateResult
    dateResult = []
    #database.set_flags(db.DB_DUP)
    #flag = db.DB_BTREE
    database.open("rw.idx")
    curs = database.cursor()
    #print(inputArray)
    #iter = curs.first()
    #print(type(iter))
    #key_to_compare = iter[0].decode("utf-8")
    index = 0
    while index < len(inputArray):
        iter = curs.first()
        while iter:
            row = iter[1].decode("utf-8")
            listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
            if inputArray[index] == "<":
                key_to_compare = float(listRow[7])
                if key_to_compare < inputArray[index + 1]:
                    dateResult.append(iter[0].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
            elif inputArray[index] == ">":
                key_to_compare = float(listRow[7])
                if key_to_compare > inputArray[index + 1]:
                    dateResult.append(iter[0].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
        index = index + 2
    curs.close()
    database.close()
    #while iter:
     #   print(iter)
      #  iter = curs.next()
    #value.decode("utf-8")
    #print("Date completed")
    #print(dateResult)
    #return dateResult
    dateRes[:] = dateResult



def processScore(inputArray, mlist):
    #TODO: date list will be : [< or> , score , < or> , score, ...]
    database = db.DB()
    #global scoreResult
    scoreResult = []
    #database.set_flags(db.DB_DUP)
    #flag = db.DB_BTREE
    database.open("sc.idx")
    curs = database.cursor()
    #print(inputArray)
    #iter = curs.first()
    #print(type(iter))
    #key_to_compare = iter[0].decode("utf-8")
    index = 0
    while index < len(inputArray):
        iter = curs.first()
        while iter:
            if inputArray[index] == "<":
                try:
                    key_to_compare = float(iter[0])
                except:
                    iter = curs.next()
                    continue
                if key_to_compare < inputArray[index + 1]:
                    scoreResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
            elif inputArray[index] == ">":
                try:
                    key_to_compare = float(iter[0])
                except:
                    iter = curs.next()
                    continue
                if key_to_compare > inputArray[index + 1]:
                    scoreResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
        index = index + 2
    curs.close()
    database.close()

    #print("score completed")
    #print(scoreResult)
    mlist[:] = scoreResult
    #print(mlist[:])
    #return scoreResult



def processPrice(inputArray, priceRes):
    #TODO: date list will be : [< or> , price , < or> , price, ...]
    database = db.DB()
    #global priceResult
    priceResult = []
    #database.set_flags(db.DB_DUP)
    #flag = db.DB_BTREE
    database.open("rw.idx")
    curs = database.cursor()
    #print(inputArray)
    #iter = curs.first()
    #print(type(iter))
    #key_to_compare = iter[0].decode("utf-8")
    index = 0
    while index < len(inputArray):
        iter = curs.first()
        while iter:
            row = iter[1].decode("utf-8")
            listRow = re.split(r',(?=(?:(?:[^"]*"){2})*[^"]*$)', row)
            if inputArray[index] == "<":
                try:
                    key_to_compare = float(listRow[2])
                except:
                    iter = curs.next()
                    continue
                if key_to_compare < inputArray[index + 1]:
                    priceResult.append(iter[0].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
            elif inputArray[index] == ">":
                try:
                    key_to_compare = float(listRow[2])
                except:
                    iter = curs.next()
                    continue
                if key_to_compare > inputArray[index + 1]:
                    priceResult.append(iter[0].decode("utf-8"))
                    iter = curs.next()
                else:
                    #index = index + 2
                    iter = curs.next()
                    continue
        index = index + 2
    curs.close()
    database.close()

    #print("price completed")
    #print(priceResult)
    #return priceResult
    priceRes[:] = priceResult


def processPterm(inputArray, pTermRes):
    #TODO: date list will be : [data, data, ...]
    #global pTermResult
    pTermResult = []
    database = db.DB()
    database.open("pt.idx")
    curs = database.cursor()
    #print(inputArray)
    for term in inputArray:
        if term[-1] == "%":
            regex = re.compile(term[:-1])
            iter = curs.set_range(term[:-1].encode("utf-8"))
            while iter:
                key_to_compare = iter[0].decode("utf-8")
                if re.match(regex, key_to_compare):
                    pTermResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    break
            
        else:
            iter = curs.set_range(term.encode("utf-8"))
            while iter:
                key_to_compare = iter[0].decode("utf-8")
                if term == key_to_compare:
                    pTermResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    break
    curs.close()
    database.close()
    #print(pTermResult)

    #print("pTerm completed")
    #return pTermResult
    pTermRes[:] = pTermResult


def processRterm(inputArray, rTermRes):
    #TODO: date list will be : [data, data , ...]
    database = db.DB()
    #global rTermResult
    rTermResult = []
	#database.set_flags(db.DB_DUP)
	#flag = db.DB_BTREE
    database.open("rt.idx")
    curs = database.cursor()
    #print(inputArray)
	#iter = curs.first()
	#print(type(iter))
	#key_to_compare = iter[0].decode("utf-8")
    for term in inputArray:
        if term[-1] == "%":
            regex = re.compile(term[:-1])
            iter = curs.set_range(term[:-1].encode("utf-8"))
            while iter:
                key_to_compare = iter[0].decode("utf-8")
                if re.match(regex, key_to_compare):
                    #print(iter)
                    rTermResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    break
			
        else:
            iter = curs.set_range(term.encode("utf-8"))
            while iter:
                key_to_compare = iter[0].decode("utf-8")
                if term == key_to_compare:
                    #print(iter)
                    rTermResult.append(iter[1].decode("utf-8"))
                    iter = curs.next()
                else:
                    break
    curs.close()
    database.close()
    #while iter:
     #   print(iter)
      #  iter = curs.next()
    #value.decode("utf-8")
    #print("rTerm completed")
    #print(rTermResult)
    #return rTermResult
    rTermRes[:] = rTermResult
