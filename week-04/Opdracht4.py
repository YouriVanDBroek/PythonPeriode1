# Opdracht - Weapon Selector
#
# Je gaat een programma maken waarin een speler een wapen kan kiezen.
# Ieder wapen heeft zijn eigen damage en een speciale eigenschap.
#
# Stap 1 - Variabelen
# Maak de volgende variabelen aan:
# - Een variabele voor de naam van de speler
# - Een variabele voor het gekozen wapen
# - Een variabele voor de damage van het wapen
#
# Geef de speler zelf een naam en kies alvast een wapen.
#
# LET OP:
# Gebruik voor alle variabelen de juiste Python naming conventions!
# Bijvoorbeeld: player_name in plaats van playerName.
speler = "Steve" ##dit zijn variabelen die de naam van de speler, het wapen en de damage van het wapen opslaan. Deze variabelen worden later gebruikt in de match case om te bepalen welk wapen de speler heeft gekozen en hoeveel damage het wapen doet.
selected_weapon = "Sword"
weapon_damage = 20

# Stap 2 - Match Case
# Gebruik een match case om te controleren welk wapen de speler heeft.
#
# De speler kan kiezen uit de volgende wapens:
#
# Sword:
# - Doet 20 damage
# - Print "Je gebruikt een zwaard!"
#
# Bow:
# - Doet 15 damage
# - Print "Je gebruikt een boog!"
#
# Staff:
# - Doet 25 damage
# - Print "Je gebruikt een magische staf!"
#
# Axe:
# - Doet 30 damage
# - Print "Je gebruikt een bijl!"
#
# Zorg ervoor dat de damage variabele de juiste waarde krijgt.
#
# Als de speler een onbekend wapen heeft gekozen:
# - Zet de damage op 0
# - Print "Onbekend wapen!"
#
# TIP:
# Gebruik case _ voor een onbekende waarde.
match speler:   ##deze match case is voor de speler naam, niet voor het wapen en het gaat dus namen vergelijken met wat er in de variabele speler staat. Als de naam van de speler overeenkomt met een van de cases, wordt de bijbehorende code uitgevoerd.
    case "Steve":
        print ("Welkom, Steve!")
    case "Alex":
        print ("Welkom, Alex!")
    case _:
        print ("Welkom, speler!")


match selected_weapon:  ##deze match case is voor het wapen dat de speler heeft gekozen. Het vergelijkt de waarde van de variabele selected_weapon met de verschillende cases. Als er een match is, wordt de bijbehorende code uitgevoerd en wordt de damage variabele aangepast aan het gekozen wapen.
    case "Sword":
        print("Je gebruikt een zwaard! en doet 20 damage.")
        weapon_damage = 20
    case "Bow":
        print("Je gebruikt een boog! en doet 15 damage.")
        weapon_damage = 15
    case "Staff":
        print("Je gebruikt een magische staf! en doet 25 damage.")
        weapon_damage = 25
    case "Axe":
        print("Je gebruikt een bijl! en doet 30 damage.")
        weapon_damage = 30
    case "Dagger":
        print("Je gebruikt een dolk! en doet 10 damage.")
        weapon_damage = 10
    case "Scythe":
        print("Je gebruikt een zeis! en doet 35 damage.")
        weapon_damage = 35
    case _:
        print("Onbekend wapen! en doet geen damage volgens onze codex.")
        weapon_damage = 0

        match weapon_damage:
            case 0:
                print("Je hebt geen wapen gekozen, je doet geen damage.")
            case 20:
                print(f"Je hebt een zwaard gekozen, je doet {weapon_damage} damage.")
 # Stap 3 - Resultaat printen
 # Print na de match case de volgende informatie:
 #
 # Speler: Steve
 # Wapen: Sword
 # Damage: 20
 #
 # Zorg ervoor dat de informatie uit je variabelen komt.
print(f"Speler: {speler}")  ##hier print ik de variabelen speler, wapen en damage uit. De f-string zorgt ervoor dat de variabelen in de string worden geïnterpreteerd en hun waarden worden weergegeven.
print(f"Wapen: {selected_weapon}")
print(f"Damage: {weapon_damage}")

# Stap 4 - Comments
# Voeg minimaal 3 eigen comments toe aan je programma.
#
# Leg met deze comments uit:
# - Wat een bepaald stuk code doet
# - Waarom je een match case gebruikt
# - Wat er gebeurt als het wapen niet bestaat
#
# Schrijf duidelijke comments die iemand anders helpen
# om jouw code te begrijpen.
## ok gedaan

# Stap 5 - Naming Conventions
# Controleer of je code voldoet aan de Python naming conventions.
#
# - Gebruik snake_case voor variabelen
# - Gebruik duidelijke Engelse namen
# - Begin variabelen met een kleine letter
# - Gebruik geen spaties in variabelenamen
#
# FOUT: playerDamage = 20
# GOED: player_damage = 20
#
# FOUT: x = "Sword"
# GOED: selected_weapon = "Sword"


# BONUS 1
# Voeg zelf minimaal 2 nieuwe wapens toe aan je match case.
# Bedenk voor ieder wapen een eigen damage en beschrijving.


# BONUS 2
# Maak een variabele enemy_health met de waarde 100.
# Laat de speler 3 keer aanvallen met zijn gekozen wapen.
#
# Gebruik hiervoor een for-loop.
#
# Print na iedere aanval hoeveel health de vijand nog heeft.
# Zorg ervoor dat de health niet onder de 0 komt.
enemy_health = 100
for i in range(3):
    enemy_health -= weapon_damage

if enemy_health > 0:
        print(f"De vijand heeft nog {enemy_health} health over.")
else:
        print("De vijand heeft geen health meer over.")
enemy_health = 0

# BONUS 3
# Gebruik een while-loop om de vijand aan te vallen
# totdat de vijand geen health meer heeft.
#
# Print daarna "Vijand verslagen!"
print("de volgende bonus opdracht:")
enemy_health2 = 200
while enemy_health2 > 0:
    enemy_health2 -= weapon_damage
    print(f"De vijand heeft nog {enemy_health2} health over.")
print("Vijand verslagen!")
