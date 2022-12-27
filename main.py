from random import randint


class Character:
    def __init__(self, name):
        self.name = name       
        
    def attack(self):
        return (f'{self.name} нанёс противнику урон, '
                f'равный {self.attack_p}')

    def defence(self):
        return (f'{self.name} блокировал {self.defence_p} ед. урона')

    def special(self):
        return (f'{self.name} применил специальное умение {self.special_p}') 


class Warrior(Character):

    def __init__(self, name):
        super().__init__(name)
        self.attack_p = 5 + randint(3, 5)
        self.defence_p = 10 + randint(5, 10)
        self.special_p = '«Выносливость {80 + 25}»'

    def attack(self):
        return super().attack()

    def defence(self):
        return super().defence()

    def special(self):
        return super().special()    
  

class Mage(Character):

    def __init__(self, name):
        super().__init__(name)
        self.attack_p = 5 + randint(5, 10)
        self.defence_p = 10 + randint(-2, 2)
        self.special_p = '«Атака {5 + 40}»'

    def attack(self):
        return super().attack()

    def defence(self):
        return super().defence()

    def special(self):
        return super().special()  


class Healer(Character):

    def __init__(self, name):
        super().__init__(name)
        self.attack_p = 5 + randint(-3, -1)
        self.defence_p = 10 + randint(2, 5)
        self.special_p = '«Защита {10 + 30}»'

    def attack(self):
        return super().attack()

    def defence(self):
        return super().defence()

    def special(self):
        return super().special()  


warrior_1 = Warrior('Воитель')
mage_1 = Mage('Маг')
healer_1 = Healer('Лекарь')

print(warrior_1.attack())
print(mage_1.attack())
print(healer_1.defence())
