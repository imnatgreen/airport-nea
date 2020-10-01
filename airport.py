import csv
from time import sleep

# Open Airports.txt and load into variable 'airports'
airportsCSV = open('Airports.txt', 'r')
csvreader = csv.reader(airportsCSV)
airports = []
for row in csvreader:
    airports.append(row)


# Create menu
def mainMenu():
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
    if option == 5:
        return "quit"


def getAirportDetails(airportData):
    try:
        ukAirport = input("Enter a UK airport code [LPL/BOH]>> ")[0:3].upper()
        if ukAirport != "LPL" and ukAirport != "BOH":
            raise ValueError
        overseasAirport = input(
            "Enter an overseas airport code >> ")[0:3].upper()
        isValid = False
        for airport in airportData:
            if overseasAirport == airport[0]:
                isValid = True
                print(airport[1] + " has been selected.")
        if isValid == False:
            print("No valid airport was entered. Returning to menu.")
    except:
        print("Input was invalid. Returning to menu.")


while True:
    loopState = mainMenu()
    if loopState == "quit":
        break
    sleep(1.5)

try:
    quit()  # Quit by raising SystemExit
except SystemExit:  # Handle SystemExit gracefully
    print("Goodbye :)")