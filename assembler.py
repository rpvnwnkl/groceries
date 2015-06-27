import csv
def readfile(fileName):
    with open(fileName, 'rb') as csvfile:
        foodList = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
        tmpList = []
        for row in foodList:
            tmpList.append(row)
    return tmpList
    
##this object holds all the food 'Item' objects
class Groceries(object):
    def __init__(self, foodList):
        ##creates food object list and puts the Item objects inside row by row
        self.foodObjects = list((Item(row) for row in foodList))
    def getFood(self):
        return self.foodObjects
    def __str__(self):
        return self.foodObjects
    def changeName(self, category, oldName, newName):
        for item in self.getFood():
            if item.sameName(oldName, category):
                item.nameChange(newName, category)
                print oldName+'-->'+newName
        for item in self.getFood():
            if item.sameName(oldName, category):
                print 'found one not fixed'
    def sellerList(self):
        ##searches through dict and pulls unique names and returns them in a list
        tmpList = []
        for item in self.foodObjects:
            if item.getSeller() not in tmpList:
                tmpList.append(item.getSeller())
        tmpList.sort()
        return tmpList

    ##this is a function using object methods to change food category values            
    def nameChange(self, oldName, newName, category):
        self.changeName(category, oldName, newName)
    
##A class is created for food items, which are denoted by each row of the food dictionary
class Item(Groceries):
    def __init__(self, row): ##init local food dict
        self.rowDict = row ##saves the dict format
        self.cats = self.rowDict.keys()##categories are just the dict keys
    def getDict(self):
        return self.rowDict
    def getSeller(self):
        return self.rowDict['Seller']
            
    def __str__(self): ##returns item as a Dict
        return str(self.rowDict.items())
    def __repr__(self):##returns food item object as key, value pairs
        return self.rowDict

    def getCats(self): ##returns list of keys as food categories
        return self.cats

    def nameChange(self, newName, category): ##changes value of given key in food dict
        self.rowDict[category] = newName
        
    def sameName(self, oldName, category): ##check to see if name is the same
        return self.rowDict[category] == oldName

##writes food object to file 
with open('foodList_x.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Amount', 'Measure', 'Cost', 'Seller', 'Date', 'Buyer', 'Category', 'Type']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for item in food.getFood():
        writer.writerow(item.getDict())
