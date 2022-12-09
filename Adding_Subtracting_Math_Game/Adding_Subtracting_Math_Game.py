'''
This is a game that is built to help 6-8 
    year olds with basic addition and subtraction. 
There should be no Negative numbers and the 
    operations should be random. 
This will go for 10 rounds and there will 
    be a score given at the end. 
The player should then be able to choose 
    to keep playing or exit
'''

import random
from operator import add, sub 

questNum = int(1)
keepPlaying = "y"


def game():
    global scoreCorrect
    global scoreIncorrect
    scoreCorrect = int(0)
    scoreIncorrect = int(0)
    global questNum

    num1 = int(random.randint(0,100))
    num2 = int(random.randint(0,100))
    operators = {"+": add, "-": sub}
    oplist = list(operators)
    op = random.choice(oplist)
    print("Question number ", questNum,":")
    print("Question: ",num1,op,num2)
    while True:
        try:
            answ = int(input("Answer: "))
        except ValueError:
            print("Please type a valid whole number.")
            continue
        else: 
            if answ == operators[op](num1,num2):
                print("Correct!")
                print(".........")
                scoreCorrect += 1
            else:
                scoreIncorrect += 1
                print("Nope", operators[op](num1,num2))
                print(".........")
            questNum += 1
            break
    



while True:
    while questNum < 11:
        game()
    print("You got ", scoreCorrect, " and", scoreIncorrect, " incorrect.")
    kPAnsw = input("Keep Playing? Y for yes, otherwise, press any key: ")
    if kPAnsw == keepPlaying:
        game()
        print("test")
    else:
        break

print("Thank's for playing!")