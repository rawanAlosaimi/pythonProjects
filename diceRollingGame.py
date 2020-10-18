import random

def generateNumber():
    number = random.randint(1,6)

    print(number)


print("roll the dice")

generateNumber()

print("would like to roll the dice again")

print("y for yes, n for no")

again = input()


while again == "y":
    generateNumber()

    print("would like to roll the dice again")
    print("y for yes, n for no")
    
    again = input()

    if again == "n":
        break


print("Thanks!")
