import random
foodsPicked = []
drinksPicked = []
fillerFood = []
fillerDrink = []
contin1 = ""
drinks = ["Fanta", "Coke", "Sprite", "Pepsi", "Root Beer", "Vanilla Cream Soda"]
food = ["Doritos", "Lay's", "Cheetos", "Ruffles", "Bugles", "Fruit Snacks"]
drinkPricesInOrder = [2.55, 2.55, 2.55, 2.55, 2.55, 3.25]
foodPricesInOrder = [2.25, 1.55, 2.15, 2.25, 2.25, 2.30]

#The list is because the pop funtion completly removes an item from the list above even though the list is only inputed as a parameter
drinksCOPY = ["Fanta", "Coke", "Sprite", "Pepsi", "Root Beer", "Vanilla Cream Soda"]
foodCOPY = ["Doritos", "Lay's", "Cheetos", "Ruffles", "Bugles", "Fruit Snacks"]
drinkPricesInOrderCOPY = [2.55, 2.55, 2.55, 2.55, 2.55, 3.25]
foodPricesInOrderCOPY = [2.25, 1.55, 2.15, 2.25, 2.25, 2.30]

#Randomly selects 3 items from the list above to be displayed. does not have repeated items
def randomItems(drinkLst, foodLst, drinkPrcLst, foodPrcLst, dPicked, fPicked):
  print("DRINKS UP FOR SALE\n__________________")
  for i in range(3):
    random1 = random.randint(0, len(drinkLst) - 1)
    print(str(i + 1) + ": " + str(drinkLst[random1]) + " ---> $" + str(drinkPrcLst[random1]))
    dPicked.append(drinkLst[random1])
    drinkLst.pop(random1)
    drinkPrcLst.pop(random1)
  print("\nFOOD UP FOR SALE\n________________")
  for i in range(3):
    random1 = random.randint(0, len(foodLst) - 1)
    print(str(i + 1) + ": " + str(foodLst[random1]) + " ---> $" + str(foodPrcLst[random1]))
    fPicked.append(foodLst[random1])
    foodLst.pop(random1)
    foodPrcLst.pop(random1)

#Checks To See if User has Enough To Buy the Item
def checkMoney(money, foodPrcLst, drinkPrcLst):
    if money < 1.55:
      print("YOU HAVE TOO LOW OF A BALANCE TO CONTINUE")
      itemList(fillerFood,fillerDrink)
      exit()

#Checks if the balance is entered as negative
def checkNegative(money):
  if money < 0:
    print("ERROR:NEGATIVE VALUE ENTERED") 
    exit()

#Checks how many items you have
def itemList(lst1, lst2):
  print("\nFoods bought:")
  print(lst1)
  print("Drinks bought:")
  print(lst2)
#Allows the user to pick items and pay for them while allowing repeat if they ask
def selectAndPay(Balance1):
  balanceCopy = Balance1
  checkNegative(Balance1)
  checkMoney(Balance1, foodPricesInOrderCOPY,       drinkPricesInOrderCOPY)
#Asking the user the type of item they desire
  foodOrDrink = input("Food or Drink?\n")
  if foodOrDrink.lower() == "food":
    option = input("What food item do you want(NAME OR NUMBER): \n")
#checks to see if item inputted matches item in stoc
    if option == "1":
      option = foodsPicked[0]
    elif option == "2":
      option = foodsPicked[1]
    elif option == "3":
      option = foodsPicked[2]
  elif foodOrDrink.lower() == "drink":
    option = input("What drink item do you want(NAME OR NUMBER): \n")
    if option == "1":
      option = drinksPicked[0]
    elif option == "2":
      option = drinksPicked[1]
    elif option == "3":
      option = drinksPicked[2]
  else:
    print("ERROR:INVALID ITEM ENTERED")
    exit()
#checks if they want food or drink
  if foodOrDrink.lower() == "drink":
#goes through the list of drinks to see if there is a match for item inputted
    for i in range(6):
      if option.lower() == drinksCOPY[i].lower():
        fillerDrink.append(drinksCOPY[i])
        Balance1 -= drinkPricesInOrderCOPY[i]
        Balance1 = round(Balance1, 2)
        for i in range(2):
#if item inputted is not in the machine, end process
          if option.lower() == drinks[i].lower():
            print("ERROR:ITEM NOT IN STOCK")
            Balance1 = balanceCopy
            exit()
#if there were no items purchased, end process
  if Balance1 == balanceCopy and foodOrDrink.lower() == "drink":
    print("ERROR:INVALID ITEM ENTERED")
    exit()
  if foodOrDrink.lower() == "food":
#goes through the list of food to see if there is a match for item inputted
    for i in range(6):
      if option.lower() == foodCOPY[i].lower():
        fillerFood.append(foodCOPY[i])
        Balance1 -= foodPricesInOrderCOPY[i]
        Balance1 = round(Balance1, 2)
        for i in range(2):
#checks to see if item inputted matches the stock and if not, end process
          if option.lower() == food[i].lower():
            print("ERROR:ITEM NOT IN STOCK")
            Balance1 = balanceCopy
            exit()
#if nothing is bought, end process
  if Balance1 == balanceCopy and foodOrDrink.lower() == "food":
    print("ERROR:INVALID ITEM ENTERED")
    exit()
#After purchase of item, displays the value of the remaining balance.
  print("Your Balance is now $" + str(Balance1)+ "\n_____________________")
#Code that allows the code to be repeated with a changed balance
  balHis = Balance1
#Asks if the user wants to continue purchasing from the vending machine, if it is a "yes" then it will loop the code.
  continue1 = input("DO YOU WANT TO SPEND MORE MONEY? (yes/no) \n")
  if continue1.lower() == "yes":
    selectAndPay(balHis)

#MAIN
#initializes the lists
randomItems(drinks, food, drinkPricesInOrder, foodPricesInOrder, drinksPicked, foodsPicked)
balance = float(input("\nENTER MONEY: "))
print("$" + str(balance) + " WAS ENTERED")
selectAndPay(balance)
itemList(fillerFood,fillerDrink)