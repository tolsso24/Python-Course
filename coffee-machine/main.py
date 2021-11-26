# OBJECTS
# Coffeemachine
water = 100
milk = 50
coffee = 76
money = 2.5

# LOOP
running = True
while running:
    command = input('What would you like? (espresso/latte/cappuccino):')
    if command == "off":
        running = False
        break
    elif command == "report":
        print(f"Water: {water}ml")
        print("Milk: %a" % (milk), "ml", sep="")
        print("Coffee: %a" % (coffee), "g", sep="")
        print("Money: $%a" % (money))
