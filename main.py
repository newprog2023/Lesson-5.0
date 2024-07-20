class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 6
        self.power -= 2

    def walk(self):
        print(f'{self.name} гуляет')
        self.endurance -= 1
        self.power += 1

    def info(self):
        print(f'имя воина -          {self.name}')
        print(f"цвет волос воина -   {self.hair_color}")
        print(f"сила воина -         {self.power}")
        print(f'выносливость воина - {self.endurance}')


war1 = Warrior("Илья", 76, 54,"блондин")
war2 = Warrior("Добрыня", 60, 60,"рыжий")

war1.info()
war2.info()

war1.sleep()
war2.eat()
war1.hit()
war2.sleep()
war1.eat()
war2.hit()
war1.walk()
war2.walk()
war2.eat()
war1.eat()
war2.hit()

war1.info()
war2.info()

