

# Oefening 1
# Maak een list aan genaamd books met minimaal 5 boeken
# Gebruik daarna een for-loop om ieder boek 1 voor 1 uit te printen

books = ["book1", "book2", "book3", "book4", "book5"]
for i in books:
    print(i)



# Oefening 2
# Maak een list aan genaamd games met minimaal 5 games
# Gebruik een for-loop om door de list heen te gaan
# Print bij iedere game de zin: "Ik speel graag ..."
# Bijvoorbeeld: "Ik speel graag Minecraft"
games = ["Minecraft", "Fortnite", "Among Us", "Valorant", "GTA V"]
for i in games:
    print("ik speel graag " + i)




# Oefening 3
# Maak een list aan genaamd scores met de volgende waardes:
# 10, 25, 40, 15, 30
# Gebruik een for-loop om iedere score uit te printen
# Tel bij iedere score 10 punten op en print daarna de nieuwe score uit
scores = [10, 25, 40, 15, 30]
for i in scores:
    print(i + 10)




# Oefening 4
# Gebruik een for-loop met range() om de getallen 1 tot en met 10 uit te printen
# Zorg ervoor dat zowel 1 als 10 geprint worden
for i in range(1, 11):
    print(i)




# Oefening 5
# Gebruik een for-loop met range() om de tafel van 5 uit te printen
# Bijvoorbeeld:
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# Ga door tot en met 10 x 5
for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")




# Oefening 6
# Maak een variabel countdown aan met de waarde 10
# Gebruik een while-loop om af te tellen van 10 naar 1
# Verlaag countdown iedere keer met 1
# Print na de loop "START!"

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    
print("START!")





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
    print (f"monster Health is nu {monsterHealth}")

print("Monster verslagen!")

# Oefening 8
# Maak een list aan genaamd inventory met de volgende items:
# Sword, Potion, Shield, Bow, Key
# Gebruik een for-loop om ieder item uit de inventory uit te printen
# Gebruik daarna binnen de loop een if-statement
# Als het item "Potion" is, print dan "Deze potion geeft health terug"
# Als het item "Key" is, print dan "Met deze key kun je een deur openen"
# Bonus! Maak een variabel itemCount aan en tel hoeveel items er in de inventory zitten
inventory = ["sword", "potion","shield","bow", "key"]
itemcount = 0
for i in inventory:
    print (i)
    if i == "potion":
        print("Deze potion geeft health terug")
    elif i == "key":
        print("Met deze key kun je een deur openen")
    itemcount += 1
print(itemcount)