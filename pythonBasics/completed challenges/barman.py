def greeting(name):
  
    print(f"Nice to meet you {name}")
    

user_name = input("What is your name?")
greeting(user_name)

age = int(input("How old are you?"))

if age < 17:
    print("Go home!")
else:
    print(f"What can I get you for you, {user_name}? ")