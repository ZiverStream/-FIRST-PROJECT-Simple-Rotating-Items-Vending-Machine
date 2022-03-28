import random
#List of items that will be rotated through
fillerFood = []
fillerDrink = []
drinks = ["Fanta", "Coke", "Sprite", "Pepsi", "Root Beer", "Vanilla Cream Soda"]
food = ["Doritos", "Lay's", "Cheetos", "Ruffles", "Bugles", "Fruit Snacks"]
drinkPricesInOrder = [2.55, 2.55, 2.55, 2.55, 2.55, 3.25]
foodPricesInOrder = [2.25, 1.55, 2.15, 2.25, 2.25, 2.30]

#The list is because the pop funtion completly removes an item from the list above even though the list is only inputed as a paremeted
drinksCOPY = ["Fanta", "Coke", "Sprite", "Pepsi", "Root Beer", "Vanilla Cream Soda"]
foodCOPY = ["Doritos", "Lay's", "Cheetos", "Ruffles", "Bugles", "Fruit Snacks"]
drinkPricesInOrderCOPY = [2.55, 2.55, 2.55, 2.55, 2.55, 3.25]
foodPricesInOrderCOPY = [2.25, 1.55, 2.15, 2.25, 2.25, 2.30]

#Randomly selects 3 items from the list above to be displayed. does not have repeated items
def randomItems(drinkLst, foodLst, drinkPrcLst, foodPrcLst):
  print("DRINKS UP FOR SALE\n__________________")
  for i in range(3):
    random1 = random.randint(0, len(drinkLst) - 1)
    print(str(i + 1) + ": " + str(drinkLst[random1]) + " ---> $" + str(drinkPrcLst[random1]))
    drinkLst.pop(random1)
    drinkPrcLst.pop(random1)
  print("\nFOOD UP FOR SALE\n________________")
  for i in range(3):
    random1 = random.randint(0, len(foodLst) - 1)
    print(str(i + 1) + ": " + str(foodLst[random1]) + " ---> $" + str(foodPrcLst[random1]))
    foodLst.pop(random1)
    foodPrcLst.pop(random1)

#Checks To See if User has Enough To Buy the Item
def checkMoney(money, foodPrcLst, drinkPrcLst):
  for i in range(len(drinkPricesInOrder)):
    if money < drinkPrcLst[i]:
      print("YOU HAVE TOO LOW OF A BALANCE TO CONTINUE")
      exit()
    if money < foodPrcLst[i]:
      print("YOU HAVE TOO LOW OF A BALANCE TO CONTINUE")
      exit()

#Checks if the balance is entered as negative
def checkNegative(money):
  if money < 0:
    print("ERROR:NEGATIVE VALUE ENTERED") 
    exit()

#Checks how many items you have
def itemList(lst1, lst2):
  print("Foods bought:")
  print(lst1)
  print("Drinks bought:")
  print(lst2)


#MAIN
randomItems(drinks, food, drinkPricesInOrder, foodPricesInOrder)
Balance = float(input("\nENTER MONEY: "))
balanceCopy = Balance
checkNegative(Balance)
checkMoney(Balance, foodPricesInOrderCOPY, drinkPricesInOrderCOPY)
print("$" + str(Balance) + " WAS ENTERED")

#Asking the user if the type of item they want
foodOrDrink = input("Food or Drink?\n")
if foodOrDrink.lower() == "food":
  option = input("What food item do you want(NAME OF THE ITEM): \n")

elif foodOrDrink.lower() == "drink":
  option = input("What drink item do you want(NAME OF THE ITEM): \n")
else:
  print("ERROR:INVALID ITEM ENTERED")
  exit()
if foodOrDrink.lower() == "drink":
  for i in range(6):
    if option.lower() == drinksCOPY[i].lower():
      fillerDrink.append(drinksCOPY[i])
      for i in range(2):
        if option.lower() == drinks[i].lower():
          print("ERROR:ITEM NOT IN STOCK")
          exit()
      Balance -= drinkPricesInOrderCOPY[i]
if Balance == balanceCopy and foodOrDrink.lower() == "drink":
  print("ERROR:INVALID ITEM ENTERED")
  exit()
if foodOrDrink.lower() == "food":
  for i in range(6):
    if option.lower() == foodCOPY[i].lower():
      fillerFood.append(foodCOPY[i])
      for i in range(2):
        if option.lower() == food[i].lower():
          print("ERROR:ITEM NOT IN STOCK")
          exit()
      Balance -= foodPricesInOrderCOPY[i]
if Balance == balanceCopy and foodOrDrink.lower() == "food":
  print("ERROR:INVALID ITEM ENTERED")
  exit()
#After purchase of item, displays the value of the remaining balance.
print("Your Balance is now $" + str(Balance)+ "\n_____________________")
continue1 = input("DO YOU WANT TO SPEND MORE MONEY? (yes/no) \n")
if continue1.lower() == "no":
  itemList(fillerFood,fillerDrink)
#Asks if the user wants to continue purchasing from the vending machine, if it is a "yes" then it will loop the code.
while continue1.lower() == "yes":
  balanceCopy = Balance
  checkNegative(Balance)
  checkMoney(Balance, foodPricesInOrderCOPY, drinkPricesInOrderCOPY)
  print("$" + str(Balance) + " WAS ENTERED")
  foodOrDrink = input("Food or Drink?\n")
  if foodOrDrink.lower() == "food":
    option = input("What food item do you want(NAME OF THE ITEM): \n")
  elif foodOrDrink.lower() == "drink":
    option = input("What drink item do you want(NAME OF THE ITEM): \n")
  else:
    print("ERROR:INVALID ITEM ENTERED")
    exit()
  if foodOrDrink.lower() == "drink":
    for i in range(6):
      if option.lower() == drinksCOPY[i].lower():
        fillerDrink.append(drinksCOPY[i])
        for i in range(2):
          if option.lower() == drinks[i].lower():
            print("ERROR:ITEM NOT IN STOCK")
            exit()
        Balance -= drinkPricesInOrderCOPY[i]
  if Balance == balanceCopy and foodOrDrink.lower() == "drink":
    print("ERROR:INVALID ITEM ENTERED")
    exit()
  if foodOrDrink.lower() == "food":
    for i in range(6):
      if option.lower() == foodCOPY[i].lower():
        fillerFood.append(foodCOPY[i])
        for i in range(2):
          if option.lower() == food[i].lower():
            print("ERROR:ITEM NOT IN STOCK")
            exit()
        Balance -= foodPricesInOrderCOPY[i]
  if Balance == balanceCopy and foodOrDrink.lower() == "food":
    print("ERROR:INVALID ITEM ENTERED")
    exit()
  print("Your Balance is now $" + str(Balance)+ "\n_____________________")
  continue1 = input("DO YOU WANT TO SPEND MORE MONEY? (yes/no) \n")
  if continue1.lower() == "no":
    itemList(fillerFood,fillerDrink)
  