from abc import ABC, abstractmethod

class Fighter(): # вводим класс бойца
    def __init__(self, name, attac_method):
        self.name = name
        self.attac_method = attac_method

    def choose(self, Weapon):
        print(f"{self.name} choose {Weapon.name}")

    def attac(self, Monster):
        print(f"{self.name} {self.attac_method} the {Monster.name}")

class Monster(): # вводим класс монстра
    def __init__(self, name):
        self.name = name

class Weapon(ABC): # вводим абстрактный класс оружия
    @abstractmethod
    # def __init__(self, name, attac_method):
    #     self.name = name
    #     self.attac_method = attac_method

    def attac(self, Weapon, Monster):
        pass
    def choose(self, Weapon):
        pass

class Sword(Weapon):
    def __init__(self, name, attac_method):
        self.name = name
        self.attac_method = attac_method

    def attac(self, Weapon, Monster):
        pass
    def choose(self, Weapon):
        pass

class Bow(Weapon):
    def __init__(self, name, attac_method):
        self.name = name
        self.attac_method = attac_method

    def attac(self, Weapon, Monster):
        pass
    def choose(self, Weapon):
        pass


Knight = Fighter("Knight", "Hit")
Archer = Fighter("Archer", "ArrowShoot")
BigMuzzle = Monster("BigMuzzle")
Octopus = Monster("Octopus")
BroadSword = Sword("BroadSword", "Hit")
RomanSword = Sword("RomanSword", "Hit")
TightBow = Bow("TightBow", "ArrowShoot")
CrossBow = Bow("CrossBow", "ArrowShoot")

Knight.choose(BroadSword)
Knight.attac(Octopus)
Knight.choose(RomanSword)
Knight.attac(Octopus)
Archer.choose(TightBow)
Archer.attac(BigMuzzle)
Archer.choose(CrossBow)
Archer.attac(BigMuzzle)




