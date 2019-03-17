import csv
import matplotlib.pyplot as plt
inFileName = "FlightTime.csv"
outPutFile = "ans"
inFile = open(inFileName,'r')
outFile = open(outPutFile, 'w')
a = csv.reader(inFile,delimiter = ',')
next(a)

newList = []
for line in a:
    if int (line[9]) >= 230:
        newList.append(line)   #Number 1

dataCount=len(newList)
print("Total Number of Entries is " + str(dataCount))    #Number 2

def TFT(d, lArr, lDes):
    return .117*d + 0.517*(lArr-lDes)+20
targetFlightTime = TFT(1741.16,-87.90,-118.41)  #Number 3
for row in newList:
    row.append(float(targetFlightTime) + ((int(row[6])+int(row[8]))/2))
print(newList)  #Number 4

car=[]
for row in newList:
    if row[1] not in car:
        car.append(row[1])
ansDict = {}
for name in car:
    ansDict.update({name:0.0})
for key in ansDict:
    tempList=[0,0]
    count=0.0
    for row in newList:
        if key == row[1]:
            tempList[0] += float (row[9])
            tempList[1] += float (row[10])
            count+=1.0
        if count > 0 :
            ans = (tempList[0]-tempList[1])/count
    ansDict[key] += ans
print(ansDict) #Number 5
print(min(ansDict.values())) #Number 5

x=list(ansDict.keys())
y=list(ansDict.values())
plt.bar(x,y)
plt.title("Time Added in Airline Flights")
plt.xlabel("Airline")

plt.ylabel("Time Added in Minutes")
plt.show()