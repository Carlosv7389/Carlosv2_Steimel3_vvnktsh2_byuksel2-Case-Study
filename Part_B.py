import csv
#Exercise1
m = 4
p = .5
Exercise1 = p*((3+m*p)/(4+m))*((1+m*p)/(3+m))*((2+m*p)/(3+m))*((1+m*p)/(3+m))
print("P(Delay|SEA,ATL,Southwest,Good) = " + str(Exercise1))
print()
#Exercise2
inFileName = "FlightDelay.csv"
inFile = open(inFileName, 'r')
preList = csv.reader(inFile, delimiter=',')
next(preList)
type(preList)
flightList = []
for line in preList:
    flightList.append(line)
for line in flightList:
    line.append(int(line[3]) + int(line[4]))
    if line[5] < -15:
        line.append("Y")
    else:
        line.append("N")
yes = 0
for line in flightList:
    if 'Y' in line:
        yes += 1
no = len(flightList) - yes


#Exercise 3
def NaiveBayes(airline, origin, destination):
    arguments = [airline, origin, destination]
    answer = [0.5, 0.5]
    for element in arguments:
        tempList = []
        tempYes = 0
        tempNo = 0
        for line in flightList:
            if element in line:
                tempList.append(line)
        for line in tempList:
            if line[6] == 'Y':
                tempYes += 1
        tempNo = len(tempList) - tempYes
        answer[0] *= (tempYes+m*p)/(yes + m)
        answer[1] *= (tempNo+m*p)/(no + m)
    print("P(Delay|" + origin + ', ' + destination + ', ' + airline + ') = ' + str(answer[0]))
    print("P(Notdelay|" + origin + ', ' + destination + ', ' + airline + ') = ' + str(answer[1]))
    print()


NaiveBayes('AA', 'JFK', 'LAS')
NaiveBayes('B6', 'JFK', 'LAS')
NaiveBayes('VX', 'SFO', 'ORD')
NaiveBayes('WN', 'SFO', 'ORD')

