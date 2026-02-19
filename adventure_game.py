#build a text-based adventure game using Python and GitHub Copilot
print("Welcome to the Adventure Game!")
def start_game():
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's start your adventure. Do you want to explore a forest or enter a cave?")
    
    choice = input("Type 'forest' or 'cave': ").lower()
    if choice == 'forest':
        explore_forest()
    elif choice == 'cave':
        enter_cave()
    else:      
        print("Invalid choice. Please try again.") 
def explore_forest():
    print("You enter the forest and find a path leading to a mysterious tree. Do you want to follow a river or climb a tree?")
    choice = input("Type 'climb' or 'follow': ").lower()
    if choice == 'climb':
        print("You climb the tree and find a hidden treasure chest! You win!")
    elif choice == 'follow':
        print("You follow the river and encounter a wild animal. You lose!")
    else:
        print("Invalid choice. Please try again.")
def enter_cave():
    print("You enter the cave and find a fork in the path. Do you want to light a torch or proceed in the dark?")
    choice = input("Type 'torch' or 'dark': ").lower()
    if choice == 'torch':
        print("You light the torch and find a hidden passage leading to a secret room. You win!")
    elif choice == 'dark':
        print("You proceed in the dark and encounter a dangerous monster. You lose!")
    else:
        print("Invalid choice. Please try again.")  
start_game()