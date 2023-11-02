#Pokerspielsimulator
#Pokerkarten modellieren
#zufällig fünf Karten ausgeben
#Funktion welche Kombinationen beim Pokerspiel
    #Paar, Drillinge, Poker, Flush, Straße, Royal Flush, ...
#1000 mal spielen und zähle verschiedene Kombinationen
#berechne den prozentuellen Anteil einer Kombination
#richtiger Anteil recherchieren und mit ergebnis vergleichen
import random as r

colors = ['red', 'black']
suits = ['hearts', 'diamonds', 'clubs', 'spades']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def generate_deck():
    deck = [f'{rank} of {suit}' for rank in numbers for suit in suits]
    r.shuffle(deck)
    return deck

def deal_hand(deck):
    return [deck.pop() for _ in range(5)]

# Rest of your code remains the same


# Rest of your code remains the same

def is_pair(listOfCards):
    values = [card[-1] for card in listOfCards]
    for value in values:
        if values.count(value) == 2:
            return True
    return False

def is_three_of_a_kind(listOfCards):
    values = [card[-1] for card in listOfCards]
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def is_four_of_a_kind(listOfCards):
    values = [card[-1] for card in listOfCards]
    for value in values:
        if values.count(value) == 4:
            return True
    return False



def is_royal_flush(listOfCards):
    if not is_flush(listOfCards):
        return False
    
    sorted_cards = sorted(listOfCards, key=lambda card: numbers.index(card[-1]))
    royal_flush_values = ['A', 'K', 'Q', 'J', '10']
    return [card[-1] for card in sorted_cards[-5:]] == royal_flush_values

def is_full_house(listOfCards):
    rank_count = {}
    for card in listOfCards:
        rank = card[-1]
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1

    return sorted(rank_count.values()) == [2, 3]

def is_straight(cards):
    card_values = [numbers.index(card[-1]) if card[-1] in numbers else 14 if card[-1] == 'A' else 13 if card[-1] == 'K' else 12 if card[-1] == 'Q' else 11 if card[-1] == 'J' else 10 if card[-1] == '10' else 0 for card in cards]
    
    sorted_cards = sorted(card_values)
    
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    
    return True

def is_flush(listOfCards):
    first_suit = listOfCards[0][5:]
    return all(card[5:] == first_suit for card in listOfCards)

def is_straight_flush(cards):
    if not is_flush(cards):
        return False
    
    sorted_cards = sorted(cards, key=lambda card: numbers.index(card[-1]))
    
    for i in range(len(sorted_cards) - 1):
        if numbers.index(sorted_cards[i][-1]) + 1 != numbers.index(sorted_cards[i + 1][-1]):
            return False
    
    return True

def is_two_pair(listOfCards):
    rank_count = {}
    for card in listOfCards:
        rank = card[-1]
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1

    pair_counts = list(rank_count.values())
    return pair_counts.count(2) == 2


def evaluate_hand(listOfCards):
    if is_royal_flush(listOfCards):
        return "Royal Flush"
    elif is_straight_flush(listOfCards):
        return "Straight Flush"
    elif is_four_of_a_kind(listOfCards):
        return "Four of a Kind"
    elif is_full_house(listOfCards):
        return "Full House"
    elif is_flush(listOfCards):
        return "Flush"
    elif is_straight(listOfCards):
        return "Straight"
    elif is_three_of_a_kind(listOfCards):
        return "Three of a Kind"
    elif is_two_pair(listOfCards):
        return "Two Pair"
    elif is_pair(listOfCards):
        return "Pair"
    else:
        return "High Card"


# Initialize variables to count different combinations
combinations_count = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0,
}


total_simulations = 10000
for _ in range(total_simulations):
    listOfCards = []
    card = None

    while len(listOfCards) < 5:
        c = r.randint(0, 1)
        s = r.randint(0, 3)
        n = r.randint(0, 12)

        # Only clubs and spades can be black
        card = colors[c] + ' ' + suits[s] + ' ' + numbers[n]


        if card not in listOfCards and card is not None:
            listOfCards.append(card)

    # Evaluate the poker hand
    hand_result = evaluate_hand(listOfCards)

    # Count the combinations
    combinations_count[hand_result] += 1

# Calculate the percentage of each combination
combinations_percentage = {
    combination: count / total_simulations * 100 for combination, count in combinations_count.items()
}

# Display the results
for combination, percentage in combinations_percentage.items():
    print(f"{combination}: {percentage:.2f}%")
    
print(combinations_count)
