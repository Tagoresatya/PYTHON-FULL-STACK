score = 0

print("Python Quiz\n")

#question 1
print("1.What is python?")
print("a)A snake")
print("b)A programming language")
print("3)A game")
print("4)An OS")
ans = input("Your answer: ")
if ans == "b":
    score += 1

#question 2
print("\n2.Which symbol is used to write comments in python?")
print("a) //")
print("b) #")
print("c) /**/")
print("d)<!-------!>")
ans = input("Your answer: ")
if ans == "b":
    score += 1

#question 3

print("\n3.Which fuction is used to display output in python?")
print("a)Print()")
print("b)Show()")
print("c)Display()")
print("d)Output()")
ans = input ("Your answer: ")
if ans == "a":
    score += 1

#question4

print("\n4.Which data type is used to store whole numbers?")
print("a)FLoat")
print("b)String")
print("c)INT")
print("d)BOOL")
ans = input ("Your answer: ")
if ans == "c":
    score +=1


print("\n Quiz completed !!")
print("Your final score is",score,"/4")

if score == 4:
    print("Excellent !!")
elif score>=2:
    print("Good !")
else:
    print("Practice more.")     
    
      
