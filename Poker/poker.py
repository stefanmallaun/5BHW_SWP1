#Pokerspielsimulator
#Pokerkarten modellieren
#zufällig fünf Karten ausgeben
#Funktion welche Kombinationen beim Pokerspiel
    #Paar, Drillinge, Poker, Flush, Straße, Royal Flush, ...
#1000 mal spielen und zähle verschiedene Kombinationen
#berechne den prozentuellen Anteil einer Kombination
#richtiger Anteil recherchieren und mit ergebnis vergleichen
import random as r

# Numerical representations for colors, suits, and numbers
colors = [0, 1]  # 0 for black, 1 for red
suits = [0, 1, 2, 3]  # 0 for clubs, 1 for diamonds, 2 for hearts, 3 for spades
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def is_pair(listOfCards):
    values = [card % 13 for card in listOfCards]  # Use modulo to get the number
    for value in values:
        if values.count(value) == 2:
            return True
    return False

def is_three_of_a_kind(listOfCards):
    values = [card % 13 for card in listOfCards]
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def is_four_of_a_kind(listOfCards):
    values = [card % 13 for card in listOfCards]
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def is_royal_flush(listOfCards):
    if not is_flush(listOfCards):
        return False

    sorted_cards = sorted(listOfCards, key=lambda card: card % 13)
    royal_flush_values = [0, 11, 12, 10, 9]  # Numerical values for 'A', 'K', 'Q', 'J', '10'
    return [card % 13 for card in sorted_cards[-5:]] == royal_flush_values

def is_full_house(listOfCards):
    rank_count = {}
    for card in listOfCards:
        rank = card % 13
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1

    return sorted(rank_count.values()) == [2, 3]

def is_straight(cards):
    card_values = [card % 13 for card in listOfCards]
    
    sorted_cards = sorted(card_values)
    
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    
    return True

def is_flush(listOfCards):
    first_suit = listOfCards[0] // 13
    return all(card // 13 == first_suit for card in listOfCards)

def is_straight_flush(cards):
    if not is_flush(cards):
        return False
    
    sorted_cards = sorted(cards, key=lambda card: card % 13)
    
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] % 13 + 1 != sorted_cards[i + 1] % 13:
            return False
    
    return True

def is_two_pair(listOfCards):
    rank_count = {}
    for card in listOfCards:
        rank = card % 13
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

total_simulations = 1000000
for _ in range(total_simulations):
    listOfCards = []

    while len(listOfCards) < 5:
        c = r.choice(colors)
        s = r.choice(suits)
        n = r.randint(0, 12)

        card = c * 13 + s * 13 + n

        if card not in listOfCards:
            listOfCards.append(card)

    hand_result = evaluate_hand(listOfCards)

    combinations_count[hand_result] += 1

combinations_percentage = {
    combination: count / total_simulations * 100 for combination, count in combinations_count.items()
}

# Display the results
for combination, percentage in combinations_percentage.items():
    print(f"{combination}: {percentage:.2f}%")

print(combinations_count)
