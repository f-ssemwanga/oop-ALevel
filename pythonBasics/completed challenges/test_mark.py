def get_marks():
    mark1 = int(input("Enter the first mark (out of 100):"))
    mark2 = int(input("Enter the first mark (out of 100):"))
    mark3 = int(input("Enter the first mark (out of 100):"))
    return mark1, mark2, mark3

def calculate_marks(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

def main():
    mark1, mark2, mark3 = get_marks()
    average = calculate_marks(mark1, mark2, mark3)
    
    print("\nConfirmation:")
    print(f"Mark 1 : {mark1} / 100")
    print(f"Mark 2 : {mark2} / 100")
    print(f"Mark 3 : {mark3} / 100")
    print(f"Average : {average} / 100")

if __name__ == "__main__":
    main()