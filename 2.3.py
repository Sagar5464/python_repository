class animal:
    def make_sound(self):
        print("Some generic animal sounds")
class dog(animal):
    def __init__(self, name="Husky"):
        self.name = name
    def make_sound(self):
        print(f"{self.name} says Bow!")
class cat(animal):
    def __init__(self, name="Max"):
        self.name = name
    def make_sound(self):
        print(f"{self.name} says Meow!")
class Bird(animal):
    def __init__(self, name="Perks"):
        self.name = name
    def make_sound(self):
        print(f"{self.name} says Tweet!")
a1 = [dog(), cat(), Bird()]
for a in a1:
    a.make_sound()  
