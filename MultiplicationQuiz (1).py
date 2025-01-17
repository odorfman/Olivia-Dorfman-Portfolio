#Olivia
#1/8/25

#Initialize
import random #this allows the computer to come up with random numbers for the user to multiply
import time #allows the user to see how long it took them to answer the questions
c=0 #tracks the amount of correct answers
t=0 #the variable that tracks the total amount of questions attempted
#Functions
def MultiplicationQuiz(): #allows the user to ask the computer to create a multiplication quiz with numbers of varying difficulty
    while True:
        global c
        global t
        print("Welcome to the multiplication game! I will give you some problems for you to practice your skills. Good luck!")
        number=int(input("How many questions would you like to answer?"))
        difficulty=str(input("Would you like to answer easy, medium, hard, or genius level questions?"))
        start_time=time.monotonic() #begins the stopwatch
        #time.sleep(5) #delays the stopwatch 5 seconds so that the user can read the questions
        for i in range(number):
            difficulty=difficulty.lower()
            if difficulty=="easy":
                multiplicand=random.randint(0,10) #the multiplicand will be between the numbers 0 and 10
                multiplier=random.randint(0,10) #the multiplier will be between the numbers 0 and 10

            elif difficulty=="medium":
                multiplicand=random.randint(10,20) #the multiplicand will be between the numbers 10 and 20
                multiplier=random.randint(0,10) #the multiplier will be between the numbers 0 and 10

            elif difficulty=="hard":
                multiplicand=random.randint(10,50) #the multiplicand will be between the numbers 10 and 50
                multiplier=random.randint(10,50) #the multiplier will be between the numbers 10 and 50

            else:
                multiplicand=random.randint(100,1000) #the multiplicand will be between the numbers 100 and 1000
                multiplier=random.randint(100,1000) #the multiplier will be between the numbers 100 and 1000

            answer=int(input("What is "+str(multiplicand)+" times "+str(multiplier)+"?"))
            if answer==multiplicand*multiplier:
                print("Correct!")
                c=c+1 #adds 1 to the correct variable
                t=t+1 #adds 1 to the total variable
            else:
                print("Incorrect. The correct answer was "+str(multiplicand*multiplier)+".")
                t=t+1
        if c==1:
            print("You got "+str(c)+" question correct out of "+str(t)+" total questions. Nice work!")

        else:
            print("You got "+str(c)+" questions correct out of "+str(t)+" total questions. Nice work!")
        end_time=time.monotonic() #stops the stopwatch
        elapsed_time=end_time-start_time
        x=round(int(elapsed_time), 2) #rounds the time to the hundredths place
        print("It took you approximately "+str(x)+" seconds to complete the quiz.") #displays how long it took the user to complete the problems
        again=input("Would you like to keep going?")
        again=again.lower()
        if again=="no":
            print("Thank you!")
            break
        else:
            print("Let's keep going!")



#Main
MultiplicationQuiz()
