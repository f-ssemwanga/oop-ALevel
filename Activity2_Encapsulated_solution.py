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
            del self.__occupants[index]
            
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
    def __init__(self, rooms, customers, receptionist, cleaner, manager):
        #hotel constructor method
        self.__rooms = rooms
        self.__customers = customers
        self.__receptionist = receptionist
        self.__cleaner = cleaner
        self.__manager = manager
    def cleanRooms(self):
        #method for cleaning the room
        #iterate over the rooms and clean the room if it needs to be cleaned
        for room in self.__rooms:
            if room.cleanRoom():
                print(f'{self.__cleaner} cleaned Room {room.getNumber()}')
    def checkIn(self, customers):
        #used to check in a customer
        for customer in customers:
            room  = self.__rooms[self.__customers[customer-1].getRoom() -1]
            room.addOccupant(self.__customers[customer -1])
            print(f'{self.__receptionist} checked in {self.__customers[customer -1].getName()}')
    def checkOut(self, customers):
        #used to check in a customer
        for customer in customers:
            room  = self.__rooms[self.__customers[customer-1].getRoom() -1]
            room.removeOccupant(self.__customers[customer -1])
            print(f'{self.__receptionist} checked out {self.__customers[customer -1].getName()}')
            self.takeFeedback(self.__customers[customer -1])
    def takeFeedback(self, customer):
        #take customer feedback
        if customer.getRating() >0:
            print(f'{self.__manager} says:\n{customer.getName()} was happy with their stay!')
        elif customer.getRating() <0:
            print(f'{self.__manager} says:\n{customer.getName()} was unhappy with their stay!')
        else:
            print(f'{self.__manager} says:\n{customer.getName()} found their stay to be ok.')
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
    hotel = Hotel(
        [Room(1,1,False), Room(2,2,True),Room(1,1,False)],
        [
            Customer(1, "Mrs. White"),
            Customer(2, "Mr. Green"),
            Customer(2, "Miss Scarlett"),
            Customer(3, "Mrs. Peacock"),
            Customer(2, "Prof. Plum"),
            Customer(3, "Col. Mustard")
        ], 
        "Jane", "Michael", "Janhavi")
    hotel.checkIn([1,2,3])
    hotel.checkOut([1])
    
    hotel.cleanRooms()
    
    hotel.checkIn([4])
    hotel.checkOut([4])
    hotel.checkIn([5])
    hotel.checkOut([5,2,3])
    
    hotel.cleanRooms()
    hotel.checkIn([6])
    hotel.checkOut([6])
    input()
    
if __name__ == '__main__':
    main()