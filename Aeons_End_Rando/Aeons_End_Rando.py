import csv
import random
import pprint

with open("C:/Users/Treil/Documents/Python Coding/Aeons_End_Rando/karten.csv", newline='') as karten_liste:
    balance = 0
    effekte = {"Draw": False, "Sift": False, "Trash": False, \
               "Riss bündeln": False, "Energie gewinnen": False, \
                "Geld gewinn": False, "Heilung Festung": False, \
                    "Heilung Charakter": False}
    reader = csv.DictReader(karten_liste, delimiter=',')
    karten = {"Artefakt": [], "Zauber": [], "Kristall": []}
    karten_im_spiel = {"Artefakt": [], "Zauber": [], "Kristall": []}
    for line in reader:
        if line["Typ"] in karten.keys():
            karten[line["Typ"]].append(line)

    karten_im_spiel["Artefakt"] = random.sample(karten["Artefakt"], k=2)
    karten_im_spiel["Kristall"] = random.sample(karten["Kristall"], k=3)
    karten_im_spiel["Zauber"] = random.sample(karten["Zauber"], k=4)
    for typ, karte in karten_im_spiel.items():
        for karten in karte:
            if effekte["Draw"] == False:
                if karten["Draw"] == "y":
                    effekte["Draw"] = True
                    balance += 1
            if effekte["Sift"] == False:
                if karten["Sift"] == "y":
                    effekte["Sift"] = True
                    balance += 1
            if effekte["Trash"] == False:
                if karten["Trash"] == "y":
                    effekte["Trash"] = True
                    balance += 1
            if effekte["Riss bündeln"] == False:
                if karten["Riss bündeln"] == "y":
                    effekte["Riss bündeln"] = True
                    balance += 1
            if effekte["Energie gewinnen"] == False:
                if karten["Energie gewinnen"] == "y":
                    effekte["Energie gewinnen"] = True
                    balance += 1
            if effekte["Geld gewinn"] == False:
                if karten["Typ"] != "Kristall":
                    if karten["Geld gewinn"] > "0":
                        effekte["Geld gewinn"] = True
                        balance += 1
            if effekte["Heilung Festung"] == False:
                if karten["Heilung Festung"] == "y":
                    effekte["Heilung Festung"] = True
                    balance += 1
            if effekte["Heilung Charakter"] == False:
                if karten["Heilung Charakter"] == "y":
                    effekte["Heilung Charakter"] = True
                    balance += 1
            print(karten["Typ"] + ": " + karten["Name"] + " " \
                  + karten["Kosten"])
    print(balance)
    pprint.pprint(effekte)
