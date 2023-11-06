class Customer:
    def __init__(self, bookedRoom, name):
        '''Customer class constructor'''
        self.__bookedRoom = bookedRoom
        self.__name = name
        self.__feedback = 0
        self.__rating =0 #added rating
    def incrementRating(self, increment):
        #Increments the rating of the hotel
        self.__rating += increment
    def getName(self):
        #returns the customer's name
        return self.__name
    def getRoom(self):
        #returns the booked room
        return self.__bookedRoom
    def getRating(self):
        #returns the rating
        return self.__rating
class Room:
    def __init__(self, number, capacity, clean):
        #room constructor Method
        self.__number = number
        self.__capacity = capacity
        self.__occupants = []
        self.__clean = clean
    def addOccupant(self, occupantIn):
        #adds a customer to the room
        #if room capacity is not exceeded
        #update occupants experience
        #update cleanliness of the room
        if len(self.__occupants) < self.__capacity:
            self.__occupants.append(occupantIn)
            occupantIn.incrementRating(1) # positive experience
        else:
            occupantIn.incrementRating(-1) # negative experience
            return
        if self.__clean:
            occupantIn.incrementRating(1) # room is clean
        else:
            occupantIn.incrementRating(-1)
        self.__clean = False
    def removeOccupant(self, occupantOut):
        #handles removal of an occupant
        index = -1  #stores the index of the occupant to be removed
        for pos, occupant in enumerate(self.__occupants):
            if occupantOut.getName() == occupant.getName():
                index = pos
        if index != -1:
            self.__occupants.pop(index)
            
        '''
        The enumerate function allows us to get the index and the object from the objects' list
        example usage:
        items = ['apple','banana', 'cherry']
        for index, value in enumerate(items):
            print(f'Index: {index}, Value: {value}')
        
        Outputs
        Index: 0 Value: Apple
        Index: 1 Value: banana
        Index: 2 Value: cherry
        
        '''
    def cleanRoom(self):
        #clean the room if it is empty
        if self.__occupants == []:
            self.__clean = True
        return self.__clean
    def getNumber(self):
        #returns the room number - needed when booking the room
        return self.__number
class Hotel:
    def __init__(self, rooms):
        self.__rooms = rooms

    def checkRooms(self):
        return self.__rooms
        
class Manager:
    def __init__(self, name):
        self.__name = name
            
class Cleaner:
    def __init__(self, name):
        self.__name = name

class Receptionist:
    def __init__(self, name):
        self.__name = name

def main():
    room1 = Room(1, 1, False)
    room2 = Room(2, 2, True)
    room3 = Room(3, 1, False)
    hotel = Hotel([room1,room2,room3])
    customer1 = Customer(1, "Mrs. White")
    customer2 = Customer(2, "Mr. Green")
    customer3 = Customer(2, "Miss. Scarlett")
    customer4 = Customer(3, "Mrs. Peacock")
    customer5 = Customer(2, "Prof. Plum")
    customer6 = Customer(3, "Col. Mustard")    
    receptionist = Receptionist("Jane")
    cleaner = Cleaner("Michael")
    manager = Manager("Janhavi")
    
    receptionist.checkIn(hotel, customer1)
    receptionist.checkIn(hotel, customer2)
    receptionist.checkIn(hotel, customer3)
    receptionist.checkOut(hotel, customer1, manager)
    
    cleaner.cleanRooms(hotel)
    
    receptionist.checkIn(hotel, customer4)
    receptionist.checkOut(hotel, customer4, manager)
    receptionist.checkIn(hotel, customer5)
    receptionist.checkOut(hotel, customer5, manager)
    receptionist.checkOut(hotel, customer2, manager)
    receptionist.checkOut(hotel, customer3, manager)
    
    cleaner.cleanRooms(hotel)
    
    receptionist.checkIn(hotel, customer6)
    receptionist.checkOut(hotel, customer6, manager)
    input()
    
if __name__ == '__main__':
    main()