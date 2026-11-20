import time



# Oefening 1
# Maak een list aan genaamd books met minimaal 5 boeken
# Gebruik daarna een for-loop om ieder boek 1 voor 1 uit te printen

books = ["book1", "book2"]
for i in books:
    print(i)

time.sleep(1)

# Oefening 2
# Maak een list aan genaamd games met minimaal 5 games
# Gebruik een for-loop om door de list heen te gaan
# Print bij iedere game de zin: "Ik speel graag ..."
# Bijvoorbeeld: "Ik speel graag Minecraft"

games = ["Minecraft", "Fortnite", "Call of Duty", "Overwatch", "League of Legends"]
for game in games:
    print("Ik speel graag " + game)




time.sleep(1)
# Oefening 3
# Maak een list aan genaamd scores met de volgende waardes:
# 10, 25, 40, 15, 30
# Gebruik een for-loop om iedere score uit te printen
# Tel bij iedere score 10 punten op en print daarna de nieuwe score uit

scores = [10, 25, 40, 15, 30]
for score in scores:
    new_score = score + 10
    print(new_score)


time.sleep(1)
# Oefening 4
# Gebruik een for-loop met range() om de getallen 1 tot en met 10 uit te printen
# Zorg ervoor dat zowel 1 als 10 geprint worden
for i in range(1, 11):
    print(i)




time.sleep(1)
# Oefening 5
# Gebruik een for-loop met range() om de tafel van 5 uit te printen
# Bijvoorbeeld:
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# Ga door tot en met 10 x 5
for i in range(1, 11):
    result = i * 5
    print(f"{i} x 5 = {result}")




time.sleep(1)
# Oefening 6
# Maak een variabel countdown aan met de waarde 10
# Gebruik een while-loop om af te tellen van 10 naar 1
# Verlaag countdown iedere keer met 1
# Print na de loop "START!"

countdown = 10
for i in range(1, 10):
    countdown -= 1
    print(countdown)
print("START!")

time.sleep(1)


# Oefening 7
# Maak de volgende variabelen aan:
# monsterHealth = 100
# damage = 20
# Gebruik een while-loop om damage van monsterHealth af te halen
# Blijf dit doen zolang monsterHealth groter is dan 0
# Print na iedere aanval hoeveel health het monster nog heeft
# Print daarna "Monster verslagen!"

monsterHealth = 100
damage = 20

while monsterHealth > 0:
    monsterHealth -= damage
    print(f"Monster health: {monsterHealth}")
print("Monster verslagen!")


time.sleep(1)
# Oefening 8
# Maak een list aan genaamd inventory met de volgende items:
# Sword, Potion, Shield, Bow, Key
# Gebruik een for-loop om ieder item uit de inventory uit te printen
# Gebruik daarna binnen de loop een if-statement
# Als het item "Potion" is, print dan "Deze potion geeft health terug"
# Als het item "Key" is, print dan "Met deze key kun je een deur openen"
# Bonus! Maak een variabel itemCount aan en tel hoeveel items er in de inventory zitten

inventory = ["Sword", "Potion", "Shield", "Bow", "Key"]
itemCount = 0

for item in inventory:
    print(item)
    itemCount += 1
    if item == "Potion":
        print("Deze potion geeft health terug")
    elif item == "Key":
        print("Met deze key kun je een deur openen")

print(f"Aantal items in inventory: {itemCount}")