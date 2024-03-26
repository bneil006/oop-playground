class Creature():
    def move(self):
        print("The creature moves")

class Dragon(Creature):
    def move(self):
        print("The dragon flys")

class Kraken(Creature):
    def move(self):
        print("The kraken swins")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()