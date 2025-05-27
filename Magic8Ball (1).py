#Olivia Dorfman
#Period 4
#1/24/25

#Initialize
import random
import time
answerlist=["Yes", "No", "Maybe", "Ask again", "Maybe if you stopped asking", "Dude, how would I know that?", "Never", "Most definetly", "Ask Mr. J", "Absolutely!", "Absolutely NOT", "Only if you dream it", "This is beyond the scope of what I can do", "Sure. That will be $500", "My sources say no", "My sources say yes", "idk", "Concentrate and ask again"]


#functions
def magicBall():
    print("Welcome to your magic 8-ball!")
    print("""     .----.
    /   _   \
    |  (8)  |
    \   ^   /
    '-...-'""")
    while True:
            ques=input("What would you like to ask?")
            x=ques.endswith("?")
            if x==False:
                print("ERROR: Please use a question mark!")
            else:
                for i in range(3):
                    print("Shaking...")
                    time.sleep(2)
                print(random.choice(answerlist))
                again=input("Would you like to ask another question?")
                again=again.lower()
                if again!="no":
                    print("Great!")
                else:
                    print("Thank you for using!")
                    break

#main
magicBall()
