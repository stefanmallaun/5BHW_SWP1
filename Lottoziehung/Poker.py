import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    return deck

def draw_hand(deck):
    hand = random.sample(deck, 5)
    return hand

def is_flush(hand):
    suits = [card['suit'] for card in hand]
    return len(set(suits)) == 1

# Weitere Funktionen für andere Kombinationen können hier hinzugefügt werden

def main(num_simulations):
    deck = create_deck()
    combinations = {'Flush': 0}

    for _ in range(num_simulations):
        hand = draw_hand(deck)
        if is_flush(hand):
            combinations['Flush'] += 1

    for combo, count in combinations.items():
        print(f'{combo}: {count/num_simulations * 100:.2f}%')

if __name__ == '__main__':
    main(100000)
