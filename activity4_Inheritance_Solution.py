from abc import ABC, ABCMeta, abstractmethod
class Animal(metaclass =ABCMeta):
  '''Animal abstract class'''
  def __init__(self) -> None:
      self._coldBlooded = False
      self._skinType = None
      self._tail = False
      self._legs = 0
      self._arms = 0
      self._wings = 0
      
  #create the abstract methods
  @abstractmethod
  def move(self):
    pass
  
  @abstractmethod
  def eat(self):
    pass
  
  @abstractmethod
  def eat(self):
    pass
  
  @abstractmethod
  def getInfo(self):
    pass
class Mammal(Animal):
  '''mammal inherits animal'''
  def __init__(self):
    super().__init__()
    self.__skinType ="fur" 
  def birth(self):
    print("This animal gives birth to live young")
  def getInfo(self):
    return super().getInfo()
  

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
class Reptile(Animal):
  '''Reptile inherits from Animal - must implement abstracted methods that apply to it'''
  def __init__(self) -> None:
    '''must call the super method and pass additional parameters/values'''
    super().__init__()  
    self._coldBlooded = True
    self._skinType = "scales"
    self._tail = True
    self._legs = 4
  
  def birth(self):
    '''implements the birth abstract method'''
    print('This animal lays eggs')
  def hibernate(self):
    '''implements its own method not part of its parent class'''
    print("This animal hibernates")

class Tortoise(Reptile):
  '''Implement Tortoise which inherits from Reptile'''
  def __init__(self) -> None:
    '''does not modify any of the parental attributes hence empty constructor'''
    super().__init__()
    
  def move(self):
    print("This animal walks")
  def eat(self):
    print('This animal is a herbivore')
  def getInfo(self):
    print("Tortoise")
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
class Snake(Reptile):
    def __init__(self):
      super().__init__()
      self._legs = 0
         
    def move(self):
        print("This animal slithers")
        
    def eat(self):
        print("This animal is a carnivore")
        
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
      
  

class Turtle(Tortoise):
    def __init__(self):
      super().__init__()  
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
        

        
class Otter(Mammal):
    def __init__(self):
      super().__init__()
      self._tail = True
      self._legs = 4
      
        
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
        
class Gorilla(Mammal):
    def __init__(self):
      super().__init__()
      self._legs = 2
      self._arms = 2
      
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
        
class Bat(Mammal):
    def __init__(self):
        super().__init__()
        self._tail = True
        self._legs = 2
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