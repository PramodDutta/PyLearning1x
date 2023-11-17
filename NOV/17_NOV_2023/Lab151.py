import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('mydata.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)


# API Automation in Selenium - 90% Read the file
# 10% update the file