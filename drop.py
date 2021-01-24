import random
import tkinter as tk
from random import randint, randrange
import numpy
from tkinter import *
import webbrowser
import BackpackTF
from BackpackTF import *
import os
import time 


submit=False
start = False
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
data = ""
mostProfit = 0
mvmMinTime=25
mvmMaxTime=75 
timePlayed=0
configRaw=[]
weapons = ["Ambassador", "Axtinguisher", "Black Box", "Blutsauger", "Flame Thrower", "Force-A-Nature", "Frontier Justice", "Grenade Launcher", "Knife", "Medi Gun", "Minigun", "Rocket Launcher", "Scattergun", "SMG", "Sniper Rifle", "Stickybomb Launcher", "Tomislav", "Wrench", "Eyelander"]
values = [15.92, 10.25, 19.26, 9.27, 32.62, 20.5, 21.74, 27.96, 30.44, 97.07, 33.55, 67.56, 57.46, 11.8, 46.13, 31.92, 32.3, 68.34, 76.1]
chance = [2.51,2.66,3.12,2.75,2.51,2.89,2.69,2.08,2.37,2.05,2.72,2.63,2.49,3.09,2.25,2.31,2.89,1.97,1.01]

def openConfig(lineNumber):
    global data
    global config
    global configRaw
    configRaw = open("settings.txt", "r+")
    config = configRaw.readlines()
    for x in config:
        config[config.index(x)] = x.replace("\n","")
    try:
        data = config[lineNumber]
    except:
        pass




try:
    openConfig(1)
except:
    error = tk.Tk()
    var = tk.IntVar()
    error.title("Error!")
    errorMessage = tk.Frame(master=error)
    temp = tk.Label(master=errorMessage, text="Error! settings.txt file not found in the\nsame directory as the program!\n\nThe program has been haulted and cannot continue until settings.txt\nhas been replaced.")
    temp.config(bg='red')
    temp.grid(row=1, column=0, sticky="w")
    errorMessage.grid(row=0, column=0, sticky="w")
    temp.wait_variable(var)



if data == "usr_api=":
    setup = tk.Tk()
    var = tk.IntVar()
    setup.title("First-time setup")
    setupMaster = tk.Frame(master=setup)
    button = tk.Frame(master=setup)
    api = tk.Frame(master=setup)
    title = tk.Label(master=setupMaster, text="Hello!\nIt seems it is your first time using this program.\nPlease follow the instructions below to get started!", fg="green")
    apiTitle = tk.Label(master=setupMaster,text="Please enter your Backpack.tf API key:")
    apiInput = tk.Entry(master=api, width=25)
    apiButton = tk.Button(master=button, text="- Submit -",command=lambda: var.set(1))
    apiTitle2 = tk.Label(master=setupMaster,text="You can get that from https://backpack.tf/developer/apikey/view")
    
    title.grid(row=0, sticky="n")
    apiTitle.grid(row=5, column=0, sticky="n")
    apiButton.grid(row=0, column=0,sticky="n")
    apiInput.grid(row=0, column=1, sticky="n")
    apiTitle2.grid(row=10,sticky="n")
    

    setupMaster.grid(row=0, column=0, sticky="n")
    api.grid(row=10, column=0, sticky="n")
    button.grid(row=20, column=0, sticky="n")
    button.wait_variable(var)
    api = apiInput.get()
    setup.destroy()
    configRaw = open("settings.txt", "w")
    config[1] = "\nusr_api="+str(api) + "\n"
    configRaw.writelines(config)
    configRaw.close()
    api = ""
openConfig(1)
api = Currency(apikey=str(data).replace("usr_api=", ""))



# if openConfig(2) != "":
#     values=[]
#     count = 2
#     while count != 21:
#         openConfig(count)
#         values.append(float(data))
#         count+=1

def calcValue(x, y, z):
    global itemValue
    try:
        itemValue = api.item_price(item=str(x), quality=str(y), craftable=z, tradable=1, priceindex=0)
        itemValue = itemValue["value"]
    except:
        print("Error while checking the price of "+x)

calcValue("Mann Co. Supply Crate Key", "Unique","1")
keyValue = itemValue

