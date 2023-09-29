import random

global x
x = 0

def game(computer, person):
    global x
    if computer == person:
        print("Draw")
    elif computer == 1 and person == 3:
        print("You lose")
        x -= 1
    elif computer == 2 and person == 1:
        print("You lose")
        x -= 1
    elif computer == 3 and person == 2:
        print("You lose")
        x -= 1
    else:
        print("You win")
        x += 1

while True:
    computer = random.randint(1, 3)
    person = int(input("Enter (1 for Stone), (2 for Paper), (3 for Scissor): "))
    game(computer, person)
    
    print()
    choice = input("Do you want to play again? [y/n] ")
    print()

    if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
        continue
    break

print("Your Score:", x)
