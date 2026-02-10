'''
names['satya','pavan','divi','vinay']
cgpa=[]
'''

n=int(input("Enter the number of students: "))

names,gpas = [],[]

for i in range(n):
    name = input("Emter the name: ")
    gpa = float(input("Enter the gpa: "))
    names.append(name)
    gpas.append(gpa)

print(f'{"Names".ljust(9)} {"GPA".ljust(5)}')
    for i in range(len(names)):
        
