monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income - monthly_expenses
projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly savings are $"+str(monthly_saving)+".")
print("Projected savings after one year, with interest, is: $"+str(projected_saving)+".")