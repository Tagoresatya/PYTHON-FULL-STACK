'''
file = open('sample.txt','r')

content1 = file.read()
file.seek(0)
content2 = file.readline()
file.seek(0)
content3 = file.readlines()

print(content1,content2,content3,sep='\n\n')

file.close()

'''

'''
file = open('sample.txt','w')

file.write("Hello Everyone")

file.close()

'''


'''
file = open('sample.txt','a')

file.write("\nWelcome to the python class !!")

file.close()
'''


'''
file = open('sample.txt','r+')

file.write("\nFile operations")
file.seek(0)
print(file.read)

file.close()
    '''


'''
with open('sample.txt''r+')as file:
    file.write("\nFile operations")
file.seek(0)
print(file.read)

'''
    
