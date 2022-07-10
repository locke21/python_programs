import random
import os

clear = lambda: os.system('cls')
playing_blackjack = True
card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, ]
suits = ["Jack", "Queen", "King", ]

dealer_hand = random.choices(card_deck, k=2)
player_hand = random.choices(card_deck, k=2)
player_hand_displayed = []
dealer_hand_displayed = []


def change_face_card(card):
    if card == 11:
        return "Ace"
    elif card == 10:
        return random.choice(suits)
    else:
        return card


def calc_total(hand):
    aces = sum(1 for ace in hand if ace == 11)
    total = sum(card for card in hand)
    while total > 21:
        if aces >= 1:
            total -= 10
            aces -= 1
        else:
            break
    return total


def check_dealers_hand(dealer_hand):
    if calc_total(hand=dealer_hand) > calc_total(hand=player_hand):
        print(f'Players hand: {player_hand_displayed}. ')
        print(f'Dealers hand: {dealer_hand_displayed}. \n')
        print(f'You lose with a {calc_total(hand=player_hand)}. Dealer has {calc_total(hand=dealer_hand)}! ')
        quit()
    while calc_total(dealer_hand) < 17:
        new_card = random.choice(card_deck)
        dealer_hand.append(new_card)
        new_card = change_face_card(card=new_card)
        dealer_hand_displayed.append(new_card)
    if calc_total(dealer_hand) < calc_total(player_hand):
        new_card = random.choice(card_deck)
        dealer_hand.append(new_card)
        new_card = change_face_card(card=new_card)
        dealer_hand_displayed.append(new_card)
    check_winner()


def check_winner():
    print(f'Players hand: {player_hand_displayed}. ')
    print(f'Dealers hand: {dealer_hand_displayed}. \n')
    if calc_total(hand=player_hand) > calc_total(hand=dealer_hand):
        print(f'You win with a {calc_total(hand=player_hand)}. Dealer has {calc_total(hand=dealer_hand)}! ')
    elif calc_total(hand=dealer_hand) > 21:
        print(f'You win with a {calc_total(hand=player_hand)}. Dealer went over with a {calc_total(hand=dealer_hand)}! ')
    elif calc_total(hand=player_hand) < calc_total(hand=dealer_hand):
        print(f'You lose with a {calc_total(hand=player_hand)}. Dealer has {calc_total(hand=dealer_hand)}! ')
    else:
        print(f'Tie with a {calc_total(hand=player_hand)}. Dealer has {calc_total(hand=dealer_hand)}! ')

for card in player_hand:
    player_hand_displayed.append(change_face_card(card))
for card in dealer_hand:
    dealer_hand_displayed.append(change_face_card(card))

clear()
print(f"Dealer: {len(dealer_hand)} cards - Dealer shows: {dealer_hand_displayed[0]}")
print(f"Player: {len(player_hand)} cards - Total: {calc_total(hand=player_hand)} "
      f"|| Your hand: {(', '.join(map(str, player_hand_displayed)))}. ")

while playing_blackjack:
    deal_card = input('\nWould you like to Hit(1 or H) or Stay (2 or S)? ')
    clear()
    if deal_card == "1" or deal_card.lower() == "h":
        new_card = random.choice(card_deck)
        player_hand.append(new_card)
        new_card = change_face_card(card=new_card)
        player_hand_displayed.append(new_card)
        print(f"Card dealt was: {new_card}.")
        print(f"Dealer: {len(dealer_hand)} cards || Dealer shows: {dealer_hand_displayed[0]}")
        print(f"Player: {len(player_hand)} cards - Total: {calc_total(hand=player_hand)} "
              f"|| Your hand: {(', '.join(map(str, player_hand_displayed)))}. ")
        if calc_total(hand=player_hand) > 21:
            print(f'Sorry you lose with a {calc_total(hand=player_hand)}. Dealer has {calc_total(hand=dealer_hand)}! ')
            quit()
    else:
        playing_blackjack = False
        check_dealers_hand(dealer_hand)
