 '''

with open('sample.txt','w') as file:
    file.write('Override')

with open('sample.txt','a') as file:
    file.write('Override')

with open('sample.txt','r') as file:
    content = file.read()
    print(content)

    '''

'''

import csv
with open('sample.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        print(row[1])

'''

'''
import csv
with open('sample.csv','a',newline='') as file:
    data = csv.writer(file)
    data.writerow(['4','Divi'])
    data.writerow(['5','Sharath'])

'''

'''
import csv
with open('products.csv','w',newline='') as file:
    data = csv.writer(file)
    data.writerow(['product_IDs','product','price'])
    data.writerow(['1','laptop','55000'])
    data.writerow(['2','Mouse','500'])
    data.writerow(['3','Speaker','5000'])
    data.writerow(['4','Keyboard','2000'])

    '''
"""

import csv
with open('products.csv','r') as file:
    data = csv.reader(file)
    for i in data:
        print(i)

"""

'''
import json

with open('sample.json','w') as file:
    data=[
        {"ID":"1","Name":"Satya"},
{"ID":"2","Name":"Shreya"},
{"ID":"3","Name":"Abhi"},
{"ID":"4","Name":"Ajith"},

]
    json.dump(data,file,indent=4)
    print("Data saved successfully !!!")
    
'''


import json
with open('sample.json','r') as file:
    data = json.load(file)
'''
    for i in data:
        print(i)   '''

data.append({'id':'5','name':'Yash'})

with open('sample.json',"w") as file:
    json.dump(data,file,indent=4)








    


