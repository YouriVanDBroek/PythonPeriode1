# Oefening 1
# Print de volgende zin "Hello World"

print("Hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Geovana"
leeftijd = 21
woonstad = "Utrecht"

print(naam)
print(leeftijd)
print(woonstad)


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print(f"Mijn naam is {naam}")
print(f"Ik ben {leeftijd} jaar oud")
print(f"Ik woon in {woonstad}")

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

game = "Stardew Valley"
uur = 921
cijfer = 10

print(f"Mijn favoriete game is {game}")
print(f"Ik heb deze game {uur}uur gespeeld")
print(f"Ik geef deze game een {cijfer}")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

number1 = 3
number2 = 2

som = number1 + number2
verschil = number1 - number2
product = number1 * number2

print(f"{number1} + {number2} = {som}")
print(f"{number1} - {number2} = {verschil}")
print(f"{number1} * {number2} = {product}")

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name = "Saki"
health = 100
level = 10
damage = 20

print(f"Character name: {name}")
print(f"Health: {health}")
print(f"Level: {level}")
health = health - damage
print(f"Damage: {damage}")
print(f"Nieuwe Health: {health}")

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weapon = "Mace"
damage = damage + 1
level = level + 1

print(weapon)
print(f"Damage: {damage}")
health = health - damage
print(f"Nieuwe Health: {health}")
print(f"Nieuwe Level: {level}")


# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

gamername = "Ravel"
age = 22
favouriteGame = "Elden Ring"
hoursPlayed = 602
level = 8
score = 42

print(f"Gamer Name: {gamername}")
print(f"Age: {age}")
print(f"Hours Played: {hoursPlayed}")
print(f"Level: 8")
print(f"Score: {score}")
score = score + 250
print(f"Nieuwe Score!: {score}")