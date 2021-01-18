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

print("v1.2 - Made by Lexzach")
print("\nEnter number of simulations to run: ")
toursToRun = input()
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
    panDropped = 0
    while panDropped != 1:
        tourNumber+=1
        totalSpent+=float(price)*float(ticketsPerTour)
        #print("Tour Number: "+str(tourNumber)+"\nTotal spent: "+str(totalspent))
        if randint(0,10000) == 10000:
            panDropped = 1
    if tourNumber*(price*int(ticketsPerTour)) < currentPanPrice:
        print("\nSimulation #"+str(simsRan)+"\nMoney spent: "+str(round(totalSpent, 2))+"\nTour pan dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*int(ticketsPerTour)))))+", you made $" + str(currentPanPrice - tourNumber*(price*int(ticketsPerTour))) + " in profit.")
        profit+=1
    else:
        print("\nSimulation #"+str(simsRan)+"\nMoney spent: "+str(round(totalSpent, 2))+"\nTour pan dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*int(ticketsPerTour)))))+", you lost $" + str(currentPanPrice - tourNumber*(price*int(ticketsPerTour))) + " in profit.")
        loss+=1
    if tourNumber < lowestTour:
        lowestTour=tourNumber
    simsRan+=1
    toursTotal = toursTotal + tourNumber

odds = numpy.random.binomial(lowestTour, 0.01, None)
cost = round(float(lowestTour*(price*4)))
if round(float(lowestTour*(price*int(ticketsPerTour)))) < currentPanPrice:
    print("\nSim finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str((profit/loss)*100)+"%\n\nBest run:\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(cost)+", you made $" + str(currentPanPrice - cost) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%")
else:
    print("\nSim finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str((profit/loss)*100)+"%\n\nBest run:\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(cost)+", you lost $" + str(currentPanPrice - cost) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%")

a=input()