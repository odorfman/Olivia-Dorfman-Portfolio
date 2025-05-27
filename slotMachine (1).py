#Olivia Dorfman
#Period 4
#1/18/25

#Initialize
import random
import time
slotSymbols=["💗","✨","⚂","☀","7"]
c=10

#Functions
def Machine():
    global c
    print("Welcome to Mr. J's slot machine!")
    while True:
        if c>0:
            spin=input("Would you like to spin?")
            spin=spin.lower()
        else:
            print("Sadly, you have run out of credits.")
            break
        if spin!="no":
            bet=int(input("How many credits would you like to bet?"))
            if c-bet<0:
                print("Sadly, you do not have enough credits to bet that amount.")
                break
            else:
                c=c-bet
                for i in range(3):
                    print("Spinning...")
                    time.sleep(2)
                slot1=random.choices(slotSymbols, weights = (5, 5, 5, 5, 1), k = 1)
                slot2=random.choices(slotSymbols, weights = (5, 5, 5, 5, 1), k = 1)
                slot3=random.choices(slotSymbols, weights = (5, 5, 5, 5, 1), k = 1)
                print(slot1[0]+" "+slot2[0]+" "+slot3[0])
                if slot1[0]=="7" and slot2[0]=="7" and slot3[0]=="7":
                    print("Congratulations! You got the jackpot!")
                    c=5*c
                    print("Credits: "+str(c))
                elif slot1==slot2 and slot2==slot3:
                    print("You win!")
                    c=3*c
                    print("Credits: "+str(c))
                else:
                    print("You lost. But do not worry, you can always spin again. Remember, most people stop playing right before they are about to win.")
                    print("Credits: "+str(c))
        else:
            print("Thank you for playing Mr. J's slot machine!")
            break



#Main
Machine()
