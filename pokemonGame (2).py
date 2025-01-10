#Olivia
#11/21/24


#Initialize
import random #used for the battle function. If the user guesses the same number as the computer, they win the battle and move up two levels.
#Global Varialbes
pokemon_level=0
pokemon_name=str("Pichu")
day=1
w=0
l=0
#Function
def pokemonGame(): #The function for the game that allows the user to develop their pokemon by training it and putting it to the test in battle mode. The pokemon can level up and get new names.
    while True:
        print("Welcome to Pokemon Evolution!")
        print("Choose an activity for day " + str(day))
        print("""
            1.Train
            2.Gym Battle
            3.Rest
            4.Quit
            5.Save Game
            6.Load Previous Game""")
        menu=int(input("Choose an activity for day " + str(day)))
        def train(): #levels up everyday pokemon trains
            global pokemon_name
            global pokemon_level
            global day
            print(pokemon_name + " did 3 pushups")
            pokemon_level=pokemon_level+ 1
            print(pokemon_name + " leveled up to level " + str(pokemon_level) )
            evolve()
            day=day+1
        def battle(): #if pokemon wins, it levels up 2 levels. If it loses it does not move up
            global pokemon_name
            global pokemon_level
            global day
            global w
            global l
            x=int(input("Pick a number: 1 or 2?"))
            y=random.randint(1,2)
            if x==y:
                print("You Win!")
                pokemon_level=pokemon_level + 2
                print(pokemon_name + " leveled up to level " + str(pokemon_level) )
                w=w+1 #win record
                evolve()
                day=day+1
            if x!=y:
                print("You lose")
                day=day+1
                l=l+1 #loss record
        def rest(): #displays the Pokemon's name, level, and record
            global pokemon_name
            global pokemon_level
            global day
            print(pokemon_name)
            print("level: "+str(pokemon_level))
            print("Record:"+str(w)+"-"+str(l)) #prints the record in battle
            day=day+1
        # The name of the file where the game data will be saved
        save_file = "savedgame.py"
        # Function to save the current game state
        def save_game():
            global pokemon_name
            global pokemon_level
            with open(save_file, "w") as file:  # Open the save file in write mode
                file.write(pokemon_name + "\n")  # Write the Pokémon's name
                file.write(str(pokemon_level) + "\n")  # Write the Pokémon's level (converted to string), followed by a newline
            print("Game saved successfully!")

        # Function to load a previously saved game state
        def load_game():
            global pokemon_name
            global pokemon_level
            try:
                with open(save_file, "r") as file:  # Open the save file in read mode
                    pokemon_name = file.readline().strip()  # Read the Pokémon's name and remove any extra whitespace
                    pokemon_level = int(file.readline().strip())  # Read the Pokémon's level and convert it to an integer
                print("Game loaded successfully!")
            except FileNotFoundError:
                # If the save file doesn't exist, display this message
                print("No save file found. Start a new game!")
            except ValueError:
                # If the file data is corrupted, display this message
                print("Save file is corrupted. Start a new game!")
        def evolve(): #the function that codes for the new names of the Pokemon as it reaches new levels
            global pokemon_level
            global pokemon_name
            if pokemon_level==10:#Pichu becomes Pikachu upon reaching level 10
                    pokemon_name=str("Pikachu")
                    print("You have leveled up, Pikachu!")
            if pokemon_level>=10:
                    pokemon_name=str("Pikachu")
            if pokemon_level==20:#Pikachu becomes Raichu upon reaching level 20
                    pokemon_name=str("Raichu")
                    print("You have leveled up, Raichu!")
            if pokemon_level>=20:
                    pokemon_name=str("Raichu")
        if menu==1:
            train()
        if menu==2:
            battle()
        if menu==3:
            rest()
        if menu==4:
            print("Thank you for playing!")
            break
        if menu==5:
            save_game()
        if menu==6:
            load_game()


#Main
pokemonGame()

