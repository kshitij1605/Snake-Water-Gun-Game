import random
user_score=0
computer_score=0
play_count=10
no_of_count=0
print("Let's Play......Snake Water Gun Game")
a=['sanke',"water","gun"]
print("You have only 10 chance to play the game")
while no_of_count<play_count:
    computer_turn=random.choice(a)
    user_turn = input("Choose your otpions:\n Snake \n Water \n Gun \n ===> ")
    if user_turn=="Snake" or user_turn=="snake":
        if computer_turn=="snake":
            print("Oohh...... The Match is Tie...!")
        elif computer_turn=="water":
            user_score=user_score+1
            print(f"You get {user_score} points")
            print("Wow....... You are winner")
        else:
            computer_score=computer_score+1
            print(f"Computer get {computer_score} points")
            print("Ohh... You lose the match...!")
    elif user_turn=="Water" or user_turn=="water":
        if computer_turn== "water":
            print("Ohh...The Match is Tie...!")
        elif computer_turn=="gun":
            user_score = user_score + 1
            print(f"You get {user_score} points")
            print("Wow.....Yor are winner")
        else:
            computer_score = computer_score + 1
            print(f"Computer get {computer_score} points")
            print("Ohhh......You lose the match..!")
    elif user_turn=="Gun" or user_turn=="gun":
        if computer_turn =="gun":
            print("Ohh.....The Match is Tie...!")
        elif computer_turn =="snake":
            user_score = user_score + 1
            print(f"You get {user_score} points")
            print("Wow.....Yor are winner")
        else:
            computer_score = computer_score + 1
            print(f"Computer get {computer_score} points")
            print("Ohhh......You lose the match...!")
    else:
        print("Wrong Input....! , Enter From The Given Options \n")
    no_of_count=no_of_count+1
    print(f"{play_count-no_of_count} chance left out of {play_count} \n")

print("*" * 30)
if computer_score>user_score:
    print("Game Over\nNow...You are a loser")
    print(f"Your Score is := {user_score}\nComputer Score is := {computer_score} ")
elif computer_score<user_score:

    print("Finally.....You are a Winner")
    print(f"Your Score is := {user_score}\nComputer Score is := {computer_score} ")
else:
    print("Game Over \nOhhh.... The Final Result Is Tie The Match...!")



