
'''
This is a game that is built to help 6-8 year olds with basic addition
and subtraction. There should be no Negative numbers and the operations 
should be random. This will go for 10 rounds and there will be a score
given at the end
'''

import random
import operator



questNum = int(1)
scoreCorrect = int(0)
scoreIncorrect = int(0)

while questNum < 11:
    num1 = int(random.randint(0,101))
    num2 = int(random.randint(0,101))
    operators = ["+","-"]
    operator = random.choice(operators)
    print("Question number ", questNum,":")
    print("Question: ",num1,operator,num2)
    answ = input("Answer: ")
    while True:
        try:
            int(answ)
        except ValueError:
            print("Please type a valid whole number.")
            continue
        else: 
            break
    if answ == (num1,operator,num2):
        scoreCorrect +=1
    else:
        scoreIncorrect +=1
    questNum +=1

print("You got ", scoreCorrect, " and", scoreIncorrect, " incorrect.")
