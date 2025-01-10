#Olivia
#1/6/25

#Intialize
import random #the computer chooses a random number that corresponds to rock, paper, or scissors. This choice is what the computer plays against the user.
w=0 #wins
l=0 #losses
t=0 #ties
#Functions
def RockPaperScissors(): #this function codes the game 'rock, paper, scissors' so that the user can play the game against the computer
    while True:
        global w
        global l
        global t
        print("Welcome to Rock Paper Scissors!")
        print("To play, you will choose between rock, paper, and scissors. Rock breaks scissors, scissors cuts paper, and paper covers rock. First to 10 wins.")
        player=input("Rock, Paper, or Scissors?")
        player=player.lower()
        robot=random.randint(1,3)
        if robot==1:
            robot="r"
            print("computer chose rock")
        elif robot==2:
            robot="p"
            print("computer chose paper")
        elif robot==3:
            robot="s"
            print("computer chose scissors")

        if robot=="r" and player=="rock" or robot=="p" and player=="paper" or robot=="s" and player=="scissors":
            print("You and the computer picked the same thing. It is a draw.")
            t=t+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="r" and player=="paper":
            print("Paper covers rock. You win!")
            w=w+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="p" and player=="scissors":
            print("Scissors cuts paper. You win!")
            w=w+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="s" and player=="rock":
            print("Rock breaks scissors. You win!")
            w=w+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="r" and player=="scissors":
            print("Rock breaks scissors. You lose.")
            l=l+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="p" and player=="rock":
            print("Paper covers rock. You lose.")
            l=l+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        elif robot=="s" and player=="paper":
            print("Scissors cuts paper. You lose.")
            l=l+1
            print("Score: "+str(w)+"-"+str(l)+"-"+str(t))
        else:
            print("That is not an option. Please try again")
        #the game ends when the user or computer reaches 10 points
        if w>=10:
            print("You have won the game!")
            break
        if l>=10:
            print("You lost")
            break

#Main
RockPaperScissors()
