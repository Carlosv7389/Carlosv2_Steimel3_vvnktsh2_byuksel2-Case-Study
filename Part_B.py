import csv
#Exercise1
m = 4
# Naive-Bayes Equation repreated product of ((nHat + m*p)/(n + m)) = P(xi|Ck)
Exercise1Y = (.5)*((3+m*(1/2))/(4+m))*((1+m*(1/2))/(3+m))*((2+m*(1/3))/(3+m))*((1+m*(1/2))/(3+m)) #Calculating probability of a delay
Exercise1N = (.5)*((1+m*(1/2))/(4+m))*((2+m*(1/2))/(3+m))*((1+m*(1/3))/(3+m))*((2+m*(1/2))/(3+m)) #Calculating probability of no delay
print("Exercise 1")
print((Exercise1Y,Exercise1N))
if Exercise1Y > Exercise1N:
    print("The flight will be delayed")
else:
    print("The flight will not be delayed")
print()
print()
print("Exercise 3")


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
    if line[5] > 15:
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
    arguments = [airline, origin, destination] # Setting up a list of our arguments to iterate through
    answer = [0.5, 0.5]
    probList=[]
    for i in range(3):
        counterList=[]
        for line in flightList:
            counterList.append(line[i])
        probList.append(1/len(list(dict.fromkeys(counterList))))
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
        answer[0] *= (tempYes+m*(probList[arguments.index(element)]))/(yes + m)
        answer[1] *= (tempNo+m*(probList[arguments.index(element)]))/(no + m)
    print("P(Delay|" + origin + ', ' + destination + ', ' + airline + ') = ' + str(answer[0]))
    print("P(Notdelay|" + origin + ', ' + destination + ', ' + airline + ') = ' + str(answer[1]))
    print()


NaiveBayes('AA', 'JFK', 'LAS')
NaiveBayes('B6', 'JFK', 'LAS')
NaiveBayes('VX', 'SFO', 'ORD')
NaiveBayes('WN', 'SFO', 'ORD')

