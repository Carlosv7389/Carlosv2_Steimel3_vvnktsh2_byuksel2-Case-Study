import csv
import matplotlib.pyplot as plt
inFileName = "FlightDelay.csv"
inFile = open(inFileName,'r')
preList = csv.reader(inFile,delimiter = ',')
next(preList)
flightDict={}
flightList = []
for line in preList:
    flightList.append(line)
    #if line[0] not in flightDict:
        #flightDict.update({line[0]:0.0})
#for key in flightDict:
    #for line in flightList:
        #if key == line[0]:
            #flightDict[key] += int(line[3])
            #flightDict[key] += int(line[4])
for line in flightList:
    line.append(int(line[3]) + int(line[4]))
    if line[5] < -15:
        line.append("Y")
    else :
        line.append("N")
for a in flightList:
    print(a)

def f(aLine):
    yes = 0
    no = 0
    set = []
    for line in flightList:
        if line[0] == aLine:
            set.append(line)
    #sublist section works

f('AA')