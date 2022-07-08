import os
clear = lambda: os.system('cls')


bidder_list = [{}, {'highest bidder': 'none'}, {'highest bid': 0}]
bidding_still_on = True

while bidding_still_on:
    clear()
    print('Welcome to the secret auction program. ')
    entered_name = input('What is your name?: ')
    entered_bid = int(input('What is your bid?: '))
    check_for_bidders = input('Are the any other bidders? Types "y" or "n". ')
    bidder_list[0].update({entered_name.title(): entered_bid})
    if entered_bid > bidder_list[2]['highest bid']:
        bidder_list[1] = {'highest bidder': entered_name.title()}
        bidder_list[2] = {'highest bid': entered_bid}
    if check_for_bidders.lower() == 'n':
        bidding_still_on = False

print(f'The winner is {bidder_list[1]["highest bidder"]} with a bid of ${bidder_list[2]["highest bid"]}. ')
