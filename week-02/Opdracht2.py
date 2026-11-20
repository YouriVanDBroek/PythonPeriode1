# Opdracht 1 - Leeftijd controleren
#
# Maak een variabele genaamd age.
# Geef deze variabele een leeftijd.
leeftijd = 17


# Controleer met een if-statement:
# - Is de leeftijd 18 of hoger?
#   Print dan: "Je bent volwassen."
#
# - Anders:
#   Print dan: "Je bent nog geen 18."
#
# Test je programma daarna met verschillende waardes voor age.
if leeftijd >=18:
    print("Je bent volwassen.")
else:
    print("Je bent nog geen 18.")

# Opdracht 2 - Voldoende of onvoldoende
#
# Maak een variabele genaamd grade.
# Geef deze variabele een cijfer.
#
# Controleer met een if-statement:
#
# - Is het cijfer 5.5 of hoger?
#   Print: "Je hebt een voldoende!"
#
# - Anders:
#   Print: "Je hebt een onvoldoende."
#
# Test je programma met verschillende cijfers.
grade = 6.5
if grade >= 5.5:
    print("Je hebt een voldoende!")
else:
    print("Je hebt een onvoldoende.")

# Opdracht 3 - Cijfer beoordelen
#
# Maak een variabele genaamd grade.
#
# Controleer het cijfer met if, elif en else.
#
# - 8 of hoger:
#   Print "Goed gedaan!"
#
# - 5.5 of hoger:
#   Print "Voldoende!"
#
# - Lager dan 5.5:
#   Print "Onvoldoende."
#
# Test je code met bijvoorbeeld:
# 4
# 6
# 9
grade = 4
if grade >= 8:
    print("Goed gedaan!")
elif grade >= 5.5:
    print("Voldoende!")
else:
    print("Onvoldoende.")


# Opdracht 4 - Game Character
#
# Maak de volgende variabelen:
#
# health = 75
# has_shield = True
#
# Controleer de health van de speler.
#
# - Heeft de speler 50 health of meer?
#   Print "Je hebt genoeg health."
#
# - Heeft de speler minder dan 50 health?
#   Print "Je hebt weinig health!"
#
# Controleer daarna of has_shield True is.
#
# Als dit zo is:
# Print "Je hebt een schild!"
health = 75
has_shield = True

if health >= 50:
    print("Je hebt genoeg health.")
else:
    print("Je hebt weinig health!")

if has_shield:
    print("Je hebt een schild!")


# Opdracht 5 - Mag je naar binnen?
#
# Maak twee variabelen:
#
# age = 20
# has_ticket = True
#
# De speler mag alleen naar binnen als:
# - De speler 18 jaar of ouder is
# EN
# - De speler een ticket heeft.
#
# Gebruik hiervoor een if-statement met 'and'.
#
# Als aan beide voorwaarden wordt voldaan:
# Print "Je mag naar binnen!"
#
# Anders:
# Print "Je mag niet naar binnen."
#
# Test daarna wat er gebeurt als je de waardes verandert.
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Je mag naar binnen!")
else:
    print("Je mag niet naar binnen.")


# Opdracht 6 - Tellen
#
# Maak een for-loop die de getallen
# 1 tot en met 10 print.
#
# De output moet zijn:
#
# 1
# 2
# 3
# ...
# 10
#
# Gebruik hiervoor range().
for i in range (1, 11):
    print(i)


# Opdracht 7 - Tafel van 5
#
# Maak een for-loop die de tafel van 5 print.
#
# De output moet ongeveer zijn:
#
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 10 x 5 = 50
#
# Gebruik de variabele uit je for-loop
# om de berekening te maken.
for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")

# Opdracht 8 - Countdown
#
# Maak een variabele:
#
# countdown = 10
#
# Maak een while-loop die blijft werken
# zolang countdown groter is dan 0.
#
# Print iedere keer de waarde van countdown.
# Verlaag countdown daarna met 1.
#
# Als de loop klaar is:
# Print "GO!"
#
# De output moet zijn:
#
# 10
# 9
# 8
# ...
# 2
# 1
# GO!
import time
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
print("GO!")

# Opdracht 9 - Health verliezen
#
# Maak een variabele:
#
# health = 100
#
# Maak een loop die 5 keer wordt uitgevoerd.
#
# Iedere keer dat de loop wordt uitgevoerd:
# - Verliest de speler 20 health.
# - Print je hoeveel health de speler nog heeft.
#
# De output wordt bijvoorbeeld:
#
# Health: 80
# Health: 60
# Health: 40
# Health: 20
# Health: 0
loop_count = 5
health = 100
while loop_count > 0:
    health -= 20
    print(f"Health: {health}")
    loop_count -= 1


# Opdracht 10 - Even of oneven
#
# Maak een loop die door de getallen
# 1 tot en met 10 gaat.
#
# Controleer bij ieder getal:
# Is het getal even of oneven?
#
# Print bijvoorbeeld:
#
# 1 is oneven
# 2 is even
# 3 is oneven
# 4 is even
#
# TIP:
# Gebruik % om te controleren of een getal
# deelbaar is door 2.
#
# Bijvoorbeeld:
# 4 % 2 == 0

# % kijkt hoevaak 2 in 1, 2, 3 etc past. Als er niks overblijft is het even, als er 1 of -0.5 overblijft is het oneven.
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is oneven")
    
# Opdracht 11 - Vijanden verslaan - BONUS
#
# De speler moet 5 vijanden verslaan.
#
# Maak een for-loop die 5 keer wordt uitgevoerd.
#
# Maak binnen de loop een variabele:
#
# enemy_health = 30
#
# De speler doet iedere aanval 10 damage.
#
# Gebruik een while-loop om de vijand aan te vallen
# totdat enemy_health 0 is.
#
# Print na iedere aanval hoeveel health
# de vijand nog heeft.
#
# Als de vijand 0 health heeft:
# Print "Vijand verslagen!"
#
# Daarna begint de volgende vijand.

for i in range(5):
    enemy_health = 30
    while enemy_health > 0:
        enemy_health -= 10
        if enemy_health > 0:
            print(f"Vijand heeft nog {enemy_health} health.")
        else:
            print("Vijand verslagen!")

# Eindopdracht - Player Training - BONUS
#
# Maak een speler met de volgende variabelen:
#
# player_name = "Steve"
# level = 1
# experience = 0
#
# De speler gaat 10 keer trainen.
#
# Maak hiervoor een loop.
#
# Iedere training krijgt de speler 20 experience.
#
# Print na iedere training:
# "Steve heeft nu 20 experience."
#
# "Steve heeft nu 40 experience."
#
# enzovoort.
#
# Iedere keer dat de speler 100 experience bereikt:
# - Gaat het level met 1 omhoog.
# - Print je "LEVEL UP!"
# - Zet je experience weer op 0.
#
# Print aan het einde:
#
# "Training voltooid!"
# "Level: ..."
# "Experience: ..."
#
#
# BONUS:
# Voeg health en damage toe aan je speler.
# Iedere keer dat de speler een level omhoog gaat,
# krijgt hij 5 extra damage.


player_name = "Steve"
level = 1
experience = 0
damage = 10

for i in range(10):
    experience += 20
    print(f"{player_name} heeft nu {experience} experience.")
    
    if experience >= 100:
        level += 1
        experience = 0
        damage += 5
        print("LEVEL UP!")

print(f"Training voltooid!")
print(f"Level: {level}")
print(f"Experience: {experience}")
print(f"Damage: {damage}")