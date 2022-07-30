import time
import random


class Enemy():
    def __init__(self, name=str, att=int, health=int, money=int):
        self.name = name
        self.att = att
        self.health = health
        self.money = money


class Player(Enemy):
    def __init__(self, name=str, att=int, health=int, money=int, pot=int, skill=int, max_health=int, level=int):
        super().__init__(name, att, health, money)
        self.pot = pot
        self.skill = skill
        self.max_health = max_health
        self.level = level

    def __str__(self) -> str:
        return f"{self.name} - Lvl:{self.level} - HP:{self.health} - Weapon damage:{self.att} \nGold : {self.money}gp - Potions : {self.pot} - Magic scrolls: {self.skill}"


goblin = Enemy("goblin", -2, 20, 10)
spider = Enemy("giant spider", -1, 25, 10)
hobgoblin = Enemy("hobgoblin", 0, 30, 20)
bugbear = Enemy("bugbear", 1, 30, 30)
bandit = Enemy("bandit", -1, 30, 30)
bandit_leader = Enemy("bandit leader", 2, 25, 50)

dragon = Enemy("dragon", 3, 60, 50)
locations = [["You enter a Cavern. It's damp and dark walls and floors look travelled.", "You find yourself in a dark room, next to a river that runs through cave.", "From the ceiling, you see a dark shadow emerge. A spider!", spider, 30, "You see a pool of water and a stone bridge.", "You see a tall figure aproaching. A Hobgoblin!", hobgoblin, "You see the sunlight in front. You move towards it. You emerge from the cave and to the path!", "Cavern"],
             ["While traveling the woods, the jungle gets thicker and thicker.", "Suddenly, you get to a clearing among the trees.", "From the bushes a shadow quickly jumps towards you. A goblin!", goblin, 30, "You come across some ruins of an old castle. You head inside.",
              "While inspecting the dilapidated castle you quickly realize a Bugbear made this place it's nest, it swipes at you with a flash!", bugbear, "You make your way out of the thick jungle and to the well traveled road...", "Jungle"],
             ["You see a camp fire at the distance. You decide to slowly aproach.", "Next to the campfire you only see a tent and one man sitting, and a chest.", "'crack!' the man suddenly gets up as he hears you step on a branch. After seeing you, unsheaths his axe and runs toward you!",
              bandit, 50, "Hearing the noise another man emergers from the tent, holding a greathammer!", "Man yells 'I will end you!!' as he starts to swing around his hammer.", bandit_leader, "You emerge victoriously from the bandit camp!", "Camp"]
             ]


def shop(player):
    inventory = {"greatsword": 25, "avenger": 50,
                 "potion": 15, "scroll": 20}
    print("\nWelcome to the shop!")
    time.sleep(1)
    while True:
        print(player)
        time.sleep(2)
        for i, j in inventory.items():
            print(f"{i} ({j}gps)  -  ", end="")
        a = input("\nChoose item(e for exit):").lower()
        if a == "e":
            break
        if a not in inventory.keys():
            print("No such item!")
            continue
        price = inventory.get(a)
        if price > player.money:
            print("Not enough gold!")
            time.sleep(1)
            continue
        else:
            print(f"You have purchased {a}")
            time.sleep(1)
            if a == "greatsword":
                player.money -= 25
                player.att = 5
            elif a == "avenger":
                player.money -= 50
                player.att = 8
            elif a == "potion":
                player.money -= 15
                player.pot += 1
            elif a == "scroll":
                player.money -= 20
                player.skill += 1
            else:
                print("\nWrong prompt!")


def heal(player):
    player.pot -= 1
    player.health += 25
    if player.health > player.max_health:
        player.health = player.max_health





def tavern(player):
    print("Would you like a room for the night? (heals 25 hp)")
    time.sleep(1)
    d = input("Room(15gp) - leave: ").lower()
    if d == "room":
        print("You decided to stay the night...")
        time.sleep(2)
        player.money -= 15
        heal(player)
        player.pot += 1


def village(player, shopf):
    print("Welcome to the village....")
    time.sleep(2)
    while True:
        print(player)
        time.sleep(1)
        c = input("Tavern  -  Shop  -  Outside : ").lower()
        time.sleep(1)
        if c == "tavern":
            tavern(player)

        elif c == "shop":
            shopf(player)

        elif c == "outside":
            break

        else:
            print("\nWrong prompt!")


