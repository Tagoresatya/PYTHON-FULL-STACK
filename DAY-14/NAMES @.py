file = open('names.txt','r')

content1 = file.read()
file.seek(0)
content2 = file,read()
file.seek(0)
content3 = file.read()

print(content1,content2,content3,sep='\n\n')

file.close()
