'''
pwd = input("Enter the pasword:  ")

if len (pwd)>=8:
   s = set()
   for i in pwd:
     if i.isupper():
         s.add("upper")
     elif i.islower():
         s.add("lower")
     elif i.isdigit():
         s.add("digit")
     else:
        s.add("splchar")
        
   if len(s) == 4:
        print("strong password")
   else:
        print ('password needs to be an uppercase,lowercase,digit,splchar')
                              

else:
    print("length needs to be >=8")





    
'''
'''

name=input("enter the name: ")
dob=input("Enter the dob{YYYY-MM-DD}: ")

username = name[:2]+name[-2:]+dob[-2:]+dob[2:4]

print(f"Hi {name} !\n Your username: {username}")


'''


data={
1:{'product':'Rice','price':60},
2:{'product':'Sugar','price':80},
3:{'product':'groundnuts','price':110},
4:{'product':'Ice cream','price':50},
5:{'product':'Salt','price':40},
6:{'product':'Brush','price':20},
7:{'product':'Chocolate','price':30},
8:{'product':'Chips','price':37},
9:{'product':'Bread','price':66},
10:{'product':'Milk','price':46},
}

print('Index'.ljust(7,' '),'product name'.ljust(7,' '),'price'.ljust(7,' '))

for i in data:
  print(
    str(i).ljust(7, ' '),
    data[i]['product'].ljust(7, ' '),
    str(data[i]['price']).ljust(7, ' ')
)



indexes = list(map(int,input("enter the indexes: ").split()))
print("Bill".center(30,'-'))
total_bill=0
for i in indexes:
   print(f'{data[i]["product"]} - ${data[i]["price"]}')
   total_bill+=data[i]["price"]

   print(f"your bill: {total_bill}")









