# Zombie Dice

# Importe

import random
import pprint

# Globale Variablen

colours = ("green", "yellow", "red")
dice_in_cup = {"green": 6, "yellow": 4, "red": 3}
faces = {"green": ("brain", "brain", "brain", "feet", "feet", "shotgun"), "yellow": ("brain", "brain", "feet", "feet", "shotgun", "shotgun"), "red": ("brain", "feet", "feet", "shotgun", "shotgun", "shotgun")}
result_collection = {"brain": 0, "shotgun": 0}
dice_in_play = []
shown_faces = []
round_number = 1

# Definition Funktionen

def reset_cup():
    dice_in_cup["green"] = 6
    dice_in_cup["yellow"] = 4
    dice_in_cup["red"] = 3

def pick_dice():
    while len(dice_in_play) < 3:
        if dice_in_cup["green"] == 0 and dice_in_cup["yellow"] == 0 and dice_in_cup["red"] == 0 and len(dice_in_play) < 3:
            reset_cup()   
            for i in dice_in_play:
                dice_in_cup[i] -= 1
        dice_to_add = random.choices(colours, weights=(dice_in_cup["green"],dice_in_cup["yellow"],dice_in_cup["red"]), k=1)[0]
        dice_in_play.append(dice_to_add)
        dice_in_cup[dice_to_add] -= 1

def reset_game():
    while len(dice_in_play) > 0:
        dice_in_play.pop()

def roll_dice():
    for die in dice_in_play:
        rolled_die = random.choice(faces[die])
        shown_faces.append(rolled_die)
        if rolled_die in result_collection:
            result_collection[rolled_die] += 1   
            
def clear_dice_in_play():
    dice_to_clear = []
    for i in enumerate(dice_in_play):
        if shown_faces[i[0]] != "feet":
            dice_to_clear.append(i[0])
        else:
            continue
    dice_to_clear.sort()
    dice_to_clear.reverse()
    for i in dice_to_clear:
        dice_in_play.pop(i)
    shown_faces.clear()

def clear_results():
    result_collection["brain"] = 0
    result_collection["shotgun"] = 0
        
number_of_players = int(input("Wie viele Zombies gehen auf Jagd?\n"))
player_dict = {i : 0 for i in range(1, number_of_players + 1)}

print(player_dict)

while True:
    for player in player_dict:
        while True:
            print(f"\nRunde: {round_number}, Zombie: {player}, Gehirne: {player_dict[player]}\n") 
            choice = input("Was willst du tun? \n1. 'Enter' zum Würfeln. \n2. 'ende' für Rundenende. \n3. 'beenden' um Spiel zu beenden.\n")
            if choice.lower() == "beenden":
                exit()
            if choice.lower() == "ende":
                if result_collection["brain"] == 1:
                    print(f"Du hast überlebt und {result_collection['brain']} Gehirn gesammelt. \n")
                    player_dict[player] += result_collection["brain"]
                    reset_cup()
                    clear_results()
                    break
                else:
                    print(f"Du hast überlebt und {result_collection['brain']} Gehirne gesammelt. \n")
                    player_dict[player] += result_collection["brain"]
                    reset_cup()
                    clear_results()
                    break
             
            else:
                pick_dice()
                roll_dice()
                print(f"Gezogene Würfel:\n{dice_in_play}\n")
                print(f"Würfelergebnis:\n{shown_faces}\n")
                print(f"Würfel im Becher:\n{dice_in_cup}\n")
                print(f"Gesammelte Ergebnisse:\n{'o' * result_collection['brain']} {result_collection} {'x' * result_collection['shotgun']}\n")
                clear_dice_in_play()
                print(f"Übrige Würfel:\n{dice_in_play}\n")
                if result_collection["shotgun"] >= 3:
                    if result_collection["brain"] == 1:
                        print(f"Peng! Du bist tot! \nDu hast {result_collection['brain']} Gehirn verpasst.")
                        reset_cup()
                        clear_results()
                        break
                    else:
                        print(f"Peng! Du bist tot! \nDu hast {result_collection['brain']} Gehirne verpasst.")
                        reset_cup()
                        clear_results()
                        break
        pprint.pprint(f"Punktestand: {player_dict}")
    for player, points in player_dict.items():
        if points >= 13:
            print(f"Herzlichen Glückwunsch Zombie {player} du hast in Runde {round_number} mit {points} Gehirnen gewonnen!")
            pprint.pprint(player_dict)
            exit()
    round_number += 1