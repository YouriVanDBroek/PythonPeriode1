# Oefening 1
# Print de volgende zin "Hello World"

print()


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = ""
leeftijd = 0
woonstad = ""

# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")
naam = "jens"
leeftijd = 16
woonstad = "Maarssen"
print(f"Mijn naam is {naam} ik ben {leeftijd} jaar oud en woon in {woonstad}")

print("\n\n")

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"
favoriete_game = "sea of thieves"
print(f"Mijn favoriete game is {favoriete_game}")

print("\n\n")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 1
number2 = 4
print(number1 + number2)
print(number1 * number2)
print(number2 - number2)
print(number2 / number1)

print("\n\n")

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit
character_name = "Bob"
character_health = 100
level = 1

damage = 20

print(character_name)
print(character_health)
print(level)


print(100 - damage)


print("\n\n")


# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 
weapon = "Sword"
damage = 40
new_level = level + 1

print(f"Character name: {character_name}, Health: {character_health}, Level: {new_level}, Damage: {damage}, Weapon: {weapon}")
print("\n\n")



# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

hours_played = 150
score = 1000
new_score = score + 250

print("Gamer Profile: \n")
print(f"Name: {character_name} \nAge: {leeftijd} \nFavourite Game: {favoriete_game} \nHours Played: {hours_played} \nLevel: {new_level} \nScore: {score}")


print(f"New Score: {new_score}")