values = []
for x in weapons:
    calcValue("Australium " + x, "Strange", "1")
    temp = itemValue
    temp = round((temp * keyValue) / 100 * 3,2)
    values.append(temp)
    print("Priced item [" + str(weapons.index(x)) + "/20]")

calcValue("Tour of Duty Ticket", "Unique", "0")
temp = itemValue
temp = round((temp) / 100 * 3,2)
ticketValue = temp
print("Priced item [19/20]")

calcValue("Golden Frying Pan", "Strange", "1")
temp = itemValue
temp = round((temp * keyValue) / 100 * 3,2)
panValue = temp
print("Priced item [20/20]")

prices = tk.Tk()
prices.title("bp.tf Import")
pricesMenu = tk.Frame(master=prices)
buttonSave = tk.IntVar()
count = 0
for x in weapons:
    temp = tk.Label(master=pricesMenu, text="Australium " + x + " (USD)")
    temp.grid(row=count, column=0, sticky="w")
    count+=1

Ambassador = tk.Entry(master=pricesMenu, width=10)
Ambassador.insert(0, values[0])
Ambassador.grid(row=0, column=5, sticky="e")

Axtinguisher = tk.Entry(master=pricesMenu, width=10)
Axtinguisher.insert(0, values[1])
Axtinguisher.grid(row=1, column=5, sticky="e")

BlackBox = tk.Entry(master=pricesMenu, width=10)
BlackBox.insert(0, values[2])
BlackBox.grid(row=2, column=5, sticky="e")

Blutsauger = tk.Entry(master=pricesMenu, width=10)
Blutsauger.insert(0, values[3])
Blutsauger.grid(row=3, column=5, sticky="e")

FlameThrower = tk.Entry(master=pricesMenu, width=10)
FlameThrower.insert(0, values[4])
FlameThrower.grid(row=4, column=5, sticky="e")

ForceANature = tk.Entry(master=pricesMenu, width=10)
ForceANature.insert(0, values[5])
ForceANature.grid(row=5, column=5, sticky="e")

FrontierJustice = tk.Entry(master=pricesMenu, width=10)
FrontierJustice.insert(0, values[6])
FrontierJustice.grid(row=6, column=5, sticky="e")

GrenadeLauncher = tk.Entry(master=pricesMenu, width=10)
GrenadeLauncher.insert(0, values[7])
GrenadeLauncher.grid(row=7, column=5, sticky="e")

Knife = tk.Entry(master=pricesMenu, width=10)
Knife.insert(0, values[8])
Knife.grid(row=8, column=5, sticky="e")

MediGun = tk.Entry(master=pricesMenu, width=10)
MediGun.insert(0, values[9])
MediGun.grid(row=9, column=5, sticky="e")

Minigun = tk.Entry(master=pricesMenu, width=10)
Minigun.insert(0, values[10])
Minigun.grid(row=10, column=5, sticky="e")

RocketLauncher = tk.Entry(master=pricesMenu, width=10)
RocketLauncher.insert(0, values[11])
RocketLauncher.grid(row=11, column=5, sticky="e")

Scattergun = tk.Entry(master=pricesMenu, width=10)
Scattergun.insert(0, values[12])
Scattergun.grid(row=12, column=5, sticky="e")

SMG = tk.Entry(master=pricesMenu, width=10)
SMG.insert(0, values[13])
SMG.grid(row=13, column=5, sticky="e")

SniperRifle = tk.Entry(master=pricesMenu, width=10)
SniperRifle.insert(0, values[14])
SniperRifle.grid(row=14, column=5, sticky="e")

Stickybomb = tk.Entry(master=pricesMenu, width=10)
Stickybomb.insert(0, values[15])
Stickybomb.grid(row=15, column=5, sticky="e")

Tomislav = tk.Entry(master=pricesMenu, width=10)
Tomislav.insert(0, values[16])
Tomislav.grid(row=16, column=5, sticky="e")

Wrench = tk.Entry(master=pricesMenu, width=10)
Wrench.insert(0, values[17])
Wrench.grid(row=17, column=5, sticky="e")

