import random
import os
clear = lambda: os.system('cls')

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
suit = ["Jack", "Queen", "King"]
player_cards = []
dealer_cards = []


def continue_game():
    print("")
    play_again = input('Would you like to play again? "y" or "n"? ').lower()
    if play_again == 'y' or play_again == "1" or play_again == "yes":
        player_cards.clear()
        dealer_cards.clear()
        game_start()
    else:
        quit()


def endgame():
    '''calculating winner'''
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)
    if dealer_score > 21:
        print(f'You win with a {player_score}! Dealer went over with {dealer_score}. ')
    elif player_score > dealer_score:
        print(f'You win with a {player_score}! Dealer had {dealer_score}. ')
    elif dealer_score > player_score:
        print(f'You lose with a {player_score}! Dealer had {dealer_score}. ')
    elif player_score == dealer_score:
        print(f'Both players tied with {player_score}! ')
    continue_game()


def dealer_turn():
    dealer_check = (sum(dealer_cards))
    if dealer_check < 17:
        card = 0
        print(f'Dealer flips a {dealer(card)} over. ')
        dealer_turn()
    else:
        endgame()


def hit_stay(card):
    choice = input('1.Draw more cards?(hit) ''\n''2.Keep hand.(stay) ').lower()
    if choice == "hit" or choice == '1' or choice == "draw":
        print(f"You drew a {deal_cards(card)}. ")
        player_total(card)
        hit_stay(card)
    elif choice == 'stay' or choice == '2' or choice == "keep":
        print(f'You hold your hand at {sum(player_cards)}. ')
        dealer_turn()
    else:
        print('Invalid Choice!')
        hit_stay(card)


def dealer(card):
    '''dealers hand'''
    card = random.choice(deck)
    dealer_cards.append(card)
    if card == 10: card = random.choice(suit)
    elif card == 11: card = "Ace"
    return card


def deal_cards(card):
    card = random.choice(deck)
    player_cards.append(card)
    if card == 10: card = random.choice(suit)
    elif card == 11: card = "Ace"
    return card


def player_total(card):
    if 11 in player_cards and sum(player_cards) > 21:
        print('Over 21! Changing value of Aces. ')
        player_cards.remove(11)
        player_cards.append(1)
        print(f"Current Total: {sum(player_cards)}. ")
        return
    elif sum(player_cards) > 21:
        print(f"You lose! You went over with a {sum(player_cards)}. ")
        continue_game()
    elif sum(player_cards) == 21:
        input(f"21! BlackJACK! Let's see what the dealer will get! ")
        dealer_turn()
    else:
        print(f"Current Total: {sum(player_cards)}. ")
        hit_stay(card)


def game_start():
    card = 0
    clear()
    print(f'First card is {deal_cards(card)}. Second card is {deal_cards(card)}. ')
    print(f'Dealer first card is showing {dealer(card)}. ')
    player_total(card)


game_start()
