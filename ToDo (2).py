#Olivia
#Period 4
#1/22/25

#Initialize
todolist=[]

#Functions
def ToDoList():
    print("Welcome to the very best task tracker!")
    while True:
        try:
            print("""You can:
                1. View your current list
                2. Add an item to your list
                3. Remove a task from the to-do list
                4. Sort your list alphabetically
                5. See how many items are on your list
                6. Exit the program""")
            choice=int(input("Which option would you like? (Enter number 1-6)"))
            def view(): #allows user to see their to-do list
                print(todolist)
            def add(): #allows user to add an item to their list
                new=str(input("What would you like to add?"))
                todolist.append(new)
                print("'"+new+"' has been added to your list.")
            def remove(): #allows user to remove an item
                away=str(input("What would you like to remove?"))
                todolist.remove(away)
                print("'"+away+"' has been removed from your list.")
            def alphabet():#sorts the user's list alphabetically
                todolist.sort()
                print(todolist)
            def count():#shows the user how many items they have in their list
                print(len(todolist))


            if choice==1:
                view()
            if choice==2:
                add()
            if choice==3:
                remove()
            if choice==4:
                alphabet()
            if choice==5:
                count()
            if choice==6:
                print("Thank you for using the very best task tracker!")
                break
        except:
            print("ERROR: Must enter a number digit!")
#Main
ToDoList()
