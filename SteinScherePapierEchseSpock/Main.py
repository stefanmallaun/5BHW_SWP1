"""
https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock
http://www.samkass.com/theories/RPSSL.html

1) Als Terminal-Spiel umsetzen
2) Spielmodi COMP vs PLAYER
3) zähle wer wie oft gewonnen
4) zähle alle gewählte Symbole
5) überlege wie die Daten dauerhaft gespeichert werden könnten
6) biete ein Menü an Spielen, Statistik

Logik:
    Stein0 schlägt Eidechse3 und Schere4
    Spock1 schlägt Schere4 und Stein0
    Papier2 schlägt Stein0 und Spock1
    Eidechse3 schlägt Spock1 und Papier2
    Schere4 schlägt Papier2 und Eidechse3
    
    
    => Mensch verliert wenn:
    1: Stein0 - Eidechse3 || Schere4 => -3 || -4 mod 5 => 2 || 1
    2: Spock1 - Schere4 || Stein0 => -3 || 1 mod 5 => 2 || 1
    3: Papier2 - Stein0 || Spock1 => 2 || 1 mod 5 => 2 || 1
    => Mensch verliert immer, wenn (wahlMensch - wahlCPU) mod 5 = 1 || 2
    => CPU verliert immer, wenn (wahlMensch - wahlCPU) mod 5 = 3 || 4
    => Unentschieden, wenn (wahlMensch - wahlCPU) mod 5 = 0
"""
import random 
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors




    

def name_to_number(name):
    if(name == 'rock'):
        return 0
    elif(name == 'spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        print ("ERROR Name")
        
def number_to_name(number):
        
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        print ("ERROR Number")
    
    
    
def game(player_choice, cpu_win_count, player_win_count, draw): 
        
    print ("Player chooses " + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
        
    print ("Computer chooses " + comp_choice)
        
    difference = (comp_number - player_number) % 5

    if difference == 1 or difference == 2:
        print("Computer wins!")
        cpu_win_count += 1
    elif difference == 3 or difference == 4:
        print("Player wins!")
        player_win_count += 1
    elif difference == 0:
        print("Player and Computer tie!")
        draw += 1

    return cpu_win_count, player_win_count, draw
        
def main():
    cpu_win_count = 0
    player_win_count = 0
    draw = 0

    next_round = True
    while next_round: 
        print('Do you want to play?[y/n]: ')
        play_again = input().strip().lower()

        if play_again == 'y':
            print('Wählen Sie: ["rock", "paper", "scissors", "lizard", "spock"]: ')
            player_choice = input().strip().lower()
            if player_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
                cpu_win_count, player_win_count, drawy = game(player_choice, cpu_win_count, player_win_count, draw)
            else:
                print("Falsche Eingabe!")
        elif play_again == 'n':
            next_round = False
        else:
            print('Falsche Eingabe!')

    print("Cpu hat " + str(cpu_win_count) + " mal gewonnen")
    print("Du hast " + str(player_win_count) + " mal gewonnen")
    print("Unentschieden " + str(draw) )

      
    
    """
    TEST:
    game("rock")
    game("spock")
    game("paper")
    game("lizard")
    game("scissors")
    """
if __name__ == "__main__":
    main()
 
 

