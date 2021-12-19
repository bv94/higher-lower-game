import game_data
import art
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_intel(data):
    print(f"""here we have
    {data["name"]}
    a {data["description"]} from {data["country"]}
    """)


def follower_count_returner(data):
    return data["follower_count"]


def pick_random_data(data):
    return random.choice(data.data)


# main game loop starts here
print(art.logo)
playing = True
won_so_far = True
level = 0
user_guess = ""
competitor_a = pick_random_data(game_data)
competitor_b = pick_random_data(game_data)
while(playing):

    while(competitor_a == competitor_b):
        competitor_b = pick_random_data(game_data)
    level += 1
    print_intel(competitor_a)
    print(art.vs)
    print_intel(competitor_b)
    user_guess = input(
        "who has more followers?\n'a' for first option, 'b' for second option\n>")
    cls()
    # evaluates if user was right or not, else this program cancels user in twitter, XD
    if((user_guess == 'a' and follower_count_returner(competitor_a) > follower_count_returner(competitor_b))):

        print("you are correct,\n :>")
    elif(user_guess == 'b' and follower_count_returner(competitor_b) > follower_count_returner(competitor_a)):

        print("you are correct,\n :>")
    else:
        won_so_far = False
        print("incorrect guess\n :<")
        print(f"you managed to reach level {level}")

    # assigns new competitors here
    competitor_b = competitor_a
    competitor_b = pick_random_data(data=game_data)

    #
    if(not(won_so_far)):
        if(input("would you like to give it another go\n 'y' for yes , 'n' for no\n>") == 'n'):
            print("you have had a good go,\n hope you play again soon :>")
            playing = False
        else:
            # resets the game
            playing = True
            won_so_far = True
            level = 0
