import random
from random import randint
import numpy

tourNumber = 0
totalSpent = 0
panDropped = 0
simsRan = 0
toursTotal = 0
lowestTour = 9999999999999999999999
odds = 0.0
profit = 0
loss = 0
underUserNumber=0
mvmMinTime=25
mvmMaxTime=75 
timePlayed=0

print("v1.4 - Made by Lexzach")
print("\nEnter number of simulations to run: ")
toursToRun = input()
print("Enter max number of tours per simulation (0 for unlimited):")
answer = input()
if answer == "0":
    displayExtra = False
else:
    displayExtra = True
    displayUnder = int(answer)
print("Enter number of tickets required for a tour: ")
ticketsPerTour = input()
print("Enter ticket price (current is $1.01 on Steam Marketplace):")
price = input()
price = price.replace("$", "")
print("Enter golden pan price (current is $4200 on Marketplace.tf): ")
currentPanPrice = input()
currentPanPrice = currentPanPrice.replace("$", "")
price = float(price)
currentPanPrice = float(currentPanPrice)
while simsRan != int(toursToRun):
    tourNumber = 0
    totalSpent = 0
    timePlayed=0
    panDropped = 0
    while panDropped != 1:
        tourNumber+=1
        totalSpent+=float(price)*float(ticketsPerTour)
        timePlayed+=randint(mvmMinTime, mvmMaxTime)
        #print("Tour Number: "+str(tourNumber)+"\nTotal spent: "+str(totalspent))
        if randint(0,10000) == 10000:
            panDropped = 1
    if tourNumber*(price*int(ticketsPerTour)) < currentPanPrice:
        print("\nSimulation #"+str(simsRan)+"\nMoney spent: "+str(round(totalSpent, 2))+"\nTour pan dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*int(ticketsPerTour)))))+", you made $" + str(currentPanPrice - tourNumber*(price*int(ticketsPerTour))) + " in profit.\nTotal estimated time spent playing MVM: "+str(round(timePlayed/60))+" hours")
        profit+=1
    else:
        print("\nSimulation #"+str(simsRan)+"\nMoney spent: "+str(round(totalSpent, 2))+"\nTour pan dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*int(ticketsPerTour)))))+", you lost $" + str(currentPanPrice - tourNumber*(price*int(ticketsPerTour))) + " in profit.\nTotal estimated time spent playing MVM: "+str(round(timePlayed/60))+" hours")
        loss+=1
    if displayExtra == True:
        if tourNumber <= displayUnder:
            underUserNumber+=1
    if tourNumber < lowestTour:
        lowestTour=tourNumber
        lowestTourTime=timePlayed
    simsRan+=1
    toursTotal = toursTotal + tourNumber

odds = numpy.random.binomial(lowestTour, 0.01, None)
cost = round(float(lowestTour*(price*4)))
bestTourPrice = str(round(float(lowestTour*(price*int(ticketsPerTour)))))
profitLoss = str(currentPanPrice - lowestTour*(price*int(ticketsPerTour)))

if round(float(lowestTour*(price*int(ticketsPerTour)))) < currentPanPrice:
    print("\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str((profit/loss)*100)+"%\n\nBest run:\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you made $" + profitLoss + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours")
    if displayExtra == True:
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
else:
    print("\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str((profit/loss)*100)+"%\n\nBest run:\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you lost $" + profitLoss + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours")
    if displayExtra == True:
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
a=input()