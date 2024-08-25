weight=float(input("Enter Your weight in kilograms: "))
height=float(input("Enter Your height in meter"))

bmi=weight / (height**2)

print(f"your BMI is {bmi:.2f}")

if bmi <18.5:
    print("you are underweight.")
elif 18.5 <=bmi <24.9:
    print("you have a normal weight..")
elif 24.9<=bmi<29.9:
    print("you are overweight")
else:
    print("you are obese")