
# class of creating IDX from specified file
# types:
# 0: hash
# 1: B+- treee

from bsddb3 import db
import sys

def createIdx(filename, typeSort, outputFile, deli):
	print("its working")
	database = db.DB()
	database.set_flags(db.DB_DUP)
	if (typeSort == 1):
		flag = db.DB_BTREE
	elif(typeSort == 0):
		flag = db.DB_HASH
	
	database.open(outputFile, None,flag, db.DB_CREATE)
	f = open(filename, "r")
	for line in f:
		delIndex = line.find(deli)
		#print("Type of sort: ", typeSort)
		#print("Key: " + line[:delIndex])
		#print("Data: " + line[delIndex+1:])
		key = line[:delIndex].encode('utf-8')
		data = line[delIndex+1:]
		database.put(key, data)
	printDatabase(database)
	f.close()

def printDatabase(database):
	curs = database.cursor()
	iter = curs.first()
	while iter:
		print(iter)
		iter = curs.next()


def readFile(filename, deli):
	print("in the reaFile")
	f = open(filename, "r")
	for line in f:
		delIndex = line.find(deli)
		print("Key: " + line[:delIndex])
	f.close()



def main():
	print("length of input: ")
	print(len(sys.argv))
	print("1: " + sys.argv[1])
	print("2: " + sys.argv[2])
	print("3: " + sys.argv[3])
	print("4: " + sys.argv[4])
	if len(sys.argv) < 5:
		print("The usage of the program:")
		print("python3 ClientIdx.py inputFile outputFile type delimeter")
		print("inputfile '###.txt'")
		print("outputFile '###.idx'")
		print("type '0': Hash '1': B+-")
		print("The column separetor ','")
	else:	
		typeSort = int(sys.argv[3])
		createIdx(sys.argv[1],typeSort,sys.argv[2],sys.argv[4])
		#readFile("rterms_sorted.txt",",")
		print("stupid python")

if __name__ == '__main__':
	main()
