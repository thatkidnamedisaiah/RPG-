import random
import time
from random import choice

inventory = []

directions = ["n", "s", "e", "w", "l"]

Monster_Is_Attacking = False

def print_Slow(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.045)
    print()

def addItem(item):
    inventory.append(item)

def move(user_Direction_Choice):
        
    if(user_Direction_Choice == "n"):
        print_Slow("Moving North...")
    elif (user_Direction_Choice == "s"):
        print_Slow("Moving South...")          
    elif (user_Direction_Choice == "e"):
        print_Slow("Moving East")
    elif (user_Direction_Choice == "w"):
        print_Slow("Moving West...") 
    elif (user_Direction_Choice == "l"):
        lookAround()
    else:
        return True

    Attack_Chance = random.randint(0, 9)
    print("Attack Chance: ", Attack_Chance)

    if Attack_Chance == 0:
        return False
    else:
        return True

def lookAround():
    items =  [" a pile of 5 copper coins",
              " a pile of 7 copper coins",
              " a pile of 15 copper coins",
              " a pile of 4 silver coins",
              " a pile of 6 silver coins",
              " a pile of 13 silver coins",
              " a pile of 2 gold coins",
              " a pile of 5 gold coins",
              " a pile of 11 gold coins",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",
              " nothing",]
    item_Found = choice(items)
    sentence = ("You found", item_Found)
    print_Slow(sentence)
    if item_Found == "nothing":
        return keepMoving
    else:
        do_You_Want_This = input("Do you want to keep this item?(y/n)")
        if (do_You_Want_This == "y"):
            addItem(item_Found)
            sentence = ("Item added. Your inventory has ", inventory)
            print_Slow(sentence)
        elif (do_You_Want_This == "n"):
            return keepMoving

        

keepMoving = True
while (keepMoving):
  user_Direction_Choice = input("Choose a Direction (North, South, East, West or Look Around)")
  if(user_Direction_Choice == "l"):
    lookAround()
  else:
    keepMoving = move(user_Direction_Choice)
    
Monster_Is_Attacking = True
while Monster_Is_Attacking:
    player_Health = 100
    monster_Health = 120
    sentence = "Current Player Health: ", player_Health
    print_Slow(sentence)

    monster = "Dragon"
    sentence = ("A ", monster, " decides to attack!")
    print_Slow(sentence)
 
    monster_Attack_Choices = ["Fire Breath ",
                              "Tail Swing ",
                              "Dragon Roar ",
                              "Wing Flap ",
                              "Bite "]
    monsters_Attack = random.choice(monster_Attack_Choices)
   
    print_Slow("")
    monster_Attack_Damage = random.randint(15, 35)
    sentence = ("The ", monster, " chooses ", monsters_Attack, "and does ", monster_Attack_Damage, " damage to Player...")
    print_Slow(sentence)
    print_Slow("")

    player_Health -= monster_Attack_Damage
    if player_Health <= 0:
        player_Health = 0
        sentence = ("Current Player Health: ", player_Health)
        print_Slow(sentence)
        sentence = ("Current ", monster, " Health:", monster_Health)
        print_Slow(sentence)
        print_Slow("")
        print_Slow("You Died...   GAME OVER")
        Monster_Is_Attacking = False

    sentence = ("Current Player Health: ", player_Health)
    print_Slow(sentence)
    sentence = ("Current ", monster, " Health:", monster_Health)
    print_Slow(sentence)
    print_Slow("")

    player_Attack_Damage = random.randint(45, 60)

    player_Attack_Choices = ["Lightning Strike",
                            "Acid Splash",
                            "Posion Spray",
                            "Earthquake",
                            "Cloud of Frost"]
    
    print_Slow("Choose a spell to attack!")
    print_Slow("")
    print_Slow("""You have

    (q) Lightning Skrike
    (w) Acid Splash
    (e) Posion Spray
    (r) Earthquake
    (t) Cloud of Frost

Type the letter next to the spell you wish to use """)
    
    players_Attack = (input(">> "))
    if players_Attack == "q":
        sentence = ("Player uses ", player_Attack_Choices[0], " and does ", player_Attack_Damage, " damage to ", monster, "!")
        print_Slow(sentence)
        monster_Health -= player_Attack_Damage
    elif players_Attack == "w":
        sentence = ("Player uses ", player_Attack_Choices[1], " and does ", player_Attack_Damage, " damage to ", monster, "!")
        print_Slow(sentence)
        monster_Health -= player_Attack_Damage
    elif players_Attack == "e":
        sentence = ("Player uses ", player_Attack_Choices[2], " and does ", player_Attack_Damage, " damage to ", monster, "!")
        print_Slow(sentence)
        monster_Health -= player_Attack_Damage
    elif players_Attack == "r":
        sentence = ("Player uses ", player_Attack_Choices[3], " and does ", player_Attack_Damage, " damage to ", monster, "!")
        print_Slow(sentence)
        monster_Health -= player_Attack_Damage
    elif players_Attack == "t":
        sentence = ("Player uses ", player_Attack_Choices[4], " and does ", player_Attack_Damage, " damage to ", monster, "!")
        print_Slow(sentence)
        monster_Health -= player_Attack_Damage
    else:
        sentence = ("That spell is not availible yet! You have wasted time and the", monster, " grows STRONGER!")
        print_Slow(sentence)
        monster_Health += 5
        

    if monster_Health <= 0:
        monster_Health = 0
        print_Slow("")
        sentence = ("Current Player Health: ", player_Health)
        print_Slow(sentence)
        sentence = ("Current ", monster, " Health: ", monster_Health)
        print_Slow(sentence)
        print_Slow("")
        sentence = ("The ", monster, " died...   YOU WIN!")
        print_Slow(sentence)
        Monster_Is_Attacking = False

