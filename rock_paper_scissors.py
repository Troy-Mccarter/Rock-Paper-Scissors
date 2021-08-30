import random, time

print("""
                ----------<==Rock-Paper-Scissor==>----------
                            """)

# taking input of total chances to be run 
chances = input("Total number of chances: ")
check_chances = chances.isdigit()  # checking if input in 'chances' is 'digit' or not
while check_chances is False:  # if no then 'check_chances' return 'False' and if it's 'False'
    time.sleep(0.15)
    print("\nInvalid literal!")
    time.sleep(0.25)
    print("Note: Only natural numbers are allowed!\n")
    time.sleep(0.35)
    chances = input("Enter total number of chances again: ")  # again taking input as 'chances' as previously taken
    check_chances = chances.isdigit()  # again checking if 'chances' is 'True' or 'False' and if it's 'False' then it will go back and runs while loop until 'True' comes
    if check_chances is True:  # 'True' comes when input in 'chances' is digit and if it's 'True'
        break  # then loop breaks
chances = int(chances)  # converts chances from 'string' to 'int'

num_of_chances = 0  # initial chances 
# initial points 
computer_points = 0  
player_points = 0

choices = ["r", "p", "s"]  # 'r' for rock, 'p' for paper and 's' for scissor

print("[Choices: 'r', 'p' and 's']\n")

while num_of_chances < chances:
    time.sleep(0.15)
    player = input("Enter: ")
    computer = random.choice(choices)  # computer chooses random literal from choices
    
    try:
        # Computer :]
        if computer == "r" and player == "s":
            time.sleep(0.25)
            print("                             Computer got a point :]")
            computer_points = computer_points + 1  # here computer wins! computer_points adds +1 everytime  
            time.sleep(0.35)
            print(f"Computer points: {computer_points}\n")
        elif computer == "s" and player == "p":
            time.sleep(0.25)
            print("                             Computer got a point :]") 
            computer_points = computer_points + 1
            time.sleep(0.35)
            print(f"Computer points: {computer_points}\n")
        elif computer == "p" and player == "r":
            time.sleep(0.25)
            print("                             Computer got a point :]")
            computer_points = computer_points + 1
            time.sleep(0.35)
            print(f"Computer points: {computer_points}\n")
        
        # No one :o
        elif computer == player:
            time.sleep(0.15)
            print("                             Tie :o")
        
        # Player :)
        elif player == "r" and computer == "s":
            time.sleep(0.25)
            print("                             Player got a point :)") 
            player_points = player_points + 1  # here player wins! player_points adds +1 everytime
            time.sleep(0.35)
            print(f"Player points: {player_points}\n")
        elif player == "s" and computer == "p":
            time.sleep(0.25)
            print("                             Player got a point :)")
            player_points = player_points + 1
            time.sleep(0.35)
            print(f"Player points: {player_points}\n")
        elif player == "p" and computer == "r":
            time.sleep(0.25)
            print("                             Player got a point :)")
            player_points = player_points + 1
            time.sleep(0.35)
            print(f"Player points: {player_points}\n")
            
    except:  # if player entered a literal other then literals in choices
        time.sleep(0.15)
        print("Invalid!\n")  # then this will be printed
        
    num_of_chances = num_of_chances + 1  # everytime loop runs/repeat result addition of +1 in num_of_chances
    chances_left = chances - num_of_chances  # everytime loop runs/repeat result to the subtraction of num_of_chances it executed the last time
    time.sleep(0.15)
    print(f"[{chances_left} chances left out of {chances}]\n")  # prints chances left out of total number of chances
    
if computer_points > player_points:  # if total points of the computer > of the player  
    time.sleep(0.15)
    print("Computer Won!\n")   
elif player_points > computer_points:  # if total points of the player > of the computer  
    time.sleep(0.15)
    print("Player Won!\n")  
else:  # if total points of the computer == of the player
    time.sleep(0.15)
    print("Match Tie!")  

print("Game Over!\n")