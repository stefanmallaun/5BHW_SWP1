"""
https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock
http://www.samkass.com/theories/RPSSL.html

1) Als Terminal-Spiel umsetzen                                      ok
2) Spielmodi COMP vs PLAYER                                         ok
3) zähle wer wie oft gewonnen                                       ok  
4) zähle alle gewählte Symbole                                      ok
5) überlege wie die Daten dauerhaft gespeichert werden könnten      ok
6) biete ein Menü an Spielen, Statistik                             ok

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
    
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors

"""
import random 



def name_to_number(name):
    return {'rock': 0, 'spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}.get(name, "ERROR Name")

def number_to_name(number):
    return {0: 'rock', 1: 'Spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}.get(number, "ERROR Number")


def load_statistics(filename):
    stats = {'rock': 0, 'spock': 0, 'paper': 0, 'lizard': 0, 'scissors': 0}
    try:
        with open(filename, "r") as file:
            for line in file:
                choice, count = line.split(": ")
                if choice in stats:
                    stats[choice] = int(count)
    except FileNotFoundError:
        print(f"No existing statistics file found. A new one will be created: {filename}")
    return stats


def update_statistics(choice, stats):
    if choice in stats:
        stats[choice] += 1


def save_statistics(stats, filename):
    with open(filename, "w") as file:
        for choice, count in stats.items():
            file.write(f"{choice}: {count}\n")

# Main game function
def game(player_choice, cpu_win_count, player_win_count, draw, stats): 
    print ("Player chooses " + player_choice)
    update_statistics(player_choice, stats)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses " + comp_choice)
    difference = (player_number - comp_number) % 5
    if difference == 1 or difference == 2:
        print("Computer wins!")
        cpu_win_count += 1
    elif difference == 3 or difference == 4:
        print("Player wins!")
        player_win_count += 1
    else:
        print("Player and Computer tie!")
        draw += 1
    return cpu_win_count, player_win_count, draw

def main():
    stats_filename = 'SteinScherePapierEchseSpock/game_statistic.txt'
    stats = load_statistics(stats_filename)
    cpu_win_count, player_win_count, draw = 0, 0, 0

    while True:
        print("\nMENU")
        print("1. Play Game")
        print("2. View Statistics")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            while True: 
                play_again = input('Do you want to play? [y/n]: ').strip().lower()
                if play_again == 'y':
                    player_choice = input('Choose ["rock", "paper", "scissors", "lizard", "spock"]: ').strip().lower()
                    if player_choice in stats:
                        cpu_win_count, player_win_count, draw = game(player_choice, cpu_win_count, player_win_count, draw, stats)
                    else:
                        print("Invalid input!")
                elif play_again == 'n':
                    break
                else:
                    print('Invalid input!')
        elif choice == '2':
            print("\nPlayer Choice Statistics:")
            for choice, count in stats.items():
                print(f"{choice}: {count}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    save_statistics(stats, stats_filename)
    print(f"\nGame Summary: Cpu wins: {cpu_win_count}, Player wins: {player_win_count}, Draws: {draw}")


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
