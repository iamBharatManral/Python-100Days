import os

bidders = []


def print_header():
    print("\n\t======================================")
    print("\tWelcome to the secret auction program!\n")
    print("\t======================================\n")


def user_inputs():
    name = input("What's your/other bidder's name? ")
    bid = int(input("What's your bid? "))
    bidders.append([name, bid])
    other_bids = input("\nAre there any other bidders? Type 'yes' or 'no': ")
    os.system("clear")
    return other_bids


def show_result():
    max = -1
    for bidder in bidders:
        name = bidder[0]
        bid = bidder[1]
        if bid > max:
            max = bid
    print(f"\nThe winner is {name} with a bid of Rs.{bid}.")


def main():
    print_header()
    while True:
        if user_inputs() == 'no':
            show_result()
            exit(0)


main()
