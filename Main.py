"""Code by William Stoneham 2020"""
"""Code for 2021 GCSE programming project"""
ver = 1.0
import os
import csv

print("Welcome to the 2021 GCSE programming project by William Stoneham")
print("This program is designed to work out the profitability of a certain air route between a uk base and overseas "
      "airports.")

"""Creates a class which all users options can be stored into"""
class user:
    pass

"""Defines an airport class then imports the airports from Airports.txt and makes multiple instances of the class. Protected by a try except statement"""


class Airport:
    def __init__(self, code, name, distance_lennon, distance_bournemouth):
        """John lennon then Bournemouth International"""
        self.code = code
        self.name = name
        self.distance_lennon = distance_lennon
        self.distance_bournemouth = distance_bournemouth


"""Reads the textfile and every airport is given a instance of the airport class"""
fileobject = open("Airports.txt", "r") ##opens the airport.txt file
file = csv.reader(fileobject, delimiter=",") ##split up every value using csv reader
airports = []##create a list to put airport class instances in
for line in file: ##i now look through every line and create an instance of the airport class using this data
    try:
        airport = Airport(line[0], line[1], line[2], line[3])
        airports.append(airport) ##i then append this to the airports list
    except:
        pass

fileobject.close()

"""Creates a plane class template. Which I can then use to create instances for every plane type."""
class planes:
    def __init__(self, name, RunningCost, MAXRange, EconomyMAX, MINFirst):
        self.name = name
        self.runningcost = int(RunningCost)
        self.maxrange = int(MAXRange)
        self.economymax = int(EconomyMAX)
        self.minfirst = int(MINFirst)


"""Creates instances of the classes for each plane type"""
mediumnarrow = planes("Medium narrow body", 8, 2650, 180, 8)

largenarrow = planes("Large narrow body", 7, 5600, 220, 10)

mediumwide = planes("Medium wide body", 5, 4050, 406, 14)

Aircraft = [mediumnarrow, largenarrow, mediumwide]

"""Defines the airport Select function"""


def Airport_Select(user, Airport):
    user.UKCODE = input("Enter the UK Base Code. BOH or LPL: ").upper()
    user.OSCODE = input("Enter the overseas Base Code: ").upper()
    OSVALID = False
    if user.UKCODE != "BOH":  ##Bournemouth or liverpool
        if user.UKCODE != "LPL":
            print("UK Code is not Valid")
            user.UKCODE = False
            return
    for airport in airports:  ##Looks through every airport in the airport class if the users input is not understood it will exit.
        if airport.code == user.OSCODE:
            OSVALID = True  ##Sets the bool value to True when you found an airport
            user.airport = airport ##pulls through the current airports class and places it inside of the user class.
    if not OSVALID:
        print("The overseas code is unrecognised")
        user.OSCODE = False ## sets the oscode value to false so if the user tries to start the third function it will pull up an error.
        return ##returns user to main menu
    if user.UKCODE == "BOH": ## uses the airport choices to calculate the distance and sets the value into the user class
        user.distance = user.airport.distance_bournemouth
    else:
        user.distance = user.airport.distance_lennon
    print("Success: Airports Selected")
    """End of subroutine"""

"""Defines the flight details function"""

def Flight_Details(user, Aircraft): 
    print("")
    print("What type of aircraft will you use?")
    print("1: Medium Narrow")
    print("2: Large Narrow")
    print("3: Medium Wide")
    planeinput = input()##user chooses plane
    try:    ##use a try catch just incase the user inputs a invalid input
        planeinput = int(planeinput)##As all the aircraft classes are in a list I can just search it using the users input -1.
        user.plane = Aircraft[planeinput - 1]
    except:
        print("You have inputed an incorect choice")
        user.plane = False ## third function will error if the user tries to run it
        return## to main menu
    try:    ##yet again another try catch function just incase the user has not inputed a route between the two airports.
        user.distance ##Checks if the user has inputed the two airports thus giving me a distance between the two airports
    except:
        print("You haven't entered in the route yet")
        user.plane = False ##sets user.plane to false thus stopping the third function  
        return

    if int(user.plane.maxrange) < int(user.distance): ##checks if the planes max range is smaller then the distance we then know the plane can not serve the route this error is flagged to the user
        print("Plane you have chosen is too small for route")
        user.plane = False
        return
    print("Plane is chosen and suitible")
    print("How many first Class seats are there. Can't be more then " + str(int(user.plane.economymax / 2)) + " seats") ##tells the user how many first class seats they can have

    try:##try catch loop to make sure the user is inputing a valid input.
        user.firstseats = int(input())
    except:
        print("Value not accepted")
        user.firstseats = False ##set to false so if the user started the price proift function early it would fail. because the data entered is incorrect.
        return

    if user.firstseats * 2 > user.plane.economymax: ##A first class seat takes up the space of 2 economy seats so if the user inputs a firstclass seat which is more then half the economymax of the aircraft the program should give a suitible error to the user.
        print("Too many first class seats")
        user.firstseats = False
        return
    elif user.firstseats * 2 < user.plane.economymax:##checks if the user has inputed enough first class seats.
        if user.firstseats >= user.plane.minfirst:##checks if the user has inputed more then the minimum ammount of first class seats for the aircraft.
            user.economy = user.plane.economymax - user.firstseats * 2 ##works out how many economy seats by subtracting the max ammount of economy seats from double the first class seats.
        else:
            print("Not enough first class seats")
            user.firstseats = False ##sets the firstclass seats to false so if the user runs the price profit functioon early it would fail. because the data entered is incorrect
            return
    user.seats = user.economy + user.firstseats ##works out the ammount of seats on the currently configured aircraft.
    print("Plane selected")
    """End of subroutine"""


