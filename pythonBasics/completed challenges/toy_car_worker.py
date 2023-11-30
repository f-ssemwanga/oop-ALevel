def work_hours(hours_worked, made_toys):
    hourly_rate = 9
    toy_rate = 0.60
    
    total_wages = (hours_worked * hourly_rate) + (made_toys * toy_rate)
    return total_wages

def main():
    hours_worked = float(input("How many hours did you work?"))
    made_toys = float(input("How many toys did you do?"))
    wages = work_hours(hours_worked, made_toys)
    print(f"You worked {hours_worked} hours.\nYou produced {made_toys} trains.")
    print(f"\nYour day`s wage is {wages : .2f} £.")
    
if __name__ == "__main__":
    main()