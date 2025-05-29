#lists
carCompanies=["ford", "porsche", "bmw", "subaru"]
lineup=[]
fordCars=["darkhorse", "gtd", "shelby", "gt", "none"]
porscheCars=["911", "boxster", "cayman", "spyder", "none"]
bmwCars=["m4", "m8", "m3","z4", "none"]
subaruSports=["brz", "wrx", "impreza","legacy", "none"]

def checkCarCompanyOption (selection):
    selection= selection.lower()
    if selection in carCompanies: 
        lineup.append(selection)
        if selection==carCompanies[0]:
            return "ford "
        elif selection==carCompanies[1]:
            return "porsche "
        elif selection==carCompanies[2]:
            return "bmw "
        elif selection==carCompanies[3]:
            return "subaru "
        else: 
            return 0 

def checkFordOptions(selection1): 
    selection1= selection1.lower()
    if selection1 in fordCars: 
        if selection1==fordCars[0]:
            lineup.append("Dark Horse")
            return "darkhorse"
        if selection1==fordCars[1]:
            lineup.append("GTD")
            return "gtd"
        if selection1==fordCars[2]:
            lineup.append("Shelby")
            return "shelby"
        if selection1==fordCars[3]:
            lineup.append("GT")
            return "gt"
        if selection1==fordCars[4]:
            lineup.append("No Ford")
            return "no ford"
        else: 
            return 0 

def checkPorscheOptions(selection1): 
    selection1= selection1.lower()
    if selection1 in porscheCars: 
        lineup. append(selection1)
        if selection1==porscheCars[0]:
            return "911"
        if selection1==porscheCars[1]:
            return "boxter"
        if selection1==porscheCars[2]:
            return "cayman"
        if selection1==porscheCars[3]:
            return "sypder"
        if selection1==porscheCars[4]:
            return "no porsche"
        else: 
            return 0 

def checkbmwOptions(selection1): 
    selection1= selection1.lower()
    if selection1 in bmwCars: 
        lineup. append(selection1)
        if selection1==bmwCars[0]:
            return "m4"
        if selection1==bmwCars[1]:
            return "m8"
        if selection1==bmwCars[2]:
            return "m3"
        if selection1==bmwCars[3]:
            return "z4"
        if selection1==bmwCars[4]:
            return "no bmw"
        else: 
            return 0 

def checksubaruOptions(selection1): 
    selection1= selection1.lower()
    if selection1 in subaruSports: 
        lineup. append(selection1)
        if selection1==subaruSports[0]:
            return "brz"
        if selection1==subaruSports[1]:
            return "wrx"
        if selection1==subaruSports[2]:
            return "impreza"
        if selection1==subaruSports[3]:
            return "legacy"
        if selection1==subaruSports[4]:
            return "no subbie"
        else: 
            return 0 

#introduction      
print("Welcome to the annual summer car show; here you will select the line up of your cars and what specs you want\n")

#car company selection 
carCompanySelection=0
carCompanySelection=checkCarCompanyOption(input("From what major company, must be from this line up, is your car from? Ford, Porsche, BMW, Subaru\n"))
while carCompanySelection==None: 
    carCompanySelection=checkCarCompanyOption(input("please choose an item from the given list\n"))

print(lineup)
print(carCompanySelection)

fordSelection=0 
fordSelection= checkFordOptions(input("What car from the ford line up do you have?(darkhorse, gtd, shelby, gt, none)\n"))
while fordSelection==None: 
    fordSelection=checkFordOptions(input("Please use something in the given options!\n"))
print(lineup)

porscheSelection=0
porscheSelection= checkPorscheOptions(input("What car do you have from the line up? (911, boxter, cayman, sypder, none)\n"))
while porscheSelection==None: 
    porscheSelection=checkPorscheOptions(input("Please use an actual thing from the list\n"))

print(lineup)

bmwSelection=0 
bmwSelection=checkbmwOptions(input("What car from the BMW Line do you have? m4, m8, m3, z4, none\n"))
while bmwSelection==None: 
    bmwSelection= checkbmwOptions(input("please use an option from the lineup cuh\n"))
print(lineup)

subaruSelection=0 
subaruSelection= checksubaruOptions(input("What car from the line up do you have? (brz, wrx, impreza, legacy, none)"))
while subaruSelection==None: 
    subaruSelection= checksubaruOptions(input("Use something from the given lineup bruh"))
print (lineup)

print("Thank you!!!!!")