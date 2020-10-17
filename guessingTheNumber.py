import random 


minNum = 1
maxNum = 100

magicNum = random.randint(minNum, maxNum)

massage = "The magic number is between {0} and {1}"

print(massage.format(minNum,maxNum))

found = False

while not found:
    print("Guess what it is! ")
    guess = int(input())
    if guess == magicNum:
        found = True
        print("*****")
        
    if guess < magicNum:
        print("Too low")
        
    if guess > magicNum:
        print("Too high")
         
print("You got it!")


#print(magicNum)
