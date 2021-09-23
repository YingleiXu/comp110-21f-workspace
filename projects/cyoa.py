"""This is my first project for COMP110."""
__author__ = "730529273"
from random import randint
points: int
# This variable is used to track "adventure points."
player: str
pet_name: str = "PikaChu"
PHOTO: str = "\U0001F606"


def main() -> None:
    """This is the entrypoint of this game."""
    global points
    global PHOTO
    points = 0
    greet()
    print(f"You start from {points} point, let's takes an adventure!{PHOTO}")
    while True:
        player_choice = getChoice()
        if player_choice == "quit":
            print(f"You have got {points} points!")
            break
        elif player_choice == "play":
            points = choice_play(points)
        elif player_choice == "guess":
            points = guess_number(points)
        elif player_choice == "feed":
            choice_feed()
        else:
            print("Sorry, I don't understand!")
            continue
        print(f'Total points:{points}')


def greet() -> None:
    """This is a greeting procedure of this game."""
    global player
    player = (input("What's your name? "))
    print(f"Hello, {player}! My name is {pet_name}.")


def guess_number(points: int) -> int:
    """This is a game within game."""
    rand: int = randint(1, 6)
    user_guess: int
    global player
    while True:
        user_guess = int(input(f'Hello {player},Please choose one number from 1 to 6:'))
        if user_guess < 1 or user_guess > 6:
            print('Please enter a number from 1 to 6')
        elif user_guess == rand:
            print('Bingo')
            points += 10
        else:
            print('You guessed wrong')
            points += 1
    return points


def getChoice():
    """This is what player chooses."""
    print(f"Hey {player}, please choose your own adventure! ")
    print('Please choose one from the follows:')
    print('[play]')
    print('[guess]')
    print('[feed]')
    print('[quit]')
    return input()


def choice_play(points: int) -> int:
    """This is the play time that the player chooses."""
    global player
    play_time = int(input(f"Hey {player},please enter the play time(hour):"))
    if play_time < 4:
        print(f"{pet_name} is happy")
        points += play_time * 2
    else:
        print(f"{pet_name} is tired")
        points += 1
    return points


def choice_feed() -> None:
    """This is what player will choose to feed."""
    global points
    global player
    while True:
        print(f'Hello {player},please choose a food:')
        print('1.apple')
        print('2.orange')
        print('3.watermelon')
        food = input()
        if food == 'apple':
            points += 2
        elif food == 'orange':
            points += 4
        elif food == 'watermelon':
            points += 5
        else:
            print('Please choose a correct food!')
            continue
        break
    print("Yummy~")


if __name__ == "__main__":
    main()
print("Bye!")
