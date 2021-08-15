bill = input("What is the total bill? $")
people = input ("Number of people? ")
choose_tip_percent = input("How much tip would you like to give: 10%, 12%, or 15%? ")
tip_percent = int(choose_tip_percent)/100
total_bill = float(bill) + float(bill) * tip_percent
bill_per_person = total_bill / int(people)


print(f"Each person needs to pay ${round(bill_per_person,2)}.")
