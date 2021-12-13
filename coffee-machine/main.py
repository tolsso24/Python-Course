# Copyright 2021 Timmy Olsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import Machine as machine
import Drink as drink

# OBJECTS
# Coffeemachine
coffeeMachine = machine.Machine(100, 50, 76, 0)

# Drinks
espresso = drink.Drink("espresso", 10, 5, 5, 1.25)
latte = drink.Drink("latte", 5, 50, 10, 2.5)
cappuccino = drink.Drink("cappuccino", 15, 7, 8, 3)
drinks = [espresso, latte, cappuccino]

# Placeholder
emptyDrink = drink.Drink("none", 0, 0, 0, 0)
coffeeChosen = emptyDrink

# LOOP
running = True
while running:
    command = input("What would you like? (espresso/latte/cappuccino):")
    if command == "off":
        running = False
        break
    elif command == "report":
        coffeeMachine.report()
    elif command == "refill":
        coffeeMachine.refill(100, 50, 76, 0)
    else:
        for d in drinks:
            if command == d.name:
                coffeeChosen = d
        if coffeeChosen.name == "none":
            print("Not a valid input")

    if "none" not in coffeeChosen.name and coffeeMachine.checkResorcesEnough(coffeeChosen):
        moneyReturn = coffeeMachine.processCoins(coffeeChosen)
        if moneyReturn > 0:
            coffeeMachine.returnCoins(moneyReturn)
    coffeeMachine.makeCoffee(coffeeChosen)
    coffeeChosen = emptyDrink

