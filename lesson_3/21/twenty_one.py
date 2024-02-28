import random
import os
import time


def valid_input(user_input):
    try:
        value = int(user_input)
    except ValueError:
        return False

    return value > 0


def valid_bet(user_input, max_bet):
    try:
        value = int(user_input)
    except ValueError:
        return False

    return 0 < value <= max_bet


def set_user_bankroll(human_dict):
    money = input('How much money are you playing with? ')

    while not valid_input(money):
        print('Please enter the amount of money you would like to start with.')
        money = input()

    human_dict['initial_bankroll'] = int(money)
    human_dict['current_bankroll'] = int(money)


def get_bet(human):
    amount = input('How much would you like to bet for this hand? ')
    max_bet = human['current_bankroll']

    while not valid_bet(amount, max_bet):
        if not valid_input(amount):
            print('Please enter a valid amount to bet.')
        else:
            print(f'Please enter an amount up to: ${max_bet}')
        amount = input()

    human['bet_amount'] = int(amount)


def display_bankroll(human):
    print(f'Your current bankroll is ${human['current_bankroll']}')


def display_bet(human):
    print(f'The current bet is ${human['bet_amount']}')


def get_available_cards(deck):
    return [key for key, info in deck.items() if info['in_deck']]


def deal_card(deck, player):
    available_cards = get_available_cards(deck)
    deck_key = random.choice(available_cards)
    random_card = deck[deck_key]

    deck[deck_key]['in_deck'] = False
    player['cards'].append(random_card)


def initial_deal(deck, human, dealer):
    cards_to_be_dealt = 4

    while cards_to_be_dealt:
        if cards_to_be_dealt % 2 == 0:
            deal_card(deck, human)
        else:
            deal_card(deck, dealer)

        cards_to_be_dealt -= 1


def update_hand_value(player):
    value = 0
    aces = 0

    for card in player['cards']:
        value += card['value']
        if card['rank'] == 'A':
            aces += 1

    while value > 21 and aces:
        value -= 10
        aces -= 1

    player['hand_value'] = value


def display_dealer_up_card(dealer):
    up_card = dealer['cards'][0]
    print(f'Dealer has: {up_card['rank']}{up_card['symbol']} and unknown card')


def display_hand(player):
    if player['player'] == 'HUMAN':
        curr_player = 'You have:'
    else:
        curr_player = 'Dealer:'

    cards = ' '.join([f'{card['rank']}{card['symbol']}'
                      for card in player['cards']])
    print(f'{curr_player} {cards}')


def display_hand_value(player):
    if player['player'] == 'HUMAN':
        curr_player = 'Your hand value is:'
    else:
        curr_player = "Dealer's hand value is:"

    print(f'{curr_player} {player['hand_value']}')


def bust(player):
    return player['hand_value'] > 21


def delay(seconds):
    time.sleep(seconds)


def reset_deck(deck):
    for card in deck.values():
        card['in_deck'] = True


def recap_session(human):
    os.system('clear')
    start = human['initial_bankroll']
    end = human['current_bankroll']
    print(f'You started this session with ${start} and left with ${end}')
    print(f'You are {'up' if end >= start else 'down'} ${abs(start - end)}')


def compare_hands(human, dealer):
    if not bust(human) and not bust(dealer):
        print('')
        display_hand(dealer)
        display_hand_value(dealer)
        print('')
        if human['hand_value'] > dealer['hand_value']:
            human['current_bankroll'] += human['bet_amount']
            print(f'You won ${human["bet_amount"]}')
        elif human['hand_value'] < dealer['hand_value']:
            human['current_bankroll'] -= human['bet_amount']
            print(f'You lose ${human["bet_amount"]}')
        else:
            print('It is a push')
        display_bankroll(human)


def ask_play_again():
    print('\nDo you want to keep playing? ( Y / N )')
    play_again = input().lower().strip()

    while play_again not in ['y', 'n']:
        print('Enter Y or N ')
        play_again = input().lower().strip()

    return play_again == 'y'


