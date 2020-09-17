import csv

# Open Airports.txt and load into variable 'airports'
airportsCSV = open('Airports.txt', 'r')
csvreader = csv.reader(airportsCSV)
airports = []
for row in csvreader:
    airports.append(row)


# Create menu
def mainMenu():
    print("=========")
    print("Main Menu")
    print("=========")
    print("1. Enter airport details")
    print("2. Enter flight details")
    print("3. Enter price plan & calculate profit")
    print("4. Clear data")
    print("5. Quit")
    try:
        option = input("Please choose an option: [1-5] ")
        option = int(option[0])
        if option < 1 or option > 5:
            raise ValueError
    except SystemExit:
        print("Goodbye :)")
    except:
        print("Input was invalid.")
        mainMenu()

    if option == 5:
        # exit gracefully
        try:
            quit()
        except SystemExit:
            print("Goodbye :)")


mainMenu()