'''
import csv

with open('sample.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
'''

'''
import csv

with open('samples.csv','w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["4","DIVI","PFS"])

    '''