def clear_hands(human, dealer):
    human['cards'].clear()
    human['hand_value'] = 0
    dealer['cards'].clear()
    dealer['hand_value'] = 0


def prepare_for_next_hand(human, dealer, deck):
    clear_hands(human, dealer)
    reset_deck(deck)
    os.system('clear')
    print('Shuffling, get ready for the next hand....')
    delay(2.2)
    os.system('clear')


def display_bankroll_bet_on_top(human):
    os.system('clear')
    display_bankroll(human)
    display_bet(human)
    print('')


def handle_human_bust(human, dealer):
    print('')
    print('Over 21!')
    display_hand(dealer)
    display_hand_value(dealer)
    print('')
    print(f'You lose ${human["bet_amount"]}')
    human['current_bankroll'] -= human['bet_amount']
    display_bankroll(human)


def handle_dealer_bust(human, dealer):
    print('')
    print('Dealer busts!')
    display_hand(dealer)
    display_hand_value(dealer)
    print('')
    print(f'You win ${human["bet_amount"]}')
    human['current_bankroll'] += human['bet_amount']
    display_bankroll(human)


def game():
    deck = {
        0: {'rank': '2', 'value': 2, 'symbol': '♠', 'in_deck': True},
        1: {'rank': '2', 'value': 2, 'symbol': '♥', 'in_deck': True},
        2: {'rank': '2', 'value': 2, 'symbol': '♣', 'in_deck': True},
        3: {'rank': '2', 'value': 2, 'symbol': '♦', 'in_deck': True},
        4: {'rank': '3', 'value': 3, 'symbol': '♠', 'in_deck': True},
        5: {'rank': '3', 'value': 3, 'symbol': '♥', 'in_deck': True},
        6: {'rank': '3', 'value': 3, 'symbol': '♣', 'in_deck': True},
        7: {'rank': '3', 'value': 3, 'symbol': '♦', 'in_deck': True},
        8: {'rank': '4', 'value': 4, 'symbol': '♠', 'in_deck': True},
        9: {'rank': '4', 'value': 4, 'symbol': '♥', 'in_deck': True},
        10: {'rank': '4', 'value': 4, 'symbol': '♣', 'in_deck': True},
        11: {'rank': '4', 'value': 4, 'symbol': '♦', 'in_deck': True},
        12: {'rank': '5', 'value': 5, 'symbol': '♠', 'in_deck': True},
        13: {'rank': '5', 'value': 5, 'symbol': '♥', 'in_deck': True},
        14: {'rank': '5', 'value': 5, 'symbol': '♣', 'in_deck': True},
        15: {'rank': '5', 'value': 5, 'symbol': '♦', 'in_deck': True},
        16: {'rank': '6', 'value': 6, 'symbol': '♠', 'in_deck': True},
        17: {'rank': '6', 'value': 6, 'symbol': '♥', 'in_deck': True},
        18: {'rank': '6', 'value': 6, 'symbol': '♣', 'in_deck': True},
        19: {'rank': '6', 'value': 6, 'symbol': '♦', 'in_deck': True},
        20: {'rank': '7', 'value': 7, 'symbol': '♠', 'in_deck': True},
        21: {'rank': '7', 'value': 7, 'symbol': '♥', 'in_deck': True},
        22: {'rank': '7', 'value': 7, 'symbol': '♣', 'in_deck': True},
        23: {'rank': '7', 'value': 7, 'symbol': '♦', 'in_deck': True},
        24: {'rank': '8', 'value': 8, 'symbol': '♠', 'in_deck': True},
        25: {'rank': '8', 'value': 8, 'symbol': '♥', 'in_deck': True},
        26: {'rank': '8', 'value': 8, 'symbol': '♣', 'in_deck': True},
        27: {'rank': '8', 'value': 8, 'symbol': '♦', 'in_deck': True},
        28: {'rank': '9', 'value': 9, 'symbol': '♠', 'in_deck': True},
        29: {'rank': '9', 'value': 9, 'symbol': '♥', 'in_deck': True},
        30: {'rank': '9', 'value': 9, 'symbol': '♣', 'in_deck': True},
        31: {'rank': '9', 'value': 9, 'symbol': '♦', 'in_deck': True},
        32: {'rank': '10', 'value': 10, 'symbol': '♠', 'in_deck': True},
        33: {'rank': '10', 'value': 10, 'symbol': '♥', 'in_deck': True},
        34: {'rank': '10', 'value': 10, 'symbol': '♣', 'in_deck': True},
        35: {'rank': '10', 'value': 10, 'symbol': '♦', 'in_deck': True},
        36: {'rank': 'J', 'value': 10, 'symbol': '♠', 'in_deck': True},
        37: {'rank': 'J', 'value': 10, 'symbol': '♥', 'in_deck': True},
        38: {'rank': 'J', 'value': 10, 'symbol': '♣', 'in_deck': True},
        39: {'rank': 'J', 'value': 10, 'symbol': '♦', 'in_deck': True},
        40: {'rank': 'Q', 'value': 10, 'symbol': '♠', 'in_deck': True},
        41: {'rank': 'Q', 'value': 10, 'symbol': '♥', 'in_deck': True},
        42: {'rank': 'Q', 'value': 10, 'symbol': '♣', 'in_deck': True},
        43: {'rank': 'Q', 'value': 10, 'symbol': '♦', 'in_deck': True},
        44: {'rank': 'K', 'value': 10, 'symbol': '♠', 'in_deck': True},
        45: {'rank': 'K', 'value': 10, 'symbol': '♥', 'in_deck': True},
        46: {'rank': 'K', 'value': 10, 'symbol': '♣', 'in_deck': True},
        47: {'rank': 'K', 'value': 10, 'symbol': '♦', 'in_deck': True},
        48: {'rank': 'A', 'value': 11, 'symbol': '♠', 'in_deck': True},
        49: {'rank': 'A', 'value': 11, 'symbol': '♥', 'in_deck': True},
        50: {'rank': 'A', 'value': 11, 'symbol': '♣', 'in_deck': True},
        51: {'rank': 'A', 'value': 11, 'symbol': '♦', 'in_deck': True}
    }

    human = {
        'cards': [],
        'hand_value': 0,
        'player': 'HUMAN',
        'initial_bankroll': 0,
        'current_bankroll': 0,
        'bet_amount': 0
    }

    dealer = {
        'cards': [],
        'hand_value': 0,
        'player': 'DEALER',
    }

    set_user_bankroll(human)

    # Main Game Loop
    while True:
        get_bet(human)
        display_bankroll_bet_on_top(human)
        initial_deal(deck, human, dealer)
        update_hand_value(human)
        update_hand_value(dealer)
        display_dealer_up_card(dealer)
        display_hand(human)
        display_hand_value(human)

        # Player Loop
        while True:
            if bust(human):
                handle_human_bust(human, dealer)
                break

            print('')
            hit_stay = input('Do you want to hit or stay? ').lower().strip()
            while hit_stay not in ('hit', 'stay'):
                hit_stay = input('Hit or Stay? ').lower().strip()

            if hit_stay == 'stay':
                break

            display_bankroll_bet_on_top(human)
            deal_card(deck, human)
            display_dealer_up_card(dealer)
            update_hand_value(human)
            display_hand(human)
            display_hand_value(human)

        # Dealer Loop
        while True:
            if bust(human) or dealer['hand_value'] >= 17:
                break

            display_bankroll_bet_on_top(human)
            display_hand(human)
            display_hand_value(human)
            print('')
            print('Dealer decides to hit...')
            deal_card(deck,dealer)
            update_hand_value(dealer)

            if bust(dealer):
                handle_dealer_bust(human, dealer)


        compare_hands(human, dealer)

        if not ask_play_again():
            recap_session(human)
            break

        if human['current_bankroll'] == 0:
            print('You have no more money!')
            delay(3)
            recap_session(human)
            break

        prepare_for_next_hand(human, dealer, deck)
        display_bankroll(human)

game()