##
# Weapon class and sub classes for Graveyards and Guards
##

class Weapon():
    def __init__(self, damage=1):
        self.__damage = damage
    
    def getDamage(self):
        return self.__damage
    
    def setDamage(self, damage):
        self.__damage = damage
    
    def __str__(self):
        return f'This weapon does {self.getDamage()} damage.'

# Sword class that is subclass of a weappon
class Sword(Weapon):
    def __init__(self, damage=4, swordType='Short'):
        super().__init__(damage)
        self.__swordType = swordType

    def __str__(self):
        return f'{self.__swordType} Sword. {super().__str__()}'

# Projectile class that is subclass of a weappon
class Projectile(Weapon):
    def __init__(self, damage=2):
        super().__init__(damage)
        
        self.__brokenStatus = False
    
    def getBrokenStatus(self):
        return self.__brokenStatus
    
    def setBrokenStatus(self, brokenStatus):
        self.__brokenStatus = brokenStatus
    
    def breakProjectile(self):
        # Sets projectile status to broken and halfs damage
        self.setBrokenStatus(True)
        self.setDamage(self.getDamage()//2)
    
    def __str__(self):
        condition = 'Broken' if self.getBrokenStatus() else 'Good condition'
        return f'Projectile. {condition}. {super().__str__()}'

def main():
    # Create two instances of each class in this file
    # one with default values and one with passed values
    weaponOne = Weapon()
    weaponTwo = Weapon(5)
    
    swordOne = Sword()
    swordTwo = Sword(10, 'Long')
    
    projectileOne = Projectile()
    projectileTwo = Projectile(8)
    
    print(weaponOne)
    print(swordOne)
    print(projectileOne)
    print(weaponTwo)
    print(swordTwo)
    print(projectileTwo)
    
    # Breaks a projectile
    projectileTwo.breakProjectile()

    print(projectileTwo)

if __name__ == '__main__':
    main()