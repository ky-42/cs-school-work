import random

import character_healer

##
# Creates new character type that is subclass fo healer
# also tests said class
##

class Gambler(character_healer.Healer):
    
    # Number of times the chance healths was hit
    # across all gambler characters
    chanceHealthHits = 0
    
    def __init__(self, name = "Bob", st = 5, health = 10, die = 3, reviveHealth = 3):

        # Adds a total of four points randomly to health and strength
        randomNum = random.randint(0, 4)
        newStrength = st + randomNum
        newHealth = health + (4-randomNum)

        super().__init__(name, newStrength, newHealth, die)
        
        # Random health that needs to be reached to increase health
        # significantly when hitting an enemy
        self.__chanceHealth = newHealth - random.randint(0, newHealth-1)
    
    def getChanceHealth(self):
        return self.__chanceHealth

    def specialAbility(self):
        # chance to add 1 health depending on how many times
        # chance health has been hit
        self.updateHealth(Gambler.chanceHealthHits%1)
        
        # If the current health is equal to the chance health
        # multiply the current health by 100 and increment
        # the number of times the chance health has been hit
        if self.getHealth() == self.__chanceHealth:
            self.updateHealth(self.getHealth()*100)
            Gambler.chanceHealthHits += 1
    
    def __str__(self):
        return f'Gambler, a specialized {super().__str__()}\n Chance Health: {self.getChanceHealth()}'

# Takes two instances of the character class
# or one of its subclasses and battles them
# till one dies returning the winners names
def battle(characterOne, characterTwo):
    print(f'BATTLE: {characterOne.getName()} vs {characterTwo.getName()}')

    # Battles the two characters will one dies
    while (characterOne.alive() and characterTwo.alive()):
        characterOne.hit(characterTwo)
        characterTwo.hit(characterOne)
        
    # Returns the name of the character that is alive
    # hence the winner
    if characterOne.alive():
        return characterOne.getName()
    return characterTwo.getName()

def main():
    # Creates an instance of each kind of character
    character = character_healer.Character('Abby')
    healer = character_healer.Healer('Bob', 11, 12, 3)
    gambler = Gambler('Clay', 9, 13, 6)
    
    print(character)
    print()
    print(healer)
    print()
    print(gambler)
    print()
    
    # Battles the healer and gambler
    battleWinner = battle(healer, gambler)
    print(f'Winner of {healer.getName()} vs {gambler.getName()} is {battleWinner}\n')

    print(healer)
    print()
    print(gambler)

if __name__ == "__main__":
    main()