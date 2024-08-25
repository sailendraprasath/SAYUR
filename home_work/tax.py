annual_income = float(input("Enter your annual income in INR: "))
tax = 0.0
if annual_income <= 250000:
    tax = 0.0  
elif annual_income <= 500000:
    tax = (annual_income - 250000) * 0.05  
elif annual_income <= 1000000:
    tax = (250000 * 0.05) + (annual_income - 500000) * 0.2  
else:
    tax = (250000 * 0.05) + (500000 * 0.2) + (annual_income - 1000000) * 0.3  
print("Your annual income tax :",tax)