#lists
carCompanies=["ford", "porsche", "bmw", "subaru"]
lineup=[]
fordCars=["darkhorse", "gtd", "shelby", "gt"]
porscheCars=["911", "boxster", "cayman", "spyder"]
bmwCars=["m4", "m8", "m3","z4"]
subaruSports=["brz", "wrx", "impreza","legacy"]
#functions
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
        lineup. append(selection1)
        if selection1==fordCars[0]:
            return "darkhorse"
        if selection1==fordCars[1]:
            return "gtd"
        if selection1==fordCars[2]:
            return "shelby"
        if selection1==fordCars[3]:
            return "gt"
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

if carCompanySelection:
        fordmodelSelection=checkFordOptions(input("What car model would you like, only cars from this lineup are allowed: GTD, Darkhorse, GT, and Shelby\n "))
print(fordmodelSelection)
while carCompanySelection in "ford": 
    fordmodelSelection=checkFordOptions(input("What car model would you like, only cars from this lineup are allowed: GTD, Darkhorse, GT, and Shelby\n "))
    while fordmodelSelection==None: 
        fordmodelSelection=checkCarCompanyOption(input("Please use a given model"))