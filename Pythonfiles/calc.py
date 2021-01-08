
# a function that adds two numbers 
def add(num1, num2):
  result = num1 + num2
  print(str(result))
  
# a function that subtracts two numbers
def subtract(num1, num2):
  result = num1 - num2
  print(str(result))

# a function that multiplies two numbers
def multiply(num1, num2):
  result = num1 * num2
  print(str(result))

# a function that divides two numbers
def divide(num1, num2):
  print(str(num1/num2))

  statusCalculator = True
calculatorFunctions = ["multiplication", "division", "subtraction", "adding"] #List of all the function in the calculator
print("The calculator has the following functions: ")
for function in calculatorFunctions: #Goes through the list of calculatorFunctions
  print(function) #Print all the function in the calculator
while(statusCalculator): #If the user types stop, the calculator stopss working
  userInput = input("Please type the function that you want to use: ") #Ask the user what function he wants to use
  if userInput.lower() in calculatorFunctions: #Goes through the list to see if the function typed by the user is in the list
    x = int(input("Please type the first number: "))
    y = int(input("Please type the second number: "))
    if userInput.lower() == "multiplication": #Calls the required function depending on the user input
      multiply(x,y)
    elif userInput.lower() == "adding":
      add(x,y)
    elif userInput.lower() == "subtraction":
      substract(x,y)
    elif userInput.lower() == "division":
      divide(x,y)
    userInput2 = input("If you are done with the calculator, please type stop. If you want to keep using it, type any letter ")
    if userInput2.lower() == "stop": #If the user types stop, the calculator will stop
      break
  else:
    print("The function is not recognized, please type it again") #If the function is not recognized in the list of functions, it will ask to type it again
print("Thank you for using our calculator.")