def attack(attr):
    dice = list(range(1, 13))
    d12 = random.choice(dice) + attr
    if d12 > 0:
        return d12
    return 0


def combat(player, enemy):
    time.sleep(1)
    print("\nCombat initiated!\n")
    time.sleep(2)
    while True:
        print(
            f"{player.name} HP:{player.health}        {enemy.name} HP : {enemy.health}\n")
        time.sleep(2)
        print(f"{enemy.name} will attack!\n")
        time.sleep(2)
        z = attack(enemy.att)
        player.health -= z
        print(f"{enemy.name} has dealt {z} damage!\n")
        time.sleep(1)
        if player.health <= 0:
            print("You Died!!!")
            time.sleep(3)
            break
        print(
            f"{player.name} HP:{player.health}        {enemy.name} HP : {enemy.health}\n")
        time.sleep(1)
        x = input(
            f"Choose action \nATTACK - HEAL({player.pot}): ").lower()
        time.sleep(2)
        if x == "heal":
            if player.pot > 0:
                print("Used healing potion!\n")
                heal(player)
                time.sleep(2)
            else:
                print("No potion left!\n")
                time.sleep(2)
        elif x == "attack":
            a = input(
                f"Weapon(+{player.att})  - Fireball(+25)({player.skill} left): ").lower()
            if a == "weapon":
                y = attack(player.att)
                print(f"You've dealt {y} damage!\n")
                enemy.health -= y
                time.sleep(2)
                if enemy.health <= 0:
                    print("Enemy felled!\n")
                    time.sleep(1)
                    print(f"You gained {enemy.money} gold.\n")
                    time.sleep(1)
                    player.money += enemy.money
                    break

            elif a == "fireball":
                if player.skill <= 0:
                    print("You don't have a scroll!!")
                else:
                    y = attack(25)
                    print(f"Fireball!!! you've dealt {y} damage!\n")
                    player.skill -= 1
                    enemy.health -= y
                    time.sleep(2)
                    if enemy.health <= 0:
                        print("Enemy felled!\n")
                        time.sleep(1)
                        print(f"You gained {enemy.money} gold.\n")
                        time.sleep(1)
                        player.money += enemy.money
                        break
            else:
                print("wrong prompt!")

        else:
            print("wrong prompt!")


def game(l, player):
    loc = locations[l]
    print(loc[0])
    time.sleep(3)
    print(loc[1])
    time.sleep(3)
    print(loc[2])
    time.sleep(3)
    combat(player, loc[3])
    if player.health < 0:
        exit()
    time.sleep(3)
    print(f"you found a chest and gained {loc[4]} gold!\n")
    time.sleep(3)
    print(loc[5])
    time.sleep(3)
    print(loc[6])
    time.sleep(3)
    combat(player, loc[7])
    if player.health < 0:
        exit()
    time.sleep(3)
    print(loc[8])
    time.sleep(3)


def gameplay():
    name = input("Enter your name warrior and start your journey... ")
    player1 = Player(name, 3, 50, 40, 2, 1, 50, 1)
    time.sleep(2)
    print(player1.__str__())
    time.sleep(2)
    z = input("left  or  right : ")
    a = random.sample(range(len(locations)), k=2)
    time.sleep(2)
    game(a[0], player1)
    if player1.health <= 0:
        exit()
    time.sleep(1)
    print("Leveled up!!!   Max health raised to 60!")
    player1.max_health = 60
    player1.level += 1
    time.sleep(1)
    village(player1, shop)
    time.sleep(2)
    print("On the road again...")
    time.sleep(2)
    z = input("left  or  right : ")
    time.sleep(1)
    game(a[1], player1)
    if player1.health <= 0:
        exit()
    time.sleep(2)
    print("Leveled up!!!   Max health raised to 70!")
    player1.max_health = 70
    player1.level += 1
    time.sleep(2)
    village(player1, shop)
    time.sleep(3)
    print("\nYou warrior, are ready for the dragon...")
    combat(player1, dragon)
    if player1.health <= 0:
        exit()
    elif dragon.health <= 0:
        print("Congratulations!!! You've vanquished the dragon!!")
        print("You have earned the dragons horde!   200gp!\n")
        player1.money += 200


if __name__ == "__main__":
    gameplay()
