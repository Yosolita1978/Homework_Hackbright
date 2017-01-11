"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

#This if for store the information
salespeople = []
melons_sold = []

#this line open de file
f = open("sales-report.txt")
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

# In this momment you have the sales info separated in two variables
#The first if create the key, value con the info of each salesperson in the dictionary melons_sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons

#This is for the person already exits in the dictionary
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
