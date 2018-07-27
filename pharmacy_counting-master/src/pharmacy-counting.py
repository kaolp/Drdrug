import csv
from decimal import Decimal
drugNameDict={}
with open ('..\input\itcont.txt', 'r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        myDrugName=row['drug_name']
        idDict={}
        if(myDrugName in drugNameDict):
            idDict=drugNameDict.get(myDrugName)
            idDict[row['id']]=row['drug_cost']
        else:
            idDict[row['id']]=row['drug_cost']
            drugNameDict[row['drug_name']]=idDict
for drugName in drugNameDict:
    idDict=drugNameDict.get(drugName)
    totalCost=0
    count=0    
    for id in idDict:
        count=count + 1
        drugCost=idDict.get(id)
        totalCost=totalCost + Decimal(drugCost)
    print (drugName + ',' + str (count) + ',' + str(totalCost))
