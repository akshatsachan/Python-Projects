from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Creating black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 20, 100, "black")
blizzard = Spell("Blizzard", 30, 300, "black")
meteor = Spell("Meteor", 50, 500, "black")
quake = Spell("Quake", 60, 700, "black")

#Creating white magic
cure = Spell("Cure", 30, 120, "white")
cura = Spell("Cura", 50, 220, "white")

#Create some items
potion = Item("Potion","potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixir", "elixir", "Fully restores HP/MP of one party memeber", 9999)
hielixer = Item("Mega-Elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#Instantiate People
pla = Person(1200, 2300000, 123, 34, [fire, thunder, blizzard, meteor, cure, cura], [potion, hipotion, superpotion, elixer, hielixer, grenade])
enemy = Person(700, 9700000, 12, 23, [], [])

running = True
i=0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("*********")
    pla.choose_action()
    choice = input("Choose action!")
    index = int(choice)-1

    #print("You chose",pla.get_spell_name(int(index)))
    if index ==0:
        dmg=pla.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked",dmg,"Points of damage",enemy.get_hp(),"is enemy's health")
    elif index ==1:
        pla.choose_magic()
        magic_choice=int(input("Choose magic"))-1
        if magic_choice == -1:
            continue
        spell = pla.magic[magic_choice]
        dmg=spell.generate_damage()



        current_mp=pla.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        pla.reduce_mp(spell.cost)

        if spell.type == "white":
            pla.heal(dmg)
            print(bcolors.OKBLUE + spell.name + " type heals for " + str(dmg)+ "points")

        elif spell.type == "black":
            enemy.take_damage(dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals",str(dmg), "points of damage" + bcolors.ENDC)

    elif index==2:
        pla.choose_item()
        item_choice = int(input("Choose Item!"))-1
        if item_choice == -1:
            continue
        item = pla.items[item_choice]
        if item.type == "potion":
            pla.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixir":
            pla.mp=pla.maxmp
            pla.hp=pla.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully heals for HP/MP" + bcolors.ENDC)
        elif item.type == "attack":

        #running = False

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()

    pla.take_damage(enemy_dmg)
    print("Enemy attacks", enemy_dmg, "remaining hp", pla.get_hp())

    print("*********")
    print(bcolors.FAIL + "Enemy HP:" + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
    print(bcolors.FAIL + "Your HP:" + str(pla.get_hp()) + "/" + str(pla.get_maxhp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif pla.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False





