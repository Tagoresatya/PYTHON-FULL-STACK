
'''
def student_data(info):
    print(f'Name: {info[0]}')
    print(f'Course:{info[1]}')
    print(f'G-Year:{info[2]}')
    print('--------END------------')

data= [['satya','PFS',2026],
       ['sai','DAA',2025],
       ['tagore','JS',2024]]
for i in data:
    student_data(i)
    '''
'''
def display(uname,email,password):
    print(f'Username:{uname}')
    print(f'Email:{email}')
    print(f'password:{password}')
    print('\n\n')
    
display('Satya','Satya@2022@gmail.com',1014)
display('Singh','Paajii@131@gmail.com','Rukku@123')
'''

'''
def display(uname,email,password,status='present'):
    print(f'Username:{uname}')
    print(f'Email:{email}')
    print(f'password:{password}')
    print(f'Status:{status}')
    print('\n\n')
    
display(uname='Satya',email='Satya@2022@gmail.com',password='1014')
display(uname='Singh',email='Paajii@131@gmail.com',password='Rukku@123')
display(password='tag@$123',uname='tagore',email= 'tag2004@gmail.com')

'''

 
def display(*names):
    for i in names:
        print(i)
    else:
        print("_____End of the list_____")
display('varsha')
display('Satya','Tagore')
display('Sai','Akash','Ajith')


'''


def menu():
    print('1.check balance')
    print('2.Deposit')
    print('3.WIthdraw')
    print('4.Set pin')
    print('5.View transactions')
    print('6.Exit\n')
    
print("Welcome to the ATM")


'''






















 

            
    
