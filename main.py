import random
import art

def bj_updates():
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def final_reveal():
    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

def bj_round():
    deal_card_to_pc()
    deal_card_to_pc()
    deal_card_to_computer()
    deal_card_to_computer()
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def deal_card_to_pc():
    player_hand.append(random.choice(cards))
    ace_check(player_hand)

def deal_card_to_computer():
    computer_hand.append(random.choice(cards))
    ace_check(computer_hand)

def ace_check(hand):
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start_game == 'y':
    print(art.logo)

while start_game == "y":
    hit_or_pass = ""
    player_hand = []
    computer_hand = []
    bj_round()

    if sum(player_hand) == 21:
        bj_updates()
        print("You win! your total score is:", sum(player_hand))

    if sum(player_hand) > 21:
        bj_updates()
        print("You lose! your total score is:", sum(player_hand))
    if sum(player_hand) < 21:
        hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        while hit_or_pass == 'y':
            deal_card_to_pc()
            bj_updates()
            if sum(player_hand) < 21:
                hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                hit_or_pass = 'n'
    if sum(player_hand) > 21:
        print("You lose! your total score is:", sum(player_hand))

    if hit_or_pass == 'n' and sum(player_hand) <= 21:
        while sum(computer_hand) < 17:
            deal_card_to_computer()
    final_reveal()
    if sum(player_hand) <= 21:
        if sum(computer_hand) > 21:
            print("Computer busted! You win!")
        elif sum(player_hand) == sum(computer_hand):
            print("You and the computer draw! You both Tie!")
        elif sum(player_hand) > sum(computer_hand):
            print("You win! Your total score is:", sum(player_hand))
        else:
            print(f"You lose! Your total score is:", sum(player_hand), "while the computers final score is", sum(computer_hand))
    start_game = input("Do you want to play a game? Type 'y' or 'n': ")
