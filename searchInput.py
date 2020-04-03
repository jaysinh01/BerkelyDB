from bsddb3 import db
import re

dateResult = []
scoreResult = []
priceResult = []
pTermResult = []
rTermResult = []


def combineResult():
    #TODO result will be stored in the global variables above
    # find common in all the list and print it
    print("program done")


def processDate(inputArray):
    #TODO: date list will be : [< or> , date , < or> , date, ...]
    # append to a result
    print("date completed")


def processScore(inputArray):
    #TODO: date list will be : [< or> , score , < or> , score, ...]
    print("score completed")


def processPrice(inputArray):
    #TODO: date list will be : [< or> , price , < or> , price, ...]
    database = db.DB()
    database.open("sc.idx")
    curs = database.cursor()
    iter = curs.first
    print(inputArray)
    index = 0;
    while index < len(inputArray):
        if inputArray[index] == "<":
            value = float(iter[0].decode('utf-8'))
            index = index + 1
            compare_value = float(inputArray[index])
            if value <= compare_value:
                
        else:
            
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
    print(pTermResult)

    print("price completed")


def processPterm(inputArray):
    #TODO: date list will be : [data, data, ...]
    database = db.DB()
    database.open("pt.idx")
    curs = database.cursor()
    print(inputArray)
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
    print(pTermResult)

    print("pTerm completed")


def processRterm(inputArray):
    #TODO: date list will be : [data, data , ...]
    database = db.DB()
	#database.set_flags(db.DB_DUP)
	#flag = db.DB_BTREE
    database.open("rt.idx")
    curs = database.cursor()
    print(inputArray)
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
    print("rTerm completed")
    print(rTermResult)
