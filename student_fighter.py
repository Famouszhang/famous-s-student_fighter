class StudentFighter(object):
    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health
hausen = StudentFighter(strength=3, health=100, name="hausen")
yonnie = StudentFighter(strength=20, health=1000, name="yonnie")
print(hausen.name, hausen.strength, hausen.health)
print(yonnie.name, yonnie.strength, yonnie.health)
