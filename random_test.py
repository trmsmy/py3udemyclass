#Guess my int
import  random

aint =  0

yourint = input("Guess a number from 1-10: ")

iteration = 0
while int(yourint) != aint:
    aint = random.randint(1, 10)
    iteration +=1

print("guessed int is found in "  + str(iteration)  + " iteration")


