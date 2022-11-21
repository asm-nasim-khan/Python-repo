def attendance_calculator(class_count):
    p = (100 * class_count)/25
    if p >= 70:
        print("Percetage: ",p,"%")
        print("Eligible for final")
    else:
        print("Not Eligible")

#------Tester======
attendance_calculator(22)

