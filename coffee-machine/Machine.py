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

import Coin as coin

# Coins
quarter = coin.Coin("quarter", 0.25)

class Machine:
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.coffeePayed = False

    def refill(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def checkResorcesEnough(self, drink):
        if self.water < drink.water:
            print("Sorry there is not enough water.")
            return False
        else:
            if self.milk < drink.milk:
                print("Sorry there is not enough milk.")
                return False
            else:
                if self.coffee < drink.coffee:
                    print("Sorry there is not enough coffee.")
                    return False
                else:
                    #resources sufficient
                    return True

    def returnCoins(self, amount):
        self.money -= amount
        print(f"You will receive ${amount} back")

    def processCoins(self, drink):
        totalCoinsAdded = 0
        while totalCoinsAdded < drink.price:
            print("Add coin by typing <amount> <cointype>, ex. 1 quarter")
            print("Type abort to abort the purchase and get the money back")
            coins = input(f"Input coin ({totalCoinsAdded} of {drink.price} added):")
            if quarter.name in coins:
                totalCoinsAdded += quarter.value * float(coins.split()[0])
            elif "abort" in coins:
                self.money += totalCoinsAdded
                return totalCoinsAdded
            else:
                print("Uncorrect input...")
        self.money += totalCoinsAdded
        if totalCoinsAdded > drink.price:
            totalCoinsAdded -= drink.price
        self.coffeePayed = True
        return totalCoinsAdded

    def makeCoffee(self, drink):
        if self.coffeePayed:
            self.water -= drink.water
            self.milk -= drink.milk
            self.coffee -= drink.coffee
            self.coffeePayed = False
            print(f"Here is your {drink.name}. Enjoy!")

