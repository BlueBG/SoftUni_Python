number_of_heroes = int(input())

hero_hp = {}
hero_mp = {}

for i in range(number_of_heroes):
    hero_name_and_stat = input().split()

    hero_name = hero_name_and_stat[0]
    hero_hit_points = hero_name_and_stat[1]
    hero_mana_points = hero_name_and_stat[2]

    hero_hp[hero_name] = int(hero_hit_points)
    hero_mp[hero_name] = int(hero_mana_points)

while True:
    command_arc = input()

    if command_arc == "End":
        break

    command_line = command_arc.split(" - ")

    command  = command_line[0]
    hero_name = command_line[1]

    if command == "CastSpell":
        mana_needed = int(command_line[2])
        spell_name = command_line[3]

        if hero_mp[hero_name] >= mana_needed:
            hero_mp[hero_name] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_mp[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(command_line[2])
        attacker = command_line[3]
        hero_hp[hero_name] -= damage

        if hero_hp[hero_name] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_hp[hero_name]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            hero_hp.pop(hero_name)
            hero_mp.pop(hero_name)

    elif command == "Recharge":
        mana_amaunt = int(command_line[2])
        hero_mp[hero_name] += mana_amaunt

        if hero_mp[hero_name] > 200:
            mp_amaunt = hero_mp[hero_name] - (mana_amaunt * 2)
            hero_mp[hero_name] = 200

            print(f"{hero_name} recharged for {mp_amaunt} MP!")
        else:
            print(f"{hero_name} recharged for {mana_amaunt} MP!")

    elif command == "Heal":
        hit_points = int(command_line[2])
        hero_hp[hero_name] += hit_points

        if hero_hp[hero_name] > 100:
            hp_amaunt = 100 - (hero_hp[hero_name] - hit_points)
            hero_hp[hero_name] = 100

            print(f"{hero_name} healed for {hp_amaunt} HP!")
        else:
            print(f"{hero_name} healed for {hit_points} HP!")


for hero in hero_hp.keys():
    hp = hero_hp[hero]
    mp = hero_mp[hero]
    print(hero)
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")


            # 73 POINT'S