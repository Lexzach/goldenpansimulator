import random
from random import randint
import numpy

price = 1.01
tourNumber = 0
totalSpent = 0
panDropped = 0
simsRan = 0
toursTotal = 0
lowestTour = 9999999999999999999999
odds = 0.0
currentPanPrice = 4200
print("Enter number of simulations to run: ")
x = input()

while simsRan != int(x):
    tourNumber = 0
    totalSpent = 0
    panDropped = 0
    while panDropped != 1:
        tourNumber+=1
        totalSpent=totalSpent + (price*4)
        #print("Tour Number: "+str(tourNumber)+"\nTotal spent: "+str(totalspent))
        if randint(0,10000) == 10000:
            panDropped = 1
    if tourNumber*(price*4) < currentPanPrice:
        print("\nPan dropped!"+"\nSimulation #"+str(simsRan)+"\nFinal Numbers:\nMoney spent - "+str(round(totalSpent, 2))+"\nTour Number - "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*4))))+", you made $" + str(currentPanPrice - tourNumber*(price*4)) + " in profit.")
    else:
        print("\nPan dropped!"+"\nSimulation #"+str(simsRan)+"\nFinal Numbers:\nMoney spent - "+str(round(totalSpent, 2))+"\nTour Number - "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(round(float(tourNumber*(price*4))))+", you lost $" + str(currentPanPrice - tourNumber*(price*4)) + " in profit.")
    if tourNumber < lowestTour:
        lowestTour=tourNumber
    simsRan+=1
    toursTotal = toursTotal + tourNumber

odds = numpy.random.binomial(lowestTour, 0.01, None)
cost = round(float(lowestTour*(price*4)))
if round(float(lowestTour*(price*4))) < currentPanPrice:
    print("\nSim finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%.\nLowest tour that pan dropped: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(cost)+", you made $" + str(currentPanPrice - cost) + " in profit.\nOdds of getting a pan on your #"+str(lowestTour)+" run: "+str(float(odds))+"%")
else:
    print("\nSim finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str((simsRan/toursTotal)*100)+"%"+". The actual drop rate is 0.01%.\nLowest tour that pan dropped: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(cost)+", you lost $" + str(currentPanPrice - cost) + " in profit.\nOdds of getting a pan on your #"+str(lowestTour)+" run: "+str(float(odds))+"%")

a=input()