def selection_statement():
    totalMark = 80
    passrate = 60
    mark1 = float(input("Enter the 1st mark: "))
    score = (mark1/totalMark) * 100
    
    if score >= passrate:
        print("Congratulations")
    else:
        print("Try one more time")
        
selection_statement()