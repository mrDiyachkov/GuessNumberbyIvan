import random

print(f"For quit press Q")

breakingpoint=0
pointscounter=0

fauls=0

while True:
    computer_number=random.randint(1,100)
    if fauls == 1:
        break

    while True:
        player_number=input("Guess the number (1-100): ")
        if player_number=="Q" or player_number=="q":
            print(f"Your score <{pointscounter}> points")
            fauls+=1
            break
        elif breakingpoint==3:
            print(f"I dont want to play with you any more...")
            fauls+=1
            break
        elif not player_number.isdigit():
            breakingpoint+=1
            print(f"I sad gues number !, try again ....")
            continue

        player_number=int(player_number)

        if player_number == computer_number:
            print(f"You guess it!!!")
            print(f"Nice + 10 points!!")
            pointscounter+=10
            break
        elif player_number > computer_number:
            print(f"Too High!")
        elif player_number < computer_number:
            print(f"Too Low!")
