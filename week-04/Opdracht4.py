monster_health = 150
player_damage = 25
aanvallen = 0

while monster_health > 0:
    monster_health -= player_damage
    aanvallen += 1

    if monster_health < 0:
        monster_health = 0

    print("Monster heeft nog", monster_health, "health")

print("Monster verslagen!")
print("Aantal aanvallen:", aanvallen)