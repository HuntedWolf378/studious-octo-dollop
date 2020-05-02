#Dylan Wanser
#COP 1500 CRN 10417
#This program serves as the final version of my integration project
#It has been simplified into a demonstration of learned skills from this course
#W3Schools

#Intro and section one instructions
print("Hello World!")
print("I was created to demonstrate all the required skills.")
print("This first section will demonstrate basic arithmetic commands")
userName = input("Please input your name so I know who I am talking to! ")
print("Thank you for taking the time to view our program", userName + "!")
print("For this section please refrain from decimals or negatives")
print("This program was designed to be segmented and easy to reach from the")
print("starting point!")
addOne = int(input("Please input the first number you would like added: "))
addTwo = int(input("Please input the second number you would like added: "))
print(addOne + addTwo)
#Code for subtraction arithmetic
subOne = int(input("Input the first number you would like subtracted: "))
subTwo = int(input("Input the second number you would like subtracted: "))
print(subOne - subTwo)
#Code for division arithmetic
divOne = int(input("Input the first number to be divided: "))
print("Think of this number as the top of a fraction")
divTwo = int(input("Input the second number to be divided: "))
print("This will act as the bottom of a fraction")
print(divOne / divTwo)
#Code for multiplication arithmetic
multOne = int(input("Input the first number to be multiplied: "))
multTwo = int(input("Input the second number to be multiplied: "))
print(multOne * multTwo)
#Code for Floor Division
print("This section is floor division so it will round down the result")
flDivOne = int(input("Input the number to be divided: "))
flDivTwo = int(input("Input the number to be divided by: "))
print(flDivOne // flDivTwo)
#Code for Exponentiation
expOne = int(input("Input a number: "))
expTwo = int(input("Input a number to act as an exponent: "))
print("This section functions as 1st number to the power of the 2nd number")
print(expOne ** expTwo)
#Code for Modulus
print("For this section this operation will display the remainder of division")
modOne = int(input("Input a number to be divided: "))
modTwo = int(input("Input a number to be divided by: "))
print(modOne % modTwo)
#Assignment operator demonstration
print("For this section we will demonstrate assignment operations")
x = (input("Input a number to be assigned to a variable: "))
print("This was done multiple times during the last section but for this part")
print("It is just being made more visible to the user!")
print("x = " + x)
#This is a separation between basic conceptual knowledge to SPRINT 2 Content
print("")
print("This is where the program moves into the fun stuff,", userName + "!")
print("Unfortunately at this point it becomes more difficult to interface")
print("with a user. Fortunately there wil still be interaction but mostly the")
print("work will be hidden in the code and not visible on the user interface.")
print(" ")
#This is the first if statement example demostrating text
#The variables ifex 1 and 2 are shorthand designations for "if example"
#Variables designated with a 1 are for text based variables while those
#Designated with 2 are for variables that contain numbers
ifex1 = input("Please input the word 'bacon' ")
if(ifex1 == "bacon"):
    print("Thank you for following instructions!")
else:
    print("Not quite what I asked but it does demonstrate an else statement")
#This is another if statement example in which there are numbers
#This is a general true/false if/else statement
print("Now we do the same but with numbers!")
print("This number will serve as the variable in the function 0 < x < 5")
ifex2 = int(input("Please input any number of your choosing "))
if(ifex2 > 0 and ifex2 < 5):
    print("The statement is true")
else:
    print("Your value is outside of the desired perameters")
#This begins an if-elif statement example
#This is a conventional grading scale in which 100-90 is an A
#89-80 is a B, 79-70 is C, 69-60 is a D, and 59 or lower is an F
print("The easiest way to demonstrate our next topic, if-elif statements, is")
print("through a demonstration of a letter grading scale.")
elifEx2 = int(input("Please enter a number grade within 0 and 100 "))
if(elifEx2 > 100):
    print("User input is outside of expected perameters.")
elif(elifEx2 <= 100 and elifEx2 > 89):
    print("This is graded as an A")
elif(elifEx2 < 90 and elifEx2 > 79):
    print("This is graded as a B")
elif(elifEx2 < 80 and elifEx2 > 69):
    print("This is graded as a C")
elif(elifEx2 < 70 and elifEx2 > 59):
    print("This is graded as a D")
elif(elifEx2 < 60 and elifEx2 >= 0):
    print("This is graded as a F")
else:
    print("User input is outside of expected perameters.")
print("This next section demonstrates the remaining relational operators.")
#For this section it is all relational operators and the previos numbered
#variable system no longer applies. relOp is shorthand for relational operators
print("For this section if the number input does not equal what is reqested")
print("the program will print false.")
relOp1 = int(input("Please input a number equal to 2 "))
if(relOp1 == 2):
    print("True")
else:
    print("False")
relOp2 = int(input("Please input a number NOT equal to 2 "))
if(relOp2 != 2):
    print("True")
else:
    print("False")
relOp3 = int(input("Please input a number greater than 2 "))
if(relOp3 > 2):
    print("True")
else:
    print("False")
relOp4 = int(input("Please input a number greater than or equal to 2 "))
if(relOp4 >= 2):
    print("True")
else:
    print("False")
relOp5 = int(input("Please input a number less than 2 "))
if(relOp5 < 2):
    print("True")
else:
    print("False")
relOp6 = int(input("Please input a number less than or equal to 2 "))
if(relOp6 <= 2):
    print("True")
else:
    print("False")
#Basic for and while loops
print("This section demonstrates basic for loops")
print("Please input any word you want and the program will separate")
forEx = input("it onto separate lines ")
for x in forEx:
    print(x)
print("This section is a basic while loop")
print("It will take basic numerical values and print them until it reaches")
print("a set, designated point")
whileEx = int(input("Please input a basic numberical value less than 20 "))
while whileEx <20:
    print(whileEx)
    whileEx += 1
