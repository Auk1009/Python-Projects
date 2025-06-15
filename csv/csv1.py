import csv
name = input('Enter name: ')
place = input('Enter place: ')

with open('test.csv' , 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name,place])

