Python.py
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"
    
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} km/h and uses {self.power}!"
    
class ArmoredHero(Superhero):
    def __init__(self, name, power, city, armor_level):
        super().__init__(name, power, city)
        self.__armor_level = armor_level  # private attribute

    def get_armor_level(self):
        return self.__armor_level

    def set_armor_level(self, level):
        if 0 <= level <= 100:
            self.__armor_level = level
        else:
            print("Armor level must be between 0 and 100.")
            
hero1 = Superhero("EcoMan", "Plant Control", "Green City")
hero2 = FlyingHero("SkyFlash", "Lightning Strike", "Cloudopolis", 300)
hero3 = ArmoredHero("SteelGuard", "Shock Shield", "Metroville", 85)

print(hero1.introduce())
print(hero2.use_power())
print(hero3.get_armor_level())
hero3.set_armor_level(95)           
    
    