def price_profit(user):
    """First of all check if the user has completed the previous subroutines"""
    try: ##These try and except functions check that the variable has been created.
        user.plane
    except:
        print("You haven't run the choose airport function")
        return
    try:
        user.firstseats
    except:
        print("You haven't inputed an ammount of first class seats")
        return
    try:
        user.UKCODE
        user.OSCODE
    except:
        print("You haven't selected a route")
        
    if not user.plane: ##These if statements check that there is data inside of these variables
        print("You haven't selected a plane")
        return
    if not user.firstseats:
        print("You haven't inputed the ammount of first class seats")
        return
    if not user.UKCODE:
        if not user.OSCODE:
            print("You haven't selected a route")
            return
    
    """Now getting the user to input the price for the seats"""
    try: ##inside a try except function just incase the user enters an incorrect value
        print("How much is a economy class seat?: ")
        economyprice = float(input())
        print("How much is a first class seat?: ")
        firstprice = float(input())
    except:
        print("One of the values is not an excepted value")
        return

    """now time for lots of formulas to work out the data"""

    user.distance = int(user.distance) ##makes sure the user.distance variable is an interger.
    
    runningcost = (float(user.plane.runningcost) * (user.distance / 100)) * float(user.seats) ##works out the running cost by taking the planes running cost times the distance /100. We then times this by the number of seats

    income = (user.firstseats * firstprice) + (user.economy * economyprice)## we now work out the cost by timesing the ammount of seats by their respective price. and then adds the totals together

    flight_profit = income - runningcost ##works out the profit by subtracting the income from the running cost

    ##now prints the results of the program to the user
    print("--------------------------------------------------------------------------")
    print("Route " + user.UKCODE + " to " + user.OSCODE)
    print("The route has a distance of: " + str(user.distance))
    print("A Economy class ticket costs: " + str(economyprice))
    print("A First Class ticket costs: " + str(firstprice))
    print("The aircraft chosen is a : " + user.plane.name)
    print("There are " + str(user.economy) + " economy seats and " + str(user.firstseats) + " first class seats to create a total of " + str(user.seats) + " seats")
    print("The running cost for the flight is: " + str(runningcost))
    print("The income for the flight is: " + str(income))
    print("The profitability for the flight is: " + str(flight_profit))
    print("--------------------------------------------------------------------------")
    print("")
    userwantstxtfile = input("Would you like to export this as a text file. y or n: ")##asks the user if they want to print the results to a text file
    if userwantstxtfile != "y":
        return
    try:
        file = open("Route" + str(user.UKCODE) + "to" + str(user.OSCODE) + ".txt", "w")
        file.write("Route " + user.UKCODE + " to " + user.OSCODE + "\n")
        file.write("The route has a distance of: " + str(user.distance) + "\n")
        file.write("A Economy class ticket costs: " + str(economyprice) + "\n")
        file.write("A First Class ticket costs: " + str(firstprice) + "\n")
        file.write("The aircraft chosen is a : " + user.plane.name + "\n")
        file.write("There are " + str(user.economy) + " economy seats and " + str(user.firstseats) + " first class seats to create a total of " + str(user.seats) + " seats" + "\n")
        file.write("The running cost for the flight is: " + str(runningcost) + "\n")
        file.write("The income for the flight is: " + str(income) + "\n")
        file.write("The profitability for the flight is: " + str(flight_profit) + "\n")
        file.write("Program by William Stoneham" + "\n")
        file.close()
        print("File created")
    except:
        print("File could not be created") ##returns a message if there was an error creating the file

"""Main Menu Stuff option list"""
options = [[1, "Enter Airport Details"], [2, "Enter Flight Details"], [3, "Enter Price Plan And Calculate Profits"],
           [4, "Clear Inputted Data"], [5, "Quit"],["ver"]] ##creates list for all the main menu options. I just like the way it formats the text.

"""Main Menu Forever Loop"""
while True:
    print("")
    print("Main Menu")
    print("Your options are: ")
    print(str(options))
    option = input("<:> ") ##User input's option
    if option == "1":   ##options are selected and the appropriate subroutine is run.
        Airport_Select(user, Airport)
    elif option == "2":
        Flight_Details(user, Aircraft)
    elif option == "3":
        price_profit(user)
    elif option == "4":
        class user: ## recreates the user class thus wiping all the users data.
            pass
        print("Data Cleared")
    elif option == "5":
        print("Program Killed")
        quit() ##umm does what it says, quits the program.
    elif option == "ver":
        print(str(ver) + " Airport Profitability Calculator William Stoneham 2020")## prints the version of this program and my beautiful name
    else:
        print("unknown input")## prints a suitble error message if what the user entered is not recognised.