Eyelander = tk.Entry(master=pricesMenu, width=10)
Eyelander.insert(0, values[18])
Eyelander.grid(row=18, column=5, sticky="e")

buttonObject = tk.Button(prices,text="- Launch Program and Save to Config -",command=lambda: buttonSave.set(1))
buttonObject.grid(row=19, column=0, sticky="s")
pricesMenu.grid(row=0, column=0, sticky="w")

buttonObject.wait_variable(buttonSave)
values = []
values.append(Ambassador.get())
values.append(Axtinguisher.get())
values.append(BlackBox.get())
values.append(Blutsauger.get())
values.append(FlameThrower.get())
values.append(ForceANature.get())
values.append(FrontierJustice.get())
values.append(GrenadeLauncher.get())
values.append(Knife.get())
values.append(MediGun.get())
values.append(Minigun.get())
values.append(RocketLauncher.get())
values.append(Scattergun.get())
values.append(SMG.get())
values.append(SniperRifle.get())
values.append(Stickybomb.get())
values.append(Tomislav.get())
values.append(Wrench.get())
values.append(Eyelander.get())
for x in range(len(values)):
    values[x] = float(values[x])
prices.destroy()








def github():
    webbrowser.open('https://github.com/Lexzach/goldenpansimulator')
def pan():
    webbrowser.open('https://marketplace.tf/items/tf2/1071;11;kt-3')
def ticket():
    webbrowser.open('https://steamcommunity.com/market/listings/440/Tour%20of%20Duty%20Ticket')
    

window = tk.Tk()
menu = Menu(window)
window.config(menu=menu)
window.title("MvM Drop Simulator")
pan_entry = tk.Frame(master=window)
sim_entry = tk.Frame(master=window)
max_tours_entry = tk.Frame(master=window)
tickets_tour = tk.Frame(master=window)
include_aussie = tk.Frame(master=window)
aussieInclude = BooleanVar()
price_ticket = tk.Frame(master=window)
buttonClick = tk.IntVar()
helpmenu = Menu(menu)
prices = Menu(menu) 
settings = Menu(menu)
start_button = tk.Frame(master=window)

pan_label = tk.Label(master=pan_entry, text="Pan Value (USD):")
pan_input = tk.Entry(master=pan_entry, width=10)
sim_label = tk.Label(master=sim_entry, text="Simulations to run:")
sim_input = tk.Entry(master=sim_entry, width=10)
max_tours_label = tk.Label(master=max_tours_entry, text="Max tours per simulation (0 = disable):")
max_tours_input = tk.Entry(master=max_tours_entry, width=10)
tickets_tour_label = tk.Label(master=tickets_tour, text="Tickets per tour:")
tickets_tour_input = tk.Entry(master=tickets_tour, width=10)
include_aussie_button = tk.Checkbutton(include_aussie, text="Include other Australium drops when calculating profit (performance intensive)",variable=aussieInclude)
price_ticket_label = tk.Label(master=price_ticket, text="Ticket Price (USD):")
price_ticket_input = tk.Entry(master=price_ticket, width=10)
start_button_button = tk.Button(master=start_button, text="- Start Simulation -", command=lambda: buttonClick.set(1)) 

menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='GitHub page', command=github) 

price_ticket_input.insert(0, ticketValue)
pan_input.insert(0, panValue)
tickets_tour_input.insert(0, "3")
max_tours_input.insert(0,"0")


#autofill.pack()



pan_input.grid(row=1, column=5, sticky="e")
pan_label.grid(row=1, column=0, sticky="w")

sim_label.grid(row=2, column=0, sticky="w")
sim_input.grid(row=2, column=5, sticky="e")

max_tours_input.grid(row=3, column=5, sticky="e")
max_tours_label.grid(row=3, column=0, sticky="w")

tickets_tour_input.grid(row=4, column=5, sticky="e")
tickets_tour_label.grid(row=4, column=0, sticky="w")

price_ticket_input.grid(row=5, column=5, sticky="e")
price_ticket_label.grid(row=5, column=0, sticky="w")

include_aussie_button.grid(row=8, column=0, sticky="w")

start_button_button.grid(row=9, column=0, sticky="w")

