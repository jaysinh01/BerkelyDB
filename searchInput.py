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
    print("price completed")


def processPterm(inputArray):
    #TODO: date list will be : [data, data, ...]
    print("pTerm completed")


def processRterm(inputArray):
    #TODO: date list will be : [data, data , ...]
	database = db.DB()
	#database.set_flags(db.DB_DUP)
	#flag = db.DB_BTREE
	database.open("rt.idx")
	curs = database.cursor()
	print(inputArray)
	iter = curs.set_range(inputArray[0].encode("utf-8"))
	#iter = curs.first()
	#print(type(iter))
	#key_to_compare = iter[0].decode("utf-8")
	regex = re.compile(inputArray[0] + '+')
	while iter:
		key_to_compare = iter[0].decode("utf-8")	
		if re.match(regex, key_to_compare):
			print(iter)
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

