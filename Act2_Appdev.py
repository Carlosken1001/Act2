#Roland Angeles Jr And Carlos Marquez


import random

def add(x, y):
    return x + y

def subtrct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y
rightAns=0
while True:
    choice = input("Enter your choice: ")
    noQuest = input("How many problems?: ")
    
    if choice in ('1', '2', '3', '4'):
       
            if choice == '1':
                for question in range(int(noQuest)):
                    num1 = float(random.randint(0, 9))
                    num2 = float(random.randrange(2, 10, 2))
                    num3 = add(num1, num2)
                    print("What is the sum of " + str(num1) + " and " + str(num2))
                    answer = float(input("Enter your answer: "))
                    if num3 == answer:
                        rightAns=rightAns+1
                        print("Correct")
                       
                    else:
                        print("Wrong! the correct answer is", num3)
                        
            
            elif choice == '2':
                for question in range(int(noQuest)):
                    num1 = float(random.randint(0, 9))
                    num2 = float(random.randrange(2, 10, 2))
                    num3 = subtrct(num1, num2)
                    print("What is the difference of " + str(num1) + " and " + str(num2))
                    answer = float(input("Enter your answer: "))
                    if num3 == answer:
                        rightAns=rightAns+1
                        print("Correct")
                    else:
                        print("Wrong! the correct answer is", num3)
            
            elif choice == '3':
                for question in range(int(noQuest)):
                    num1 = float(random.randint(0, 9))
                    num2 = float(random.randrange(2, 10, 2))
                    num3 = multiply(num1, num2)
                    print("What is the product of " + str(num1) + " and " + str(num2))
                    answer = float(input("Enter your answer: "))
                    if num3 == answer:
                        rightAns=rightAns+1
                        print("Correct")
                    else:
                        print("Wrong! the correct answer is", num3)
                
            elif choice == '4':
                for question in range(int(noQuest)):
                    num1 = round(float(random.randint(0, 9)),2)
                    num2 = round(float(random.randrange(2, 10, 2)), 2)
                    num3 = dividiby(num1, num2)
                    print("What is the Quotient of " + str(num1) + " and " + str(num2))
                    answer = float(input("Enter your answer: "))
                    if num3 == answer:
                        rightAns=rightAns+1
                        print("Correct")
                    else:
                        print("Wrong! the correct answer is", num3)
        
    
    print("Score:" + str(rightAns) + "/" + str(noQuest))
    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break

else:
    print("Invalid input")