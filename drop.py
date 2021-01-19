import random
from random import randint, randrange
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
mostProfit = 0
mvmMinTime=25
mvmMaxTime=75 
timePlayed=0
weapons = ["Ambassador", "Axtinguisher", "Black Box", "Blutsauger", "Flame Thrower", "Force-A-Nature", "Frontier Justice", "Grenade Launcher", "Knife", "Medi-Gun", "Minigun", "Rocket Launcher", "Scattergun", "SMG", "Sniper Rifle", "Stickybomb Launcher", "Tomislav", "Wrench", "Eyelander"]
values = [15.92, 10.25, 19.26, 9.27, 32.62, 20.5, 21.74, 27.96, 30.44, 97.07, 33.55, 67.56, 57.46, 11.8, 46.13, 31.92, 32.3, 68.34, 76.1]
chance = [2.51,2.66,3.12,2.75,2.51,2.89,2.69,2.08,2.37,2.05,2.72,2.63,2.49,3.09,2.25,2.31,2.89,1.97,1.01]

def australium():
    global australiumCount
    global moneyEarned
    alreadyDropped = False
    up = 0
    while up != 19:
        if random.uniform(0,10000) <= chance[up]:
            alreadyDropped = True
            moneyEarned+=values[up]
            australiumCount+=1
            australiumsFound.append("Australium " + weapons[up])
        up+=1



print("v1.5 - Made by Lexzach")
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
print("Include other Australiums to profit (slows down performance)? (y/n)")
answer=input()
if answer == "y":
    includeOthers = True
else:
    includeOthers = False
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
    australiumsFound = []
    australiumCount = 0
    panDropped = 0
    alreadyDropped = False
    moneyEarned = 0
    while panDropped != 1:
        tourNumber+=1
        totalSpent+=float(price)*float(ticketsPerTour)
        timePlayed+=randint(mvmMinTime, mvmMaxTime)
        if randint(0,10000) == 10000:
            panDropped = 1
        if panDropped != 1:
            if includeOthers == True:
                australium()
    simCost = round(float(tourNumber*(price*int(ticketsPerTour))),2)
    if totalSpent < moneyEarned+currentPanPrice:
        print("\nSimulation #"+str(simsRan)+"\nTour that pan was dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(simCost)+"\nTotal estimated time spent playing MVM: "+str(round(timePlayed/60))+" hours")
        if australiumCount > 0:
            print("Number of Australiums found: " + str(australiumCount))
            print("Total value of Australiums: $"+str(round(moneyEarned)))
            
        profit+=1
        print("TOTAL MONEY EARNED: $"+str(round(totalSpent - (moneyEarned+currentPanPrice),2)*-1))
    else:
        print("\nSimulation #"+str(simsRan)+"\nTour that pan was dropped: "+str(tourNumber)+"\nMoney spent on " + str(tourNumber) + " tours: $"+str(simCost)+"\nTotal estimated time spent playing MVM: "+str(round(timePlayed/60))+" hours")
        if australiumCount > 0:
            print("Number of Australiums found: " + str(australiumCount))
            print("Total value of Australiums: $"+str(round(moneyEarned)))
            
        loss+=1
        print("TOTAL MONEY SPENT: $"+str(round(totalSpent - (moneyEarned+currentPanPrice),2)))
    if displayExtra == True:
        if tourNumber <= displayUnder:
            underUserNumber+=1
    if tourNumber < lowestTour:
        lowestSim = simsRan
        lowestTour=tourNumber
        lowestTourTime=timePlayed
        lowestAustralium=australiumCount
        lowestAustraliumValue=round(moneyEarned,2)
        totalSpentLowest = round(totalSpent - (moneyEarned+currentPanPrice),2)
    if round(totalSpent - (moneyEarned+currentPanPrice),2)*-1 > mostProfit:
        mostProfit = round(totalSpent - (moneyEarned+currentPanPrice),2)*-1
        mostSim = simsRan
        mostTour=tourNumber
        mostTourTime=timePlayed
        mostAustralium=australiumCount
        mostAustraliumName = australiumsFound
        mostAustraliumValue=round(moneyEarned,2)
        totalSpentMost = round(totalSpent - (moneyEarned+currentPanPrice),2)*-1
    simsRan+=1
    toursTotal = toursTotal + tourNumber

odds = numpy.random.binomial(lowestTour, 0.01, None)
cost = round(float(lowestTour*(price*4)))
bestTourPrice = str(round(float(lowestTour*(price*int(ticketsPerTour)))))
try:
    mostProfitPrice = str(round(float(mostTour*(price*int(ticketsPerTour)))))
except:
    print("")


if totalSpentLowest < lowestAustraliumValue+currentPanPrice:
    print("\n\n\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you made $" + str(totalSpentLowest*-1) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))
    if displayExtra == True:
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
else:
    print("\n\n\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you lost $" + str(totalSpentLowest) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))
    if displayExtra == True:
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
#try:
print("\nMost profitable (Simulation #" + str(mostSim) +"):")
print("Tour that pan dropped on: "+str(mostTour)+"\nMoney spent: $"+str(mostProfitPrice)+"\nTotal estimated time playing MVM: "+str(mostTourTime)+" hours\nAustralium Drops: "+str(mostAustralium)+"\nAustralium value: $"+str(mostAustraliumValue)+"\nTOTAL EARNED: "+str(totalSpentMost))
#except:
#    print("")
a=input()