def get_user_info():
    pocket_money = float(input("Input your weekly pocket money : ££ "))
    phone_bill = float(input("Input your weekly spending on phone : ££ "))
    food = float(input("Input your weekly spending on food: ££ "))
    meeting_friends = float(input("Input your weekly spending on friends : ££ "))
    return pocket_money, phone_bill, food, meeting_friends

def calculate_spending(pocket_money, phone_bill, food, meeting_friends):
    
    total_expenses = phone_bill + food + meeting_friends
    money_left = pocket_money - total_expenses
    print(f"\nMoney left:  {money_left : .2f}")
    print(f"You spend {total_expenses} ££")
    
    if total_expenses == money_left:
        print("You spent all money")
    else:
        print(f"You can save {money_left}££") 
    
def main():
    print("Welcome to pocket money calculator!")
    pocket_money, phone_bill, food, meeting_friends = get_user_info()
    calculate_spending(pocket_money, phone_bill, food, meeting_friends)
    
if __name__ == "__main__":
    main()