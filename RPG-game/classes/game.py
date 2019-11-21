import random
from classes.inventory import Item
from classes.magic import Spell
import pprint

class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[94n'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0n'
    BOLD = '\033[1n'
    UNDERLINE = '\033[4n'


class Person:
    def __init__(self,hp,mp,df,atk,magic, items):
        self.maxhp = hp
        self.hp=hp
        self.maxmp = mp
        self.mp = mp
        self.atkl=atk-10
        self.atkh = atk+10
        self.df=df
        self.magic = magic
        self.items= items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self,dmg):
        self.hp = self.hp-dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp-=cost



    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i=1
        for item in self.magic:
            print(str(i)+ ". " + item.name)
            i += 1
        return False

    def choose_item(self):
        i=1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print(str(i)+ ". " + self.item.name)




