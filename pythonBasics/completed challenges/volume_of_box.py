def calculate_volume(lenght, width, height):
    volume = lenght * width * height
    return volume

def main():
    lenght = float(input("Input the lenght: "))
    width =  float(input("Input the width: "))
    height =  float(input("Input the height: "))
    
    volume = calculate_volume(lenght, width, height)
    print(f"The volume is : {volume}")
    
if __name__ == "__main__":
    main()
    