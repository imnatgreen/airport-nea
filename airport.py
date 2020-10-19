#####################################
##                                 ##
##   Airport NEA by Nathan Green   ##
##                                 ##
#####################################

import csv
from time import sleep

# Open Airports.txt and load into variable 'airports'
airportsCSV = open('Airports.txt', 'r')  # Open file
csvreader = csv.reader(airportsCSV)  # Load file into CSV module
airports = []  # Prepare empty array
for row in csvreader:  # Loop over rows
    airports.append(row)  # Add rows to array

aircrafts = [['Medium narrow body', 8, 2650, 180, 8],
             ['Large narrow body', 7, 5600, 220, 10],
             ['Medium wide body', 5, 4050, 406, 14]]

airportDetails = None
flightDetails = None


# Create menu
def mainMenu():
    global airportDetails  # Open as global for persistance
    global flightDetails  #  once menu is finished
    print("\n=========")
    print("Main Menu")
    print("=========")
    print("1. Enter airport details")
    print("2. Enter flight details")
    print("3. Enter price plan & calculate profit")
    print("4. Clear data")
    print("5. Quit")
    try:
        option = input("Please choose an option: [1-5] ")
        option = int(option[0])  # Check that input was an integer
        if option < 1 or option > 5:  # Check that integer is valid
            raise ValueError
    except SystemExit:  # Handle Ctrl+C and similar.
        return "quit"
    except:  # Handle an invalid input (ValueError etc.)
        print("Input was invalid. Returning to menu.")

    if option == 1:
        airportDetails = getAirportDetails(airports)
    elif option == 2:
        flightDetails = getFlightDetails(aircrafts)
    elif option == 3:
        getPricePlan(airportDetails, flightDetails)
    elif option == 4:
        print("Clearing data...")
        airportDetails = None
        flightDetails = None
    elif option == 5:
        return "quit"


def getAirportDetails(airportData):
    try:  # Get first 3 letters of input and make uppercase.
        ukAirport = input("Enter a UK airport code [LPL/BOH]>> ")[0:3].upper()
        if ukAirport != "LPL" and ukAirport != "BOH":
            raise ValueError
        overseasAirport = input(
            "Enter an overseas airport code >> ")[0:3].upper()
        isValid = False
        for airport in airportData:  # Search airportData for code
            if overseasAirport == airport[0]:
                isValid = True
                print(airport[1] + " has been selected.")
                return [ukAirport, airport]  # Return for use later
        if isValid == False:  # Code wasn't found in airportData
            print("No valid airport was entered. Returning to menu.")
    except:  # Handle errors from invalid input
        print("Input was invalid. Returning to menu.")


def getFlightDetails(aircraftData):
    print("Available aircraft types:")
    for count, aircraft in enumerate(aircraftData):  # Loop over aircraft
        print(str(count + 1) + ". " +
              aircraft[0])  # Print numbered list of aircraft
    try:  # Handle inputs as in mainMenu
        option = input("Please choose an option: [1-" +
                       str(len(aircraftData)) +
                       "] ")  # Dynamically change max input
        option = int(option[0])
        if option < 1 or option > len(aircraftData):
            raise ValueError
    except:
        print("Input was invalid. Returning to menu.")
        return None

    labels = [
        "Type", "Running cost/seat/100km", "Max flight range (km)",
        "Capacity (all standard seats)", "Min 1st class seats"
    ]
    aircraft = aircraftData[option - 1]  # Store selected aircraft
    print("\nAircraft selected:")
    for count, detail in enumerate(aircraft):  # Loop over selected aircraft
        print(labels[count] + ": " + str(detail))  # Print details of aircraft

    lowHigh = ''
    try:
        option = input("\nEnter number of 1st class seats: (" +
                       str(aircraft[4]) + " - " + str(int(aircraft[3] / 2)) +
                       ") ")  # Calculate seat ranges
        option = int(option)
        if option < aircraft[4]:  # Raise error if too low
            lowHigh = "low"
            raise ValueError
        elif option > aircraft[3] / 2:  # Raise error if too high
            lowHigh = "high"
            raise ValueError
        firstSeats = option
        standardSeats = aircraft[3] - firstSeats * 2
        print("No. of 1st class seats: " + str(firstSeats))
        print("No. of standard seats: " + str(standardSeats))
        return [aircraft, firstSeats, standardSeats]  # Return for use later
    except:  # Handle exceptions
        if lowHigh == '':
            print("Input was invalid. Returning to menu.")
        else:
            print("Value entered was too " + lowHigh + ". Returning to menu.")


def getPricePlan(airportDetails, flightDetails):
    try:  # Check data is ready for this stage
        if airportDetails == None:
            print("Airport details weren't entered.")
            raise ValueError
        if flightDetails == None:
            print("Flight details weren't entered.")
            raise ValueError
        ukAirportCheck = 2 if airportDetails[0] == 'LPL' else 3
        flightDistance = int(airportDetails[1][ukAirportCheck])
        if flightDetails[0][2] < flightDistance:
            print("Selected plane's range is too short.")
            raise ValueError
    except ValueError:
        print("Returning to main menu")
        return None  # Leave the function
    try:
        stdSeatPrice = float(
            input("Enter the price of a standard-class seat: £"))
        firstSeatPrice = float(
            input("Enter the price of a first-class seat: £"))
        costPerSeat = flightDetails[0][1] * flightDistance / 100
        flightCost = costPerSeat * (flightDetails[1] + flightDetails[2])
        flightIncome = (flightDetails[1] *
                        firstSeatPrice) + (flightDetails[2] * stdSeatPrice)
        flightProfit = flightIncome - flightCost
        # Print the calculated values formated to 2dp.
        print("Flight cost/seat: £{:.2f}".format(costPerSeat))
        print("Flight cost:      £{:.2f}".format(flightCost))
        print("Flight income:    £{:.2f}".format(flightIncome))
        print("Flight profit:    £{:.2f}".format(flightProfit))
    except:
        print("Input was invalid, returning to menu.")


while True:
    loopState = mainMenu()  # Run the menu (which runs the other options)
    if loopState == "quit":
        break  # Break out of the loop (to quit, see below)
    sleep(1.5)  # Add pause so text can be read more easily

try:
    quit()  # Quit by raising SystemExit
except SystemExit:  # Handle SystemExit gracefully
    print("Goodbye :)")