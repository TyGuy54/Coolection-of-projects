class Character:
    def __init__(self, name, attack, energy):
        self.name = name
        self.attack = attack
        self.energy = energy

    def name(self):
        return self.name

    def attack(self):
        return self.attack
    
    def energy(self):
        return self.energy


class Monster(Character):
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return f'This is {self.name}'

class Player(Character):
    def __init__(self, func):
        self.func = func
        
    def __str__(self):
        return f'This is {self.name}'


monster = Monster('Ted', 1, 2)
print(monster)

player = Player('Ty', 2, 3)
print(player)
