import time
import random

firstattacktimes = 0
secondattacktimes = 0
firstblowup = False
secondblowup = False
firsthp = 0
secondhp = 0
firstpick = "n"
secondpick = "n"
firstarmour = False
secondarmour = False
firstmobhealth = 0
secondmobhealth = 0
firstmobattackdp = 0
secondmobattackdp = 0
firstmobspecialattackone = "none"
firstmobspecialattacktwo = "none"
secondmobspecialattackone = "none"
secondmobspecialattacktwo = "none"
firstmobspecialattackonedamage = 0
firstmobspecialattacktwodamage = 0
secondmobspecialattackonedamage = 0
secondmobspecialattacktwodamage = 0
firstitempick = "random"
seconditempick = "random"
firstsmart = "N"
secondsmart = "N"
firstphase = 0
secondphase = 0
fightmode = 1

print("Welcome to the minecraft mob battle game!")
time.sleep(1)

pick = input("do you want to pick the mobs that fight? (Y/N)")
if pick == "y" or pick == "Y":
  firstpick = input("what do you want the first mob to be?")
  time.sleep(1)
  secondpick = input("what do you want the second mob to be?")
elif pick == "Cc":
  firstpick = str(input("what do you want the first custom mob name to be?"))
  secondpick = str(input("what do you want the second custom mob name to be?"))
  firstmobhealth = int(input("how much health do you want the first custom mob to have?"))
  secondmobhealth = int(input("how much health do you want the second custom mob to have?"))
  firstmobattackdp = int(input("how much damage points do you want the first custom mob to deal when hitting?"))
  secondmobattackdp = int(input("how much damage points do you want the second custom mob to deal when hitting?"))
  print("special attacks: none, sonic boom, laser, fireball, fly, heal, poison, explosive wither skull, dragon breath, clone, summon spikes, dig, lightning, meteorite")
  firstmobspecialattackone = str(input("what do you want the first custom mob's  first special attack to be?"))
  firstmobspecialattacktwo = str(input("what do you want the first custom mob's  second special attack to be?"))
  secondmobspecialattackone = str(input("what do you want the second custom mob's  first special attack to be?"))
  secondmobspecialattacktwo = str(input("what do you want the second custom mob's  second special attack to be?"))
  firstmobspecialattackonedamage = int(input("how much damage points do you want the first custom mob to deal(or heal), when using the first special attack?"))
  firstmobspecialattacktwodamage = int(input("how much damage points do you want the first custom mob to deal(or heal), when using the second special attack?"))
  secondmobspecialattackonedamage = int(input("how much damage points do you want the second custom mob to deal(or heal), when using the first special attack?"))
  secondmobspecialattacktwodamage = int(input("how much damage points do you want the first custom mob to deal(or heal), when using the second special attack?"))
  firstsmart = str(input("do you want the first custom mob to be intellegent?(Y/N)"))
  secondsmart = str(input("do you want the second custom mob to be intellegent?(Y/N)"))
  firstitempick = str(input("what do you want the first custom mob to hold?(enter random to get a 'random' one)"))
  seconditempick = str(input("what do you want the second custom mob to hold?(enter random to get a 'random' one)"))

mobslist = ["player", "zombie", "skeleton", "stray", "creeper", "phantom", "spider", "husk", "drowned", "baby zombie", "wither skeleton", "enderman", "big slime", "medium slime", "pillager", "vindicator", "evolker", "ravenger", "bogged", "breeze", "creaking", "iron golem", "zombified piglin", "piglin", "baby zombified piglin", "baby piglin", "warden", "wither", "ender dragon", "illusioner", "cave spider", "bee", "goat", "witch", "vex", "hoglin", "zoglin", "zombified villager", "baby zombified villager", "blaze", "ghast", "big magma cube", "medium magma cube", "shulker", "snow golem", "piglin brute"]

itemslist = ["nothing", "apple", "wooden sword", "stone sword", "iron sword", "golden apple", "grass block"]

firstmob = mobslist[random.randrange(0, len(mobslist))]
secondmob = mobslist[random.randrange(0, len(mobslist))]
firstitem = itemslist[random.randrange(0, len(itemslist))]
seconditem = itemslist[random.randrange(0, len(itemslist))]

if not firstpick == "n":
  firstmob = firstpick
if not secondpick == "n":
  secondmob = secondpick
if not firstitempick == "random":
  firstitem = firstitempick
if not seconditempick == "random":
  seconditem = seconditempick
print("\nthis battle:", firstmob, "holding", firstitem, "against", secondmob, "holding", seconditem, "\n")

if fightmode == 1:
  for i in range(5):
    print(5 - i)
    time.sleep(1)

match firstmob:
  case "zombie" | "zombified villager" | "zombified piglin" | "husk" | "drowned" | "skeleton" | "stray" | "piglin" | "baby zombified villager" | "baby zombified piglin" | "baby piglin" | "bogged" | "bee" | "baby zombie":
    firsthp = 3
  case "witch" | "piglin brute" | "vindicator" | "evolker" | "wither skeleton" | "snow golem" | "ravenger":
    firsthp = 25
  case "big slime" | "big magma cube" | "player":
    firsthp = 21
  case "medium slime" | "medium magma cube" | "ghast":
    firsthp = 5
  case "wither":
    firsthp = 300
  case "warden":
    firsthp = 500
  case "ender dragon":
    firsthp = 200
  case "spider" | "cave spider" | "goat" | "creeper" | "hoglin" | "zoglin" | "phantom" | "vex" | "pig" | "cow" | "sheep":
    firsthp = 6
  case "enderman" | "iron golem" | "illusioner":
    firsthp = 35
  case "shulker" | "blaze" | "breeze":
    firsthp = 18
  case "creaking" | "wither storm":
    firsthp = 99999
  case firstpick:
    firsthp = firstmobhealth