sim_entry.grid(row=10, column=0, sticky="w")
pan_entry.grid(row=0, column=0, sticky="w")
max_tours_entry.grid(row=20, column=0, sticky="w")
tickets_tour.grid(row=30, column=0, sticky="w")
price_ticket.grid(row=40, column=0, sticky="w")
include_aussie.grid(row=50, column=0, sticky="w")
start_button.grid(row=60, column=0, sticky="n")

start_button_button.wait_variable(buttonClick)
displayUnder = max_tours_input.get()
toursToRun = sim_input.get()
ticketsPerTour = tickets_tour_input.get()
includeOthers = aussieInclude.get()
price = price_ticket_input.get()
currentPanPrice = pan_input.get()
window.destroy()

#window.mainloop()




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
if displayUnder == "0":
    displayExtra = False
else:
    displayExtra = True
price = price.replace("$", "")
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
        if tourNumber <= int(displayUnder):
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
menuIncludeOthers = ""
menuTextExtra = ""
if totalSpentLowest < lowestAustraliumValue+currentPanPrice:
    print("\n\n\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you made $" + str(totalSpentLowest*-1) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))
    menuText = ("Simulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you made $" + str(totalSpentLowest*-1) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))
    if displayExtra == True:
        menuTextExtra = ("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
else:
    print("\n\n\nSimulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you lost $" + str(totalSpentLowest) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))
    menuText = ("Simulations finished!\n\nTotal tours simulated: " +str(toursTotal)+"\nTotal pans dropped: "+str(simsRan)+"\nFrom this data, the pan drop rate was: "+str(round((simsRan/toursTotal)*100,8))+"%"+". The actual drop rate is 0.01%."+"\nSimulations that ended in profit: "+str(profit)+"\nSimulations that ended in loss: "+str(loss)+"\nThe chances of earning profit would be: "+str(round((profit/loss)*100,2))+"%\n\nQuickest pan drop (Simulation #" + str(lowestSim) + "):\nTour that pan dropped on: " + str(lowestTour)+"\nMoney spent on " + str(lowestTour) + " tours: $"+str(bestTourPrice)+", you lost $" + str(totalSpentLowest) + " in profit.\nOdds of getting a pan on your "+str(lowestTour)+" run: "+str(odds)+"%"+"\nTotal estimated time playing MVM: "+str(round(lowestTourTime/60))+" hours\nAustralium Drops: "+str(lowestAustralium)+"\nAustralium value: $"+str(lowestAustraliumValue))

    if displayExtra == True:
        print("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")
        menuTextExtra = ("\nTours where pan was aquired within " + str(displayUnder) + " or less tours: " + str(underUserNumber)+"/"+str(simsRan)+" ("+str((underUserNumber/simsRan)*100)+"%)")

#try:
if includeOthers == True and int(toursToRun) != 1 and int(toursToRun) != 0:
    print("\nMost profitable (Simulation #" + str(mostSim) +"):")
    print("Tour that pan dropped on: "+str(mostTour)+"\nMoney spent: $"+str(mostProfitPrice)+"\nTotal estimated time playing MVM: "+str(mostTourTime)+" hours\nAustralium Drops: "+str(mostAustralium)+"\nAustralium value: $"+str(mostAustraliumValue)+"\nTOTAL EARNED: $"+str(totalSpentMost))
    menuIncludeOthers = ("\nMost profitable (Simulation #" + str(mostSim) +"):\n Tour that pan dropped on: "+str(mostTour)+"\nMoney spent: $"+str(mostProfitPrice)+"\nTotal estimated time playing MVM: "+str(mostTourTime)+" hours\nAustralium Drops: "+str(mostAustralium)+"\nAustralium value: $"+str(mostAustraliumValue)+"\nTOTAL EARNED: $"+str(totalSpentMost/60))
#except:
#    print("")
window = tk.Tk()
window.config(menu=menu)
window.title("Results")
finished = tk.Frame(master=window)
temp = tk.Label(master=finished, text=menuText+menuTextExtra+"\n"+menuIncludeOthers)
temp.grid(row=1, column=0, sticky="w")
finished.grid(row=0, column=0, sticky="w")

a=input()