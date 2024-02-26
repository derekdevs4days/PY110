import random
import pprint

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


def game():
    DECK = {
        0: {'rank': '2', 'suit': 'Spades', 'value': 2, 'symbol': '♠', 'in_deck': True},
        1: {'rank': '2', 'suit': 'Hearts', 'value': 2, 'symbol': '♥', 'in_deck': True},
        2: {'rank': '2', 'suit': 'Clubs', 'value': 2, 'symbol': '♣', 'in_deck': True},
        3: {'rank': '2', 'suit': 'Diamonds', 'value': 2, 'symbol': '♦', 'in_deck': True},
        4: {'rank': '3', 'suit': 'Spades', 'value': 3, 'symbol': '♠', 'in_deck': True},
        5: {'rank': '3', 'suit': 'Hearts', 'value': 3, 'symbol': '♥', 'in_deck': True},
        6: {'rank': '3', 'suit': 'Clubs', 'value': 3, 'symbol': '♣', 'in_deck': True},
        7: {'rank': '3', 'suit': 'Diamonds', 'value': 3, 'symbol': '♦', 'in_deck': True},
        8: {'rank': '4', 'suit': 'Spades', 'value': 4, 'symbol': '♠', 'in_deck': True},
        9: {'rank': '4', 'suit': 'Hearts', 'value': 4, 'symbol': '♥', 'in_deck': True},
        10: {'rank': '4', 'suit': 'Clubs', 'value': 4, 'symbol': '♣', 'in_deck': True},
        11: {'rank': '4', 'suit': 'Diamonds', 'value': 4, 'symbol': '♦', 'in_deck': True},
        12: {'rank': '5', 'suit': 'Spades', 'value': 5, 'symbol': '♠', 'in_deck': True},
        13: {'rank': '5', 'suit': 'Hearts', 'value': 5, 'symbol': '♥', 'in_deck': True},
        14: {'rank': '5', 'suit': 'Clubs', 'value': 5, 'symbol': '♣', 'in_deck': True},
        15: {'rank': '5', 'suit': 'Diamonds', 'value': 5, 'symbol': '♦', 'in_deck': True},
        16: {'rank': '6', 'suit': 'Spades', 'value': 6, 'symbol': '♠', 'in_deck': True},
        17: {'rank': '6', 'suit': 'Hearts', 'value': 6, 'symbol': '♥', 'in_deck': True},
        18: {'rank': '6', 'suit': 'Clubs', 'value': 6, 'symbol': '♣', 'in_deck': True},
        19: {'rank': '6', 'suit': 'Diamonds', 'value': 6, 'symbol': '♦', 'in_deck': True},
        20: {'rank': '7', 'suit': 'Spades', 'value': 7, 'symbol': '♠', 'in_deck': True},
        21: {'rank': '7', 'suit': 'Hearts', 'value': 7, 'symbol': '♥', 'in_deck': True},
        22: {'rank': '7', 'suit': 'Clubs', 'value': 7, 'symbol': '♣', 'in_deck': True},
        23: {'rank': '7', 'suit': 'Diamonds', 'value': 7, 'symbol': '♦', 'in_deck': True},
        24: {'rank': '8', 'suit': 'Spades', 'value': 8, 'symbol': '♠', 'in_deck': True},
        25: {'rank': '8', 'suit': 'Hearts', 'value': 8, 'symbol': '♥', 'in_deck': True},
        26: {'rank': '8', 'suit': 'Clubs', 'value': 8, 'symbol': '♣', 'in_deck': True},
        27: {'rank': '8', 'suit': 'Diamonds', 'value': 8, 'symbol': '♦', 'in_deck': True},
        28: {'rank': '9', 'suit': 'Spades', 'value': 9, 'symbol': '♠', 'in_deck': True},
        29: {'rank': '9', 'suit': 'Hearts', 'value': 9, 'symbol': '♥', 'in_deck': True},
        30: {'rank': '9', 'suit': 'Clubs', 'value': 9, 'symbol': '♣', 'in_deck': True},
        31: {'rank': '9', 'suit': 'Diamonds', 'value': 9, 'symbol': '♦', 'in_deck': True},
        32: {'rank': '10', 'suit': 'Spades', 'value': 10, 'symbol': '♠', 'in_deck': True},
        33: {'rank': '10', 'suit': 'Hearts', 'value': 10, 'symbol': '♥', 'in_deck': True},
        34: {'rank': '10', 'suit': 'Clubs', 'value': 10, 'symbol': '♣', 'in_deck': True},
        35: {'rank': '10', 'suit': 'Diamonds', 'value': 10, 'symbol': '♦', 'in_deck': True},
        36: {'rank': 'J', 'suit': 'Spades', 'value': 10, 'symbol': '♠', 'in_deck': True},
        37: {'rank': 'J', 'suit': 'Hearts', 'value': 10, 'symbol': '♥', 'in_deck': True},
        38: {'rank': 'J', 'suit': 'Clubs', 'value': 10, 'symbol': '♣', 'in_deck': True},
        39: {'rank': 'J', 'suit': 'Diamonds', 'value': 10, 'symbol': '♦', 'in_deck': True},
        40: {'rank': 'Q', 'suit': 'Spades', 'value': 10, 'symbol': '♠', 'in_deck': True},
        41: {'rank': 'Q', 'suit': 'Hearts', 'value': 10, 'symbol': '♥', 'in_deck': True},
        42: {'rank': 'Q', 'suit': 'Clubs', 'value': 10, 'symbol': '♣', 'in_deck': True},
        43: {'rank': 'Q', 'suit': 'Diamonds', 'value': 10, 'symbol': '♦', 'in_deck': True},
        44: {'rank': 'K', 'suit': 'Spades', 'value': 10, 'symbol': '♠', 'in_deck': True},
        45: {'rank': 'K', 'suit': 'Hearts', 'value': 10, 'symbol': '♥', 'in_deck': True},
        46: {'rank': 'K', 'suit': 'Clubs', 'value': 10, 'symbol': '♣', 'in_deck': True},
        47: {'rank': 'K', 'suit': 'Diamonds', 'value': 10, 'symbol': '♦', 'in_deck': True},
        48: {'rank': 'A', 'suit': 'Spades', 'value': 11, 'symbol': '♠', 'in_deck': True},
        49: {'rank': 'A', 'suit': 'Hearts', 'value': 11, 'symbol': '♥', 'in_deck': True},
        50: {'rank': 'A', 'suit': 'Clubs', 'value': 11, 'symbol': '♣', 'in_deck': True},
        51: {'rank': 'A', 'suit': 'Diamonds', 'value': 11, 'symbol': '♦', 'in_deck': True}
    }

    HUMAN = {
        'cards': [],
        'hand_value': 0
    }

    DEALER = {
        'cards': [],
        'hand_value': 0
    }

    initial_deal(DECK, HUMAN, DEALER)
    update_hand_value(HUMAN)
    update_hand_value(DEALER)
    pprint.pprint(HUMAN)
    pprint.pprint(DEALER)

game()