import random
from art import logo,vs
from game_data import data
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    def format_account(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f" {account_name}, a {account_description}, from {account_country}."

    def compare(guess,a_follower,b_follower):
        if a_follower > b_follower:
            return guess == "a"
        else:
            return guess == "b"


    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    user_guess = input("Who has more followers A or B:").lower()

    print("\n"*30)
    print(logo)

    account_follower = account_a["follower_count"]
    account_follower2 = account_b["follower_count"]

    is_correct = compare(user_guess,account_follower,account_follower2)

    if is_correct:
        score += 1
        print(f"You're right! Your current score: {score}")
    else:
        print(f"Sorry that's wrong! Your total score:{score}")
        game_should_continue = False
