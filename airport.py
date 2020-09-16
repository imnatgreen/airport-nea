import csv
airportsCSV = open('Airports.txt', 'r')
#with open('Airports.txt', 'r') as csvfile:
reader = csv.reader(airportsCSV)
airports = []
for row in reader:
    airports.append(row)

print(airports)