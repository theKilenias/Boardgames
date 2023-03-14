import random

#Festlegen der Variablen


Insel = 'N'
Geister = ['Hunger des Ozeans', 'Lebenskraft der Erde', 'Sonnengenährter Fluss', 'Pfeilschneller Blitzschlag', 'Flackernder Schatten', 'Wildwucherndes Grün', 'Stimme des Donners', 'Bote der Albträume', 'Seele des Flächenbrandes', 'Unter der Insel schlummernde Schlange', 'Reißzähne im Dickicht', 'Hüter der verbotenen Wildniss', 'Sternenlicht sucht Gestalt', 'Tagessplitter teilen den Himmel', 'Trotzendes Felsgestein', 'Rache in Gesalt brennender Seuche', 'Finder unsichtbarer Wege', 'Grinsender Gestaltwandler macht Ärger', 'Viele bewegen sich als eines', 'Nebel des leisen Todes', 'Hochaufragender Vulkan', 'Verlockung der tiefsten Wälder', 'Wandelndes Urgedächtnis', 'Sturzregen durchnässt die Welt']
Nationenstufe = {1:['Königreich Brandenburg-Preussen 0', 'Königreich England 0', 'Königreich Schweden 0', 'Zarentum Russland 0'], 
                 2:['Königreich Brandenburg-Preussen 1', 'Königreich Schweden 1', 'Königreich Frankreich 0', 'Habsburger Monarchie 0'], 
                 3:['Königreich England 1', 'Königreich Schweden 2', 'Königreich Frankreich 1', 'Habsburger Monarchie 1', 'Zarentum Russland 1'],
                 4:['Königreich Brandenburg-Preussen 2', 'Königreich England 2', 'Zarentum Russland 2'],
                 5:['Königreich Schweden 3', 'Königreich Frankreich 2', 'Habsburger Monarchie 2'],
                 6:['Königreich Brandenburg-Preussen 3', 'Königreich England 3', 'Königreich Schweden 4', 'Habsburger Monarchie 3', 'Zarentum Russland 3'],
                 7:['Königreich Brandenburg-Preussen 4', 'Königreich England 4', 'Königreich Schweden 5', 'Königreich Frankreich 3', 'Zarentum Russland 4'],
                 8:['Königreich Schweden 6', 'Königreich Frankreich 4', 'Habsburger Monarchie 4'],
                 9:['Königreich Brandenburg-Preussen 5', 'Königreich England 5', 'Königreich Frankreich 5', 'Habsburger Monarchie 5', 'Zarentum Russland 5'],
                 10:['Königreich Brandenburg-Preussen 6', 'Königreich Frankreich 6', 'Habsburger Monarchie 6'],
                 11:['Königreich England 6', 'Zarentum Russland 6']}
Inselteile = ['A', 'B', 'C', 'D', 'E', 'F']
Inselrando = ['Y', 'N']
Nation = ''

#Spielerzahl, Schwierigkeit und eventuell Größe der Insel abfrage und festlegen
print('Willkommen beim Spirit Island Randomizer!'.center(60, '*'))
Spielerzahl = int(input('Wie viele spielen mit? 1/6: '))
Schwzufall = input('Wollt ihr eine fixe Schwierigkeit, oder einen Bereich eingeben? z = Zufall, f = fix: ' )

if Schwzufall.lower() == 'z':
    SchwBereich1 = int(input('Bitte die untere Schwierigkeit wählen 1/11: '))
    SchwBereich2 = int(input('Bitte die obere Schwierigkeit wählen 1/11: '))
    Schwierigkeit = Nationenstufe[random.randint(SchwBereich1, SchwBereich2)]
    Nation = random.choice(Schwierigkeit)
elif Schwzufall.lower() == 'f':
    Schwierigkeit = Nationenstufe[int(input('Bitte wähle eine Schwierigkeit aus 1/11: '))]
    Nation = random.choice(Schwierigkeit)

if Spielerzahl < 6:
    Insel = input('Wollt ihr eine größere Insel? y/n/z: ').lower()
    if Insel == 'z':
        Insel = random.choice(Inselrando)

#Ausgabe der spielrelevanten Informationen

print(random.sample(Geister, k = Spielerzahl))

# Hier erfolgt die Generierung der Inselteile mit den Checks welche Spielplanteile nicht miteinander verwendet werden sollen.
while True:
    if Insel == 'n':
        Inselteileverwendet = random.sample(Inselteile, k = Spielerzahl)
        if Spielerzahl <= 4:
            if 'B' and 'E' in Inselteileverwendet:
                Inselteileverwendet = []
                continue
            elif 'F' and 'D' in Inselteileverwendet:
                Inselteileverwendet = []
                continue
            else:
                print(f'Inselteile: {Inselteileverwendet}')
                break
        else:
            print(f'Inselteile: {Inselteileverwendet}')
            break
    elif Insel == 'y':
        Inselteileverwendet = random.sample(Inselteile, k = (Spielerzahl + 1))
        if Spielerzahl <= 3:
            if 'B' and 'E' in Inselteileverwendet:
                Inselteileverwendet = []
                continue
            elif 'F' and 'D' in Inselteileverwendet:
                Inselteileverwendet = []
                continue
            else:
                print(f'Inselteile: {Inselteileverwendet}')
                break
        else:
            print(f'Inselteile: {Inselteileverwendet}')
            break


print(Nation)

print('Viel Spaß und viel Erfolg!'.center(60, '*'))
input('Enter drücken zum beenden')