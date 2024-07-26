print("*********Rock Paper Scissor*********")
print("-------------------------------------")

import random

options = ['Rock' , 'Paper' , 'Scissors']

choice = input("Choose Rock,Paper,Scissors:")

computer_choice = random.choice(options)

print("You choose:",choice)

print("Computer choose:",computer_choice)

if(choice==computer_choice):

    print("It's a lie!")

elif(choice=="Rock" and computer_choice=='Scissors'):

    print("You Win!")

elif(choice=="Scissors" and computer_choice=="Paper"):

    print("You Win")

elif(choice=="Paper" and computer_choice=='Rock'):

    print("You Win!")

else:

    print("Computer Wins")