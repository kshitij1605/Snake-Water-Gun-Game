import random
user_score=0
computer_score=0
play_count=10
no_of_count=0
print("Let's Play......Snake Water Gun Game")
a=['sanke',"water","gun"]
print("You have only 10 chance to play the game \n ")

b=input("Enter Your Name :- ")
while no_of_count<play_count:
    computer_turn=random.choice(a)
    user_turn = input("Choose your options:\n Snake \n Water \n Gun \n ===> ")
    if user_turn=="Snake" or user_turn=="snake":
        if computer_turn=="snake":
            print("Oohh......The Match is Tie...!")
        elif computer_turn=="water":
            user_score=user_score+1
            print(f"{a} get {user_score} points")
            print(f"Wow.......{b} are winner")
        else:
            computer_score=computer_score+1
            print(f"Computer get {computer_score} points")
            print("Ohh......Computer are winner...")
    elif user_turn=="Water" or user_turn=="water":
        if computer_turn== "water":
            print("Ohh......The Match is Tie...!")
        elif computer_turn=="gun":
            user_score = user_score + 1
            print(f"You get {user_score} points")
            print(f"Wow......{b} are winner")
        else:
            computer_score = computer_score + 1
            print(f"Computer get {computer_score} points")
            print("Ohhh......Computer are winner...")
    elif user_turn=="Gun" or user_turn=="gun":
        if computer_turn =="gun":
            print("Ohh......The Match is Tie...!")
        elif computer_turn =="snake":
            user_score = user_score + 1
            print(f"You get {user_score} points")
            print(f"Wow......{b} are winner")
        else:
            computer_score = computer_score + 1
            print(f"Computer get {computer_score} points")
            print(f"Ohhh......Computer are winner...")
    else:
        print("Wrong Input....! , Enter From The Given Options \n")
    no_of_count=no_of_count+1
    print(f"{play_count-no_of_count} chance left out of {play_count} \n")

print("*" * 30)
if computer_score>user_score:
    print(f"Game Over\nNow...{b} are a loser")
    print("-" * 30)
    print(f"{b} Score is := {user_score}\nComputer Score is := {computer_score} ")
elif computer_score<user_score:

    print("Finally.....You are a Winner")
    print("-" * 30)
    print(f"{b} Score is := {user_score}\nComputer Score is := {computer_score} ")
else:
    print("Game Over \nOhhh.... The Final Result is Tie ...!")







