class Warrior():

    def __init__(self, name, power, stamina, hair_color):
        self.name = name
        self.power = power
        self.stamina = stamina
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.stamina += 2

    def eat(self):
        print(f"{self.name} is eating")
        self.power += 1

    def hit(self):
        print(f"{self.name} hits")
        self.stamina -= 1

    def walk(self):
        print(f"{self.name} walks")

    def info(self):
        print(f"Warriors name - {self.name}")
        print(f"Warriors hair color - {self.hair_color}")
        print(f"Warriors power - {self.power}")
        print(f"Warriors stamina - {self.stamina}")

