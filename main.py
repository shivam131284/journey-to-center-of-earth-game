print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the journey to the center of earth.")
print("Your mission is to find the treasure and hopefully make it out alive.")

a = input("you are at the entry of cave where you like to go left or right?  ")

choice_1 = a.lower()

if choice_1 == "left":
  print("you have been eaten by goblin!! GAME OVER!")

elif choice_1 == "right":
  choice_2 = input("you fell in a hole that took you to center of earth!! where would you like to go left or right?" ).lower()

  if choice_2 == "left":
    print("you are dead by lava")
    

  elif choice_2 == "right":
    choice_3 = input("you see a red colored light and white colored light where would you like to go red or white ?")
  

    if choice_3 == "white":
      print("congratulations you found monolith and you are now abducted by the aliens GAME OVER!!!!!!!!!!")

    elif choice_3 == "red":
      print("you found a red rare jewel, bete mauj kardi !!")
      print("paisa hi paisa hoga !!!!!!")
      print("aadha hissa mujhe bhi bro !!!!!!")
else :
  print("invalid input")




#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload