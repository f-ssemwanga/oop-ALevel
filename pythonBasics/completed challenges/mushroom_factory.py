def work_hours(hours_work, kilos):
    hourly_rate = 10.50
    rate_per_kilo = 1
    
    total_wages = (hours_work * hourly_rate) + (kilos * rate_per_kilo)
    return total_wages

def main():
    hours_work = float(input("How many hours was your rota?"))
    kilos = float(input("How many kg did you pick up?"))
    wages = work_hours(hours_work, kilos)
    print(f"You have worked {hours_work} hours.")
    print(f"You produced {kilos} kilos.")
    print(f"Your day`s wage is {wages : .2f} £££.")
    
if __name__ == "__main__":
    main()