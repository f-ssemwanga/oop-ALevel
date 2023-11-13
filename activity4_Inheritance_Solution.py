class Tortoise:
    def __init__(self):
        self._coldBlooded = True
        self._skinType = "scales"
        self._tail = True
        self._legs = 4
        self._arms = 0
        self._wings = 0
    
    def move(self):
        print("This animal walks")
        
    def eat(self):
        print("This animal is a herbivore")

    def birth(self):
        print("This animal lays eggs")
        
    def hibernate(self):
        print("This animal hibernates")
        
    def getInfo(self):
        print("Tortoise:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        self.hibernate()
        print()
        
class Turtle:
    def __init__(self):
        self._coldBlooded = True
        self._skinType = "scales"
        self._tail = True
        self._legs = 4
        self._arms = 0
        self._wings = 0
    
    def move(self):
        print("This animal crawls and swims")
        
    def eat(self):
        print("This animal is an omnivore")
        
    def birth(self):
        print("This animal lays eggs")
        
    def hibernate(self):
        print("This animal hibernates")
        
    def getInfo(self):
        print("Turtle:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        self.hibernate()
        print()
        
class Snake:
    def __init__(self):
        self._coldBlooded = True
        self._skinType = "scales"
        self._tail = True
        self._legs = 0
        self._arms = 0
        self._wings = 0
        
    def move(self):
        print("This animal slithers")
        
    def eat(self):
        print("This animal is a carnivore")

    def birth(self):
        print("This animal lays eggs")
        
    def hibernate(self):
        print("This animal hibernates")
        
    def getInfo(self):
        print("Snake:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        self.hibernate()
        print()
        
class Otter:
    def __init__(self):
        self._coldBlooded = False
        self._skinType = "fur"
        self._tail = True
        self._legs = 4
        self._arms = 0
        self._wings = 0
        
    def move(self):
        print("This animal walks and swims")
        
    def eat(self):
        print("This animal is an omnivore")

    def birth(self):
        print("This animal gives birth to live young")
        
    def getInfo(self):
        print("Otter:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        print()
        
class Gorilla:
    def __init__(self):
        self._coldBlooded = False
        self._skinType = "fur"
        self._tail = False
        self._legs = 2
        self._arms = 2
        self._wings = 0
        
    def move(self):
        print("This animal walks and climbs")
        
    def eat(self):
        print("This animal is an herbivore")
    
    def birth(self):
        print("This animal gives birth to live young")
        
    def getInfo(self):
        print("Gorilla:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        print()
        
class Bat:
    def __init__(self):
        self._coldBlooded = False
        self._skinType = "fur"
        self._tail = True
        self._legs = 2
        self._arms = 0
        self._wings = 2
        
    def move(self):
        print("This animal flies")
        
    def eat(self):
        print("This animal is an omnivore")
    
    def birth(self):
        print("This animal gives birth to live young")
        
    def hibernate(self):
        print("This animal hibernates")
        
    def getInfo(self):
        print("Bat:")
        if self._coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self._skinType != None:
            print("This animal is covered in " + self._skinType)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")
        self.move()
        self.eat()
        self.birth()
        self.hibernate()
        print()
        
def main():
    tortoise = Tortoise()
    turtle = Turtle()
    snake = Snake()
    otter = Otter()
    gorilla = Gorilla()
    bat = Bat()
    
    tortoise.getInfo()
    turtle.getInfo()
    snake.getInfo()
    otter.getInfo()
    gorilla.getInfo()
    bat.getInfo()
    input()
	
if __name__ == '__main__':
    main()