match secondmob:
  case "zombie" | "zombified villager" | "zombified piglin" | "husk" | "drowned" | "skeleton" | "stray" | "piglin" | "baby zombified villager" | "baby zombified piglin" | "baby piglin" | "bogged" | "bee" | "baby zombie":
    secondhp = 3
  case "witch" | "piglin brute" | "vindicator" | "evolker" | "wither skeleton" | "snow golem" | "ravenger":
    secondhp = 25
  case "big slime" | "big magma cube" | "player":
    secondhp = 21
  case "medium slime" | "medium magma cube" | "ghast":
    secondhp = 5
  case "wither":
    secondhp = 300
  case "warden":
    secondhp = 500
  case "ender dragon":
    secondhp = 200
  case "spider" | "cave spider" | "goat" | "creeper" | "hoglin" | "zoglin" | "phantom" | "vex" | "pillager" | "pig" | "cow" | "sheep":
    secondhp = 6
  case "enderman" | "iron golem" | "illusioner":
    secondhp = 35
  case "shulker" | "blaze" | "breeze":
    secondhp = 18
  case "creaking" | "wither storm":
    secondhp = 99999
  case secondpick:
    secondhp = secondmobhealth

while True:
  if firstblowup == True:
    match secondmob:
      case "zombie" | "zombified villager" | "zombified piglin" | "husk" | "drowned" | "zoglin" | "baby zombified villager" | "baby zombified piglin":
        print(secondmob, "got exploded by", firstmob, ", dropping rotten flesh")
        print("\n", firstmob, "wins!")
      case "player" | "warden" | "wither" | "ender dragon" | "big magma cube" | "big slime" | "ghast" | "iron golem" | "shulker" | "blaze" | "enderman" | "illusioner":
        print(secondmob, "got hurt by", firstmob, "explosion")
        print("\n", secondmob, "wins!")
      case "creaking":
        print(secondmob, "survived", firstmob, "explosion")
        print("\n", secondmob, "wins!")
      case _:
        print(secondmob, "got exploded by", firstmob)
        print("\n", firstmob, "wins!")
    break
  if secondblowup == True:
    match firstmob:
      case "zombie" | "zombified villager" | "zombified piglin" | "husk" | "drowned" | "zoglin" | "baby zombified villager" | "baby zombified piglin":
        print(firstmob, "got exploded by", secondmob, ", dropping rotten flesh")
        print("\n", secondmob, "wins!")
      case "player" | "warden" | "wither" | "ender dragon" | "big magma cube" | "big slime" | "ghast" | "iron golem" | "shulker" | "blaze" | "enderman" | "illusioner":
        print(firstmob, "got hurt by", secondmob, "explosion")
        print("\n", firstmob, "wins!")
      case "creaking":
        print(firstmob, "survived", secondmob, "explosion")
        print("\n", firstmob, "wins!")
      case _:
        print(firstmob, "got exploded by", secondmob)
        print("\n", secondmob, "wins!")
    break
  if firsthp < 1:
    print(firstmob, "died")
    print("\n", secondmob, "wins!")
    break


  firstattack = random.randrange(0, 5)
  secondattack = random.randrange(0, 5)
  match firstmob:
    case "zombie" | "zombified villager" | "zombified piglin" | "husk":
      if firstattacktimes % 2 == 0:
        print(firstmob, "walks toward", secondmob)
      else:
        if "sword" in firstitem:
          print(firstmob, "hits", secondmob, "with", firstitem)
          secondhp = secondhp - 2
        else:
          print(firstmob, "hits", secondmob)
        secondhp = secondhp - 2
    case "skeleton" | "pillager" | "stray" | "bogged":
      if firstattack == 0:
        print(firstmob, "walks toward", secondmob)
      else:
        if firstattacktimes % 2 == 0:
          print(firstmob, "reloads")
        else:
          print(firstmob, "shoots arrows at", secondmob)
          secondhp = secondhp - 6
    case "creeper":
      if firstattack == 0:
        print(firstmob, "walks toward", secondmob)
      else:
        if firstattacktimes % 2 == 0:
          print(firstmob, "flashes")
        else:
          print(firstmob, "blows up")
          firstblowup = True
    case "creaking":
      firsthp = 99999
      if firstattacktimes % 2 == 0:
        print(firstmob, "hits", secondmob)
        secondhp = secondhp - 4
      elif firstattack == 0:
        print("creaking heart has been broken")
        print("\n", secondmob, "wins!")
        break
      else:
        print(firstmob, "walks toward", secondmob)
    case "wither":
      if firstattacktimes == 0:
        print("the wither has been summoned in")
        secondhp = secondhp - 2
      else:
        if firstattack == 0:
          print(firstmob, "flies toward", secondmob)
        elif firstattack == 1:
          print(firstmob, "shoots blue wither skull at", secondmob)
          secondhp = secondhp - 10
        else:
          print(firstmob, "shoots grey wither skull at", secondmob)
          secondhp = secondhp - 8
      if firsthp < 151:
        if firstarmour == False:
          print("wither has gained armour")
          firstarmour = True
    case "warden":
      if firstattacktimes == 0:
        print(firstmob, "shrieks at", secondmob)
      else:
        if firstattack == 0:
          print("warden digs")
          firsthp = firsthp + 4
          if fightmode == 1:
            time.sleep(1)
          print("warden reappears")
        if firstattack == 1:
          print("warden charges up sonic boom")
          if fightmode == 1:
            time.sleep(1)
          print("warden releases sonic boom")
          secondhp = secondhp - 8
        else:
          print(firstmob, "hits", secondmob)
          secondhp = secondhp - 18
    case "ender dragon":
      if firstattacktimes % 2 == 0:
        print("dragon flies")
        firsthp = firsthp + 1
      else:
        print("dragon lands")
      if firstattack == 0:
        print("dragon releases dragon breath")
        secondhp = secondhp - 8
      elif firstattack == 1:
        print("dragon heals at crystal")
        firsthp = firsthp + 6
      else:
        print("dragon shoots fireball at", secondmob)
        secondhp = secondhp - 8
    case "baby zombie" | "baby zombified villager" | "baby zombified piglin":
      if firstattacktimes % 2 == 0:
        print(firstmob, "runs toward", secondmob)
        firsthp = firsthp + 1
      else:
        if "sword" in firstitem:
          print(firstmob, "hits", secondmob, "with", firstitem)
          secondhp = secondhp - 2
        else:
          print(firstmob, "hits", secondmob)
        secondhp = secondhp - 1
    case "drowned":
      if firstattacktimes % 2 == 0:
        print(firstmob, "walks toward", secondmob)
      else:
        if firstattack == 0 or firstattack == 1:
          print(firstmob, "hits", secondmob)
          secondhp = secondhp - 2
        else:
          print(firstmob, "throws trident at", secondmob)
          secondhp = secondhp - 6
    case "illusioner":
      if firstattacktimes % 2 == 0:
        print(firstmob, "creates clones of itself")
        firsthp = firsthp + 5
      else:
        if firstattack == 0 or firstattack == 1:
          print(firstmob, "shoots arrows at", secondmob)
          secondhp = secondhp - 6
        else:
          print(firstmob, "flies")
          firsthp = firsthp + 1
    case "iron golem" | "wither skeleton":
      if firstattacktimes % 2 == 0:
        print(firstmob, "walks toward", secondmob)
      else:
        print(firstmob, "hits", secondmob)
        secondhp = secondhp - 7
    case "ravenger" | "hoglin" | "zoglin" | "vindicator":
      if firstattacktimes % 2 == 0:
        print(firstmob, "charges at", secondmob)
        secondhp = secondhp - 5
      elif firstmob == "ravenger":
        print("ravenger pushes", secondmob, "away")
        firsthp = firsthp + 4
      else:
        if firstattack == 0:
          print(firstmob, "dodges", secondmob)
          firsthp = firsthp + 2
        else:
          print(firstmob, "charges at", secondmob)
          secondhp = secondhp - 5
    case "phantom" | "vex":
      if firstattacktimes % 2 == 0:
        print(firstmob, "flies at", secondmob)
        secondhp = secondhp - 2
      else:
        print(firstmob, "flies up")
        firsthp = firsthp + 2
    case "enderman":
      if firstattacktimes % 2 == 0:
        if firstattack == 0:
          print("enderman teleported")
          firsthp = firsthp + 1
        else:
          print(firstmob, "hits", secondmob)
          secondhp = secondhp - 5
      else:
        if firstattack == 0:
          print("enderman teleported away")
          firsthp = 30
          if fightmode == 1:
            time.sleep(1)
          print("enderman teleported back")
        else:
          print("enderman teleported")
          firsthp = firsthp + 1
    case "shulker":
      if firstattacktimes % 2 == 0:
        if firstattack == 0:
          print("shulker teleported")
          firsthp = firsthp + 1
        else:
          print(firstmob, "shoots projectile at", secondmob)
          secondhp = secondhp - 5
          if fightmode == 1:
            time.sleep(1)
          print(secondmob, "levitates")
      else:
        print(firstmob, "shoots projectile at", secondmob)
        secondhp = secondhp - 5
        if fightmode == 1:
          time.sleep(1)
        print(secondmob, "levitates")
    case "evolker":
      if firstattacktimes % 2 == 0:
        print(firstmob, "summoned vexes")
        if fightmode == 1:
          time.sleep(1)
        print("summoned vex hits", secondmob)
        secondhp = secondhp - 4
      else:
        print("summoned vex hits", secondmob)
        if firstattack == 0 or firstattack == 1:
          print("summoned vex goes through wall")
          firsthp = firsthp + 4
        else:
          print("evolker summons spikes")
          secondhp = secondhp - 6
    case "witch":
      if firstattacktimes == 0:
        print("witch poisons", secondmob)
      else:
        print(secondmob, "hurts from poison")
        secondhp = secondhp - 1
        if firstattack == 0 or firstattack == 1:
          print("witch heals itself")
          firsthp = firsthp + 5
        else:
          print("witch throws potion at", secondmob)
          secondhp = secondhp - 5
    case "blaze" | "ghast":
      if firstattack == 0 or firstattack == 1:
        print(firstmob, "flies")
        firsthp = firsthp + 1
      else:
        print(firstmob, "shoots fireball at", secondmob)
        secondhp = secondhp - 5
    case "breeze":
      if firstattack == 0 or firstattack == 1:
        print(firstmob, "launches itself")
        firsthp = firsthp + 5
      else:
        print(firstmob, "shoots wind charge")
        secondhp = secondhp - 5
    case "piglin" | "piglin brute" | "baby piglin":
      if firstattack == 0 or firstattack == 1:
        print(firstmob, "shoots arrows at", secondmob)
        secondhp = secondhp - 7
      else:
        if "sword" in firstitem:
          print(firstmob, "hits", secondmob, "with", firstitem)
          secondhp = secondhp - 3
        else:
          print(firstmob, "hits", secondmob)
        secondhp = secondhp - 4
    case "spider" | "cave spider":
      if firstattack == 0 or firstattack == 1:
        print(firstmob, "pounces at", secondmob)
        secondhp = secondhp - 2
      else:
        print(firstmob, "climbs")
        firsthp = firsthp + 1
    case "bee":
      if firstattacktimes % 2 == 0:
        print(firstmob, "flies")
      else:
        print("bee attacks")
        secondhp = secondhp - 2
    case "big slime" | "big magma cube":
      if firsthp < 8:
        print(firstmob, "splits")
        if fightmode == 1:
          time.sleep(1)
        if firstmob == "big slime":
          firstmob = "medium slime"
        else:
          firstmob = "medium magma cube"
      else:
        print(firstmob, "pounces at", secondmob)
        secondhp = secondhp - 4
    case "medium slime" | "medium magma cube":
      if firsthp < 3:
        print(firstmob, "splits")
        if fightmode == 1:
          time.sleep(1)
        if firstmob == "medium slime":
          firstmob = "small slime"
        else:
          firstmob = "small magma cube"
      else:
        print(firstmob, "pounces at", secondmob)
        secondhp = secondhp - 2
    case "small slime" | "small magma cube":
      print(firstmob, "pounces at", secondmob)
    case "goat":
      print(firstmob, "crashes into", secondmob)
      secondhp = secondhp - 4
    case "snow golem":
      if firstattack == 0:
        print(firstmob, "takes damage from sun")
        firsthp = firsthp - 10
      else:
        print(firstmob, "throws snowball at", secondmob)
        secondhp = secondhp - 2
    case "player":
      if firstattack == 0 or firstattack == 1:
        if "sword" in firstitem:
          print(firstmob, "hits", secondmob, "with", firstitem)
          secondhp = secondhp - 6
        elif "apple" in firstitem:
          if firstitem == "apple":
            print("player eats apple")
            firsthp = firsthp + 3
          else:
            print("player eats", firstitem)
            firsthp = firsthp + 8
        else:
          print("player hides")
          firsthp = firsthp + 3
          if fightmode == 1:
            time.sleep(1)
          print("player reappears")
      else:
        print("player stacks up")
        firsthp = firsthp + 3
        if fightmode == 1:
            time.sleep(1)
        print("player delivers critical hit")
        secondhp = secondhp - 7
      if firsthp < 8:
        if fightmode == 1:
          time.sleep(1)
        print("player dodges", secondmob)
        firsthp = firsthp + 6
    case "wither storm":
      if firstattacktimes == 0:
        print("the wither storm has been summoned in")
        firstphase = 1
      else:
        if firstphase < 2:
          if firstattack == 0 and not secondmob == "wither storm":
            print("wither storm fires explosive wither skull at", secondmob)
            secondhp = secondhp - 8
          elif firstattack == 1:
            print("wither storm absorbs chunks of land")
            firstphase = firstphase + 0.1
            firsthp = firsthp + 50
          else:
            print("wither storm sucks up blocks")
            firstphase = firstphase + 0.05
            firsthp = firsthp + 100
        if firstphase > 1.9 and firstphase < 2.1:
          print("the wither storm is now phase 2")
          firstphase = 2.1
          if fightmode == 1:
            time.sleep(1)
        if firstphase > 2.09 and firstphase < 3:
          firsthp = 99999999999999999999
          if firstattack == 0 and not secondmob == "wither storm":
            print("wither storm points tractor beam at", secondmob)
            if fightmode == 1:
              time.sleep(1)
            print("wither storm starts devouring", secondmob)
            secondhp = secondhp - 20
          elif firstattack == 1:
            print("wither storm devours village")
            firstphase = firstphase + 0.1
          else:
            print("wither storm sucks up blocks")
            firstphase = firstphase + 0.05
      if firstphase > 2.9 and firstphase < 3.1:
        print("the wither storm is now phase 3")
        firstphase = 3.1
        if fightmode == 1:
          time.sleep(1)
      if firstphase > 3.09 and firstphase < 4:
        firsthp = 99999999999999999999
        if firstattack == 0 and not secondmob == "wither storm":
          print("wither storm points tractor beam at", secondmob)
          if fightmode == 1:
            time.sleep(1)
          print("wither storm starts devouring", secondmob)
          secondhp = secondhp - 20
        elif firstattack == 1:
          print("wither storm hits", secondmob, "with tentacle")
          secondhp = secondhp - 18
        else:
          print("wither storm sucks up blocks")
          firstphase = firstphase + 0.1
      if firstphase > 3.9 and firstphase < 4.1:
        print("wither storm is now phase 4")
        firstphase = 4.1
        if fightmode == 1:
            time.sleep(1)
      if firstphase > 4.09 and firstphase < 5:
        if secondmob == "player" or secondsmart == "Y":
          print(secondmob, "activates formidibomb")
          if fightmode == 1:
            time.sleep(1)
          print("formidibomb explodes")
          if fightmode == 1:
            time.sleep(1)
          print("wither storm splits in three")
          if fightmode == 1:
            time.sleep(1)
          print("the wither storm has been defeated...")
          time.sleep(1.5)
          print("...or has it?")
          time.sleep(1)
          print("wither storm parts recover")
          if fightmode == 1:
            time.sleep(1)
          print("command block sealed into body, wither storm now phase 5")
          firstphase = 5.1
        else:
          if firstattack == 0 or firstattack == 1:
            print("wither storm points tractor beam at", secondmob)
            if fightmode == 1:
              time.sleep(1)
            print("wither storm starts devouring", secondmob)
            secondhp = secondhp - 99999
          else:
            print("wither storm squishes", secondmob, "with tentacle")
          secondhp = secondhp - 999999
      if firstphase > 5.09 and firstphase < 6:
        if firstattack == 0 or firstattack == 1:
          print("wither storm points tractor beam at", secondmob)
          if fightmode == 1:
            time.sleep(1)
          print("wither storm starts devouring", secondmob)
          secondhp = secondhp - 99999
        elif firstattack == 3:
          print("wither storm squishes", secondmob, "with tentacle")
          secondhp = secondhp - 999999
        else:
          print("wither storm devours chunks of land")
          firstphase = firstphase + 0.45
      if firstphase > 5.9 and firstphase < 6.1:
        print("wither storm is now phase 6")
        firstphase = 6.1
        if fightmode == 1:
          time.sleep(1)
      if firstphase > 6.09 and firstphase < 7:
        print("wither storm devours village")
        if fightmode == 1:
          time.sleep(1)
        print("wither storm absorbs energy")
        print("the wither storm is now phase 7")
        firstphase = 7.1
        if fightmode == 1:
          time.sleep(1)
      if firstphase > 7.09 and firstphase < 8:
        if firstattacktimes % 2 == 0:
          print("wither storm devours chunks of land")
          firstphase = firstphase + 4.5
        else:
          print("wither storm prepares for evolution")
      if firstphase > 7.9 and firstphase < 8.1:
        firsthp = 9999999999
        print("the wither storm is now phase 8")
        firstphase = 8.1
        if fightmode == 1:
          time.sleep(1)
        print("hole from formidibomb opened up")
        if fightmode == 1:
          time.sleep(1)
      if firstphase > 8.09:
        if secondmob == "player" or secondsmart == "Y":
          print(secondmob, "goes inside the wither storm's body")
          if fightmode == 1:
            time.sleep(1)
          print(secondmob, "destroys command block")
          firsthp = 0
        else:
          print("wither storm destroys", secondmob)
          secondhp = 0
    case "pig" | "cow" | "sheep":
      if firstattack == 0:
        print(firstmob, "falls into lava")
        firsthp = 0
      else:
        print(firstmob, "walks around")
    case firstpick:
      if firstmobspecialattackone == "poison" or firstmobspecialattacktwo == "poison":
        if firstattacktimes == 0:
          print(secondmob, "has been poisoned")
          secondhp = secondhp - 4
        else:
          print(secondmob, "hurts from poison")
          secondhp = secondhp - 1
        if fightmode == 1:
          time.sleep(1)
      if firstattack == 0:
        match firstmobspecialattackone:
          case "sonic boom":
            print(firstmob, "charges up sonic boom")
            if fightmode == 1:
              time.sleep(1)
            print(firstmob, "releases sonic boom")
            secondhp = secondhp - firstmobspecialattackonedamage
          case "laser":
            print(firstmob, "fires laser beam at", secondmob)
            secondhp = secondhp - firstmobspecialattackonedamage
          case "fireball":
            print(firstmob, "shoots fireball at", secondmob)
            secondhp = secondhp - firstmobspecialattackonedamage
          case "fly":
            print(firstmob, "flies")
            firsthp = firsthp + 5
          case "heal":
            print(firstmob, "heals itself")
            firsthp = firsthp + firstmobspecialattackonedamage
          case "explosive wither skull":
            if random.randrange(0, 3) == 0:
              print(firstmob, "shoots grey wither skull at", secondmob)
              secondhp = secondhp - firstmobspecialattackonedamage
            else:
              print(firstmob, "shoots blue wither skull at", secondmob)
              secondhp = secondhp - 2 - firstmobspecialattackonedamage
          case "dragon breath":
            print(firstmob, "releases dragon breath")
            secondhp = secondhp - firstmobspecialattackonedamage
          case "clone":
            print(firstmob, "creates clones of itself")
            firsthp = firsthp + firstmobspecialattackonedamage
          case "summon spikes":
            print(firstmob, "summons spikes")
            secondhp = secondhp - firstmobspecialattackonedamage
          case "dig":
            print(firstmob, "digs")
            firsthp = firsthp + firstmobspecialattackonedamage
            if fightmode == 1:
              time.sleep(1)
            print(firstmob, "reappears")
          case "lightning":
            print(firstmob, "summoned lightning")
            secondhp = secondhp - firstmobspecialattackonedamage
          case "meteorite":
            print(firstmob, "fired a meteorite at", secondmob)
            if fightmode == 1:
              time.sleep(1)
            print("meteorite crashes")
            secondhp = secondhp - firstmobspecialattackonedamage
            if fightmode == 1:
              time.sleep(1)
            secondhp = secondhp - firstmobspecialattackonedamage
            print("explosion stops")
          case "none":
            print(firstmob, "hits", secondmob)
            secondhp = secondhp - firstmobattackdp
      elif firstattack == 1:
        match firstmobspecialattacktwo:
          case "sonic boom":
            print(firstmob, "charges up sonic boom")
            if fightmode == 1:
              time.sleep(1)
            print(firstmob, "releases sonic boom")
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "laser":
            print(firstmob, "fires laser beam at", secondmob)
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "fireball":
            print(firstmob, "shoots fireball at", secondmob)
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "fly":
            print(firstmob, "flies")
            firsthp = firsthp + 5
          case "heal":
            print(firstmob, "heals itself")
            firsthp = firsthp + firstmobspecialattacktwodamage
          case "explosive wither skull":
            if random.randrange(0, 3) == 0:
              print(firstmob, "shoots grey wither skull at", secondmob)
              secondhp = secondhp - firstmobspecialattacktwodamage
            else:
              print(firstmob, "shoots blue wither skull at", secondmob)
              secondhp = secondhp - 2 - firstmobspecialattacktwodamage
          case "dragon breath":
            print(firstmob, "releases dragon breath")
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "clone":
            print(firstmob, "creates clones of itself")
            firsthp = firsthp + firstmobspecialattacktwodamage
          case "summon spikes":
            print(firstmob, "summons spikes")
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "dig":
            print(firstmob, "digs")
            firsthp = firsthp + firstmobspecialattacktwodamage
            if fightmode == 1:
              time.sleep(1)
            print(firstmob, "reappears")
          case "lightning":
            print(firstmob, "summoned lightning")
            secondhp = secondhp - firstmobspecialattacktwodamage
          case "meteorite":
            print(firstmob, "fired a meteorite at", secondmob)
            if fightmode == 1:
              time.sleep(1)
            print("meteorite crashes")
            secondhp = secondhp - firstmobspecialattacktwodamage
            if fightmode == 1:
              time.sleep(1)
            secondhp = secondhp - firstmobspecialattacktwodamage
            print("explosion stops")
          case "none":
            print(firstmob, "hits", secondmob)
            secondhp = secondhp - firstmobattackdp
      else:
        print(firstmob, "hits", secondmob)
        secondhp = secondhp - firstmobattackdp
  if secondhp < 1:
    print(secondmob, "died")
    print("\n", firstmob, "wins!")
    break
  if fightmode == 1:
    time.sleep(1)
  firstattacktimes = firstattacktimes + 1
  match secondmob:
    case "zombie" | "zombified villager" | "zombified piglin" | "husk":
      if secondattacktimes % 2 == 0:
        print(secondmob, "walks toward", firstmob)
      else:
        if "sword" in seconditem:
          print(secondmob, "hits", firstmob, "with", seconditem)
          firsthp = firsthp - 2
        else:
          print(secondmob, "hits", firstmob)
        firsthp = firsthp - 2
    case "skeleton" | "pillager" | "stray" | "bogged":
      if secondattack == 0:
        print(secondmob, "walks toward", firstmob)
      else:
        if secondattacktimes % 2 == 0:
          print(secondmob, "reloads")
        else:
          print(secondmob, "shoots arrows at", firstmob)
          firsthp = firsthp - 6
    case "creeper":
      if secondattack == 0:
        print(secondmob, "walks toward", firstmob)
      else:
        if secondattacktimes % 2 == 0:
          print(secondmob, "flashes")
        else:
          print(secondmob, "blows up")
          secondblowup = True
    case "creaking":
      secondhp = 99999
      if secondattacktimes % 2 == 0:
        print(secondmob, "hits", firstmob)
        firsthp = firsthp - 4
      elif secondattack == 0:
        print("creaking heart has been broken")
        print("\n", firstmob, "wins!")
        break
      else:
        print(secondmob, "walks toward", firstmob)
    case "wither":
      if secondattacktimes == 0:
        print("the wither has been summoned in")
        firsthp = firsthp - 2
      else:
        if secondattack == 0:
          print(secondmob, "flies toward", firstmob)
        elif secondattack == 1:
          print(secondmob, "shoots blue wither skull at", firstmob)
          firsthp = firsthp - 10
        else:
          print(secondmob, "shoots grey wither skull at", firstmob)
          firsthp = firsthp - 8
      if secondhp < 151:
        if secondarmour == False:
          print("wither has gained armour")
          secondarmour = True
    case "warden":
      if secondattacktimes == 0:
        print(secondmob, "shrieks at", firstmob)
      else:
        if secondattack == 0:
          print("warden digs")
          secondhp = secondhp + 4
          if fightmode == 1:
            time.sleep(1)
          print("warden reappears")
        if secondattack == 1:
          print("warden charges up sonic boom")
          if fightmode == 1:
            time.sleep(1)
          print("warden releases sonic boom")
          firsthp = firsthp - 8
        else:
          print(secondmob, "hits", firstmob)
          firsthp = firsthp - 18
    case "ender dragon":
      if secondattacktimes % 2 == 0:
        print("dragon flies")
        secondhp = secondhp + 1
      else:
        print("dragon lands")
      if secondattack == 0:
        print("dragon releases dragon breath")
        firsthp = firsthp - 8
      elif secondattack == 1:
        print("dragon heals at crystal")
        secondhp = secondhp + 6
      else:
        print("dragon shoots fireball at", firstmob)
        firsthp = firsthp - 8
    case "baby zombie" | "baby zombified villager" | "baby zombified piglin":
      if secondattacktimes % 2 == 0:
        print(secondmob, "runs toward", firstmob)
        secondhp = secondhp + 1
      else:
        if "sword" in seconditem:
          print(secondmob, "hits", firstmob, "with", seconditem)
          firsthp = firsthp - 2
        else:
          print(secondmob, "hits", firstmob)
        firsthp = firsthp - 1
    case "drowned":
      if secondattacktimes % 2 == 0:
        print(secondmob, "walks toward", firstmob)
      else:
        if secondattack == 0 or secondattack == 1:
          print(secondmob, "hits", firstmob)
          firstmob = firstmob - 2
        else:
          print(secondmob, "throws trident at", firstmob)
          firsthp = firsthp - 6
    case "illusioner":
      if secondattacktimes % 2 == 0:
        print(secondmob, "creates clones of itself")
        secondhp = secondhp + 5
      else:
        if secondattack == 0 or secondattack == 1:
          print(secondmob, "shoots arrows at", firstmob)
          firsthp = firsthp - 6
        else:
          print(secondmob, "flies")
          secondhp = secondhp + 1
    case "iron golem" | "wither skeleton":
      if secondattacktimes % 2 == 0:
        print(secondmob, "walks toward", firstmob)
      else:
        print(secondmob, "hits", firstmob)
        firsthp = firsthp - 7
    case "ravenger" | "hoglin" | "zoglin" | "vindicator":
      if secondattacktimes % 2 == 0:
        print(secondmob, "charges at", firstmob)
        firsthp = firsthp - 5
      elif secondmob == "ravenger":
        print("ravenger pushes", firstmob, "away")
        secondhp = secondhp + 4
      else:
        if secondattack == 0:
          print(secondmob, "dodges", firstmob)
          secondhp = secondhp + 2
        else:
          print(secondmob, "charges at", firstmob)
          firsthp = firsthp - 5
    case "phantom" | "vex":
      if secondattacktimes % 2 == 0:
        print(secondmob, "flies at", firstmob)
        firsthp = firsthp - 2
      else:
        print(secondmob, "flies up")
        secondhp = secondhp + 2
    case "enderman":
      if secondattacktimes % 2 == 0:
        if secondattack == 0:
          print("enderman teleported")
          secondhp = secondhp + 1
        else:
          print(secondmob, "hits", firstmob)
          firsthp = firsthp - 5
      else:
        if secondattack == 0:
          print("enderman teleported away")
          secondhp = 30
          if fightmode == 1:
            time.sleep(1)
          print("enderman teleported back")
        else:
          print("enderman teleported")
          secondhp = secondhp + 1
    case "shulker":
      if secondattacktimes % 2 == 0:
        if secondattack == 0:
          print("shulker teleported")
          secondhp = secondhp + 1
        else:
          print(secondmob, "shoots projectile at", firstmob)
          firsthp = firsthp - 5
          if fightmode == 1:
            time.sleep(1)
          print(firstmob, "levitates")
      else:
        print(secondmob, "shoots projectile at", firstmob)
        firsthp = firsthp - 5
        if fightmode == 1:
          time.sleep(1)
        print(firstmob, "levitates")
    case "evolker":
      if secondattacktimes % 2 == 0:
        print(secondmob, "summoned vexes")
        if fightmode == 1:
          time.sleep(1)
        print("summoned vex hits", firstmob)
        firsthp = firsthp - 4
      else:
        print("summoned vex hits", firstmob)
        if secondattack == 0 or secondattack == 1:
          print("summoned vex goes through wall")
          secondhp = secondhp + 4
        else:
          print("evolker summons spikes")
          firsthp = firsthp - 6
    case "witch":
      if secondattacktimes == 0:
        print("witch poisons", firstmob)
      else:
        print(firstmob, "hurts from poison")
        firsthp = firsthp - 1
        if secondattack == 0 or secondattack == 1:
          print("witch heals itself")
          secondhp = secondhp + 5
        else:
          print("witch throws potion at", firstmob)
          firsthp = firsthp - 5
    case "blaze" | "ghast":
      if secondattack == 0 or secondattack == 1:
        print(secondmob, "flies")
        secondhp = secondhp + 1
      else:
        print(secondmob, "shoots fireball at", firstmob)
        firsthp = firsthp - 5
    case "breeze":
      if secondattack == 0 or secondattack == 1:
        print(secondmob, "launches itself")
        secondhp = secondhp + 5
      else:
        print(secondmob, "shoots wind charge")
        firsthp = firsthp - 5
    case "piglin" | "piglin brute" | "baby piglin":
      if secondattack == 0 or secondattack == 1:
        print(secondmob, "shoots arrows at", firstmob)
        firsthp = firsthp - 7
      else:
        if "sword" in seconditem:
          print(secondmob, "hits", firstmob, "with", seconditem)
          firsthp = firsthp - 3
        else:
          print(secondmob, "hits", firstmob)
        firsthp = firsthp - 4
    case "spider" | "cave spider":
      if secondattack == 0 or secondattack == 1:
        print(secondmob, "pounces at", firstmob)
        firsthp = firsthp - 2
      else:
        print(secondmob, "climbs")
        secondhp = secondhp + 1
    case "bee":
      if secondattacktimes % 2 == 0:
        print(secondmob, "flies")
      else:
        print("bee attacks")
        firsthp = firsthp - 2
    case "big slime" | "big magma cube":
      if secondhp < 8:
        print(secondmob, "splits")
        if fightmode == 1:
          time.sleep(1)
        if secondmob == "big slime":
          secondmob = "medium slime"
        else:
          secondmob = "medium magma cube"
      else:
        print(secondmob, "pounces at", firstmob)
        firsthp = firsthp - 4
    case "medium slime" | "medium magma cube":
      if secondhp < 3:
        print(secondmob, "splits")
        if fightmode == 1:
          time.sleep(1)
        if secondmob == "medium slime":
          secondmob = "small slime"
        else:
          secondmob = "small magma cube"
      else:
        print(secondmob, "pounces at", firstmob)
        firsthp = firsthp - 2
    case "small slime" | "small magma cube":
      print(secondmob, "pounces at", firstmob)
    case "goat":
      print(secondmob, "crashes into", firstmob)
      firsthp = firsthp - 4
    case "snow golem":
      if secondattack == 0:
        print(secondmob, "takes damage from sun")
        secondhp = secondhp - 10
      else:
        print(secondmob, "throws snowball at", firstmob)
        firsthp = firsthp - 2
    case "player":
      if secondattack == 0 or secondattack == 1:
        if "sword" in seconditem:
          print(secondmob, "hits", firstmob, "with", seconditem)
          firsthp = firsthp - 6
        elif "apple" in seconditem:
          if seconditem == "apple":
            print("player eats apple")
            secondhp = secondhp + 3
          else:
            print("player eats", seconditem)
            secondhp = secondhp + 8
        else:
          print("player hides")
          secondhp = secondhp + 3
          if fightmode == 1:
            time.sleep(1)
          print("player reappears")
      else:
        print("player stacks up")
        secondhp = secondhp + 3
        if fightmode == 1:
          time.sleep(1)
        print("player delivers critical hit")
        firsthp = firsthp - 7
      if secondhp < 8:
        if fightmode == 1:
          time.sleep(1)
        print("player dodges", firstmob)
        secondhp = secondhp + 6
    case "wither storm":
      if secondattacktimes == 0:
        print("the wither storm has been summoned in")
        secondphase = 1
      else:
        if secondphase < 2:
          if secondattack == 0 and not firstmob == "wither storm":
            print("wither storm fires explosive wither skull at", firstmob)
            firsthp = firsthp - 8
          elif secondattack == 1:
            print("wither storm absorbs chunks of land")
            secondphase = secondphase + 0.1
            secondhp = secondhp + 50
          else:
            print("wither storm sucks up blocks")
            secondphase = secondphase + 0.05
            secondhp = secondhp + 100
        if secondphase > 1.9 and secondphase < 2.1:
          print("the wither storm is now phase 2")
          secondphase = 2.1
          if fightmode == 1:
            time.sleep(1)
        if secondphase > 2.09 and secondphase < 3:
          secondhp = 99999999999999999999
          if secondattack == 0 and not firstmob == "wither storm":
            print("wither storm points tractor beam at", firstmob)
            if fightmode == 1:
              time.sleep(1)
            print("wither storm starts devouring", firstmob)
            firsthp = firsthp - 20
          elif secondattack == 1:
            print("wither storm devours village")
            secondphase = secondphase + 0.1
          else:
            print("wither storm sucks up blocks")
            secondphase = secondphase + 0.05
      if secondphase > 2.9 and secondphase < 3.1:
        print("the wither storm is now phase 3")
        secondphase = 3.1
        if fightmode == 1:
          time.sleep(1)
      if secondphase > 3.09 and secondphase < 4:
        secondhp = 99999999999999999999
        if secondattack == 0 and not firstmob == "wither storm":
          print("wither storm points tractor beam at", firstmob)
          if fightmode == 1:
            time.sleep(1)
          print("wither storm starts devouring", firstmob)
          firsthp = firsthp - 20
        elif secondattack == 1:
          print("wither storm hits", firstmob, "with tentacle")
          firsthp = firsthp - 18
        else:
          print("wither storm sucks up blocks")
          secondphase = secondphase + 0.1
      if secondphase > 3.9 and secondphase < 4.1:
        print("wither storm is now phase 4")
        secondphase = 4.1
        if fightmode == 1:
          time.sleep(1)
      if secondphase > 4.09 and secondphase < 5:
        if firstmob == "player" or firstsmart == "Y":
          print(firstmob, "activates formidibomb")
          if fightmode == 1:
            time.sleep(1)
          print("formidibomb explodes")
          if fightmode == 1:
            time.sleep(1)
          print("wither storm splits in three")
          if fightmode == 1:
            time.sleep(1)
          print("the wither storm has been defeated...")
          time.sleep(1.5)
          print("...or has it?")
          time.sleep(1)
          print("wither storm parts recover")
          if fightmode == 1:
            time.sleep(1)
          print("command block sealed into body, wither storm now phase 5")
          secondphase = 5.1
        else:
          if secondattack == 0 or secondattack == 1:
            print("wither storm points tractor beam at", firstmob)
            if fightmode == 1:
              time.sleep(1)
            print("wither storm starts devouring", firstmob)
            firsthp = firsthp - 99999
          else:
            print("wither storm squishes", firstmob, "with tentacle")
          firsthp = firsthp - 999999
      if secondphase > 5.09 and secondphase < 6:
        if secondattack == 0 or secondattack == 1:
          print("wither storm points tractor beam at", firstmob)
          if fightmode == 1:
            time.sleep(1)
          print("wither storm starts devouring", firstmob)
          firsthp = firsthp - 99999
        elif secondattack == 3:
          print("wither storm squishes", firstmob, "with tentacle")
          firsthp = firsthp - 999999
        else:
          print("wither storm devours chunks of land")
          secondphase = secondphase + 0.45
      if secondphase > 5.9 and secondphase < 6.1:
        print("wither storm is now phase 6")
        secondphase = 6.1
        if fightmode == 1:
          time.sleep(1)
      if secondphase > 6.09 and secondphase < 7:
        print("wither storm devours village")
        if fightmode == 1:
          time.sleep(1)
        print("wither storm absorbs energy")
        print("the wither storm is now phase 7")
        secondphase = 7.1
        if fightmode == 1:
          time.sleep(1)
      if secondphase > 7.09 and secondphase < 8:
        if secondattacktimes % 2 == 0:
          print("wither storm devours chunks of land")
          secondphase = secondphase + 4.5
        else:
          print("wither storm prepares for evolution")
      if secondphase > 7.9 and secondphase < 8.1:
        secondhp = 9999999999
        print("the wither storm is now phase 8")
        secondphase = 8.1
        if fightmode == 1:
          time.sleep(1)
        print("hole from formidibomb opened up")
        if fightmode == 1:
          time.sleep(1)
      if secondphase > 8.09:
        if firstmob == "player" or firstsmart == "Y":
          print(firstmob, "goes inside the wither storm's body")
          if fightmode == 1:
            time.sleep(1)
          print(firstmob, "destroys command block")
          secondhp = 0
        else:
          print("wither storm destroys", firstmob)
          firsthp = 0
    case "pig" | "cow" | "sheep":
      if secondattack == 0:
        print(secondmob, "falls into lava")
        secondhp = 0
      else:
        print(secondmob, "walks around")
    case secondpick:
      if secondmobspecialattackone == "poison" or secondmobspecialattacktwo == "poison":
        if secondattacktimes == 0:
          print(firstmob, "has been poisoned")
          firsthp = firsthp - secondmobspecialattackonedamage
        else:
          print(firstmob, "hurts from poison")
          firsthp = firsthp - secondmobspecialattackonedamage
        if fightmode == 1:
          time.sleep(1)
      if secondattack == 0:
        match secondmobspecialattackone:
          case "sonic boom":
            print(secondmob, "charges up sonic boom")
            if fightmode == 1:
              time.sleep(1)
            print(secondmob, "releases sonic boom")
            firsthp = firsthp - secondmobspecialattackonedamage
          case "laser":
            print(secondmob, "fires laser beam at", firstmob)
            firsthp = firsthp - secondmobspecialattackonedamage
          case "fireball":
            print(secondmob, "shoots fireball at", firstmob)
            firsthp = firsthp - secondmobspecialattackonedamage
          case "fly":
            print(secondmob, "flies")
            secondhp = secondhp + 5
          case "heal":
            print(secondmob, "heals itself")
            secondhp = secondhp + secondmobspecialattackonedamage
          case "explosive wither skull":
            if random.randrange(0, 3) == 0:
              print(secondmob, "shoots grey wither skull at", firstmob)
              firsthp = firsthp - secondmobspecialattackonedamage
            else:
              print(secondmob, "shoots blue wither skull at", firstmob)
              firsthp = firsthp - 2 - secondmobspecialattackonedamage
          case "dragon breath":
            print(secondmob, "releases dragon breath")
            firsthp = firsthp - secondmobspecialattackonedamage
          case "clone":
            print(secondmob, "creates clones of itself")
            secondhp = secondhp + secondmobspecialattackonedamage
          case "summon spikes":
            print(secondmob, "summons spikes")
            firsthp = firsthp - secondmobspecialattackonedamage
          case "dig":
            print(secondmob, "digs")
            secondhp = secondhp + secondmobspecialattackonedamage
            if fightmode == 1:
              time.sleep(1)
            print(secondmob, "reappears")
          case "lightning":
            print(secondmob, "summoned lightning")
            firsthp = firsthp - secondmobspecialattackonedamage
          case "meteorite":
            print(secondmob, "fired a meteorite at", firstmob)
            if fightmode == 1:
              time.sleep(1)
            print("meteorite crashes")
            firsthp = firsthp - secondmobspecialattackonedamage
            if fightmode == 1:
              time.sleep(1)
            firsthp = firsthp - secondmobspecialattackonedamage
            print("explosion stops")
          case "none":
            print(secondmob, "hits", firstmob)
            firsthp = firsthp - secondmobattackdp
      elif secondattack == 1:
        match secondmobspecialattacktwo:
          case "sonic boom":
            print(secondmob, "charges up sonic boom")
            if fightmode == 1:
              time.sleep(1)
            print(secondmob, "releases sonic boom")
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "laser":
            print(secondmob, "fires laser beam at", firstmob)
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "fireball":
            print(secondmob, "shoots fireball at", firstmob)
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "fly":
            print(secondmob, "flies")
            secondhp = secondhp + 5
          case "heal":
            print(secondmob, "heals itself")
            secondhp = secondhp + secondmobspecialattacktwodamage
          case "explosive wither skull":
            if random.randrange(0, 3) == 0:
              print(secondmob, "shoots grey wither skull at", firstmob)
              firsthp = firsthp - secondmobspecialattacktwodamage
            else:
              print(secondmob, "shoots blue wither skull at", firstmob)
              firsthp = firsthp - 2 - secondmobspecialattacktwodamage
          case "dragon breath":
            print(secondmob, "releases dragon breath")
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "clone":
            print(secondmob, "creates clones of itself")
            secondhp = secondhp + secondmobspecialattacktwodamage
          case "summon spikes":
            print(secondmob, "summons spikes")
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "dig":
            print(secondmob, "digs")
            secondhp = secondhp + secondmobspecialattacktwodamage
            if fightmode == 1:
              time.sleep(1)
            print(secondmob, "reappears")
          case "lightning":
            print(secondmob, "summoned lightning")
            firsthp = firsthp - secondmobspecialattacktwodamage
          case "meteorite":
            print(secondmob, "fired a meteorite at", firstmob)
            if fightmode == 1:
              time.sleep(1)
            print("meteorite crashes")
            firsthp = firsthp - secondmobspecialattacktwodamage
            if fightmode == 1:
              time.sleep(1)
            firsthp = firsthp - secondmobspecialattacktwodamage
            print("explosion stops")
          case "none":
            print(secondmob, "hits", firstmob)
            firsthp = firsthp - secondmobattackdp
      else:
        print(secondmob, "hits", firstmob)
        firsthp = firsthp - secondmobattackdp
  secondattacktimes = secondattacktimes + 1
  if fightmode == 1:
    time.sleep(1)
