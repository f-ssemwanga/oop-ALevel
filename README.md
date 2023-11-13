# oop-ALevel
OOp Principles A Level 

### Task 1 - This is the very first Task 

Students are required to Use pseudocode to write a class with relevant attributes and methods to represent a digital clock object. It should represent the time as a 24 hour clock, and include methods to: create a new object, set the time manually, display the time, and update the time at the end of each minute.
![Task 1 Pseudo Algorithm](oop_Task1_Clock.png)

### Extension
- Add functionality so that the clock automatically displays from the starting minute and hour
- Add functionality so that the clock now has changing seconds.

### Task 2 - OOP Programming Activity 1 - The Bank Task

This Activity uses Skeleton code [OOP_Activity1_Skeleton_Code](OOP_Activity1_skeleton_Code.py) is part of a program that allows a user to create a bank account, login to their account, check their balance and deposit or withdraw money from their account. 

It defines an account class, that stores information about the 

individual bank accounts, and a Bank class, that holds all of the Bank accounts and performs operations on individual accounts when asked to by the user.  
 
Add the missing attributes and method logic to the Activity 1 Skeleton Code to complete its functionality. No changes should be made to main, no new methods should be defined, and the parameters that the methods use should not be changed, deleted or added to. 

### Task 3 - Encapsulation - Demonstrate understanding and implementation of encapsulation
The Activity 2 Skeleton Code is a system that manages a hotel and its staff.  You have been provided with 2 files 
- [Activity 2 - Encapsulation Skeleton Code](Activity2_Encapsulated%20Skeleton.py)

- [Activity 2 - None Encapsulated code](Activity2_None-Encapsulated.py)

Customers are checked in and out of their rooms, and leave feedback depending on how their stay was (if they are successfully checked in or their room is clean they become happier with their stay, and if their room is overbooked or unclean they become less happy with their stay). 

Recreate the Activity 2 Non-Encapsulated code so that it keeps the same functionality but is properly encapsulated.  

There should be classes for: Hotel, Room, Customer, Manager, Receptionist and Cleaner.  

The manager should be responsible for processing feedback, the cleaner should be responsible for cleaning rooms, and the receptionist should be responsible for checking customers in and out of their rooms.  

All attributes should be made private (although you may add any methods that you think are helpful). 

You may use the provided Activity 2 Encapsulated Skeleton code, which provides a converted main method and constructors for each class that do not need to be altered. 

### Task 4 - Inheritance and Abstract methods
- The code template provides contains classes for various animals, describing what attributes they have and what actions they can do.

- The task is to do the following:
1. Keep  the functionality of the code i.e. produces the same output
2. Add 3 additional classes - Animal, Reptile  and Mammal
3. The Animal class should include abstract methods
4. Classes should inherit from other classes as appropriate, and as much functionality as possible should be moved to the 3 new classes
5. The main method should not be altered.
- ![Task Diagram showing relationship between the classes](inheritance_Abstract_Methods_diagram.png)
- ![Start up code templates for inheritance and Abstract method implementation](abstract_Method_Inhertance_Code_StartUp.png)
- [Main code template](Activity4_SkeletonCode.py)