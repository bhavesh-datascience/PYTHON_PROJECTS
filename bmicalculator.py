height = float(input("Enter the value of height: "))
weight = int(input("Enter the value of weight: "))

# Convert height to meters if greater than 10 feet
if height < 10:
 value = height * 0.3048
elif  height > 10:
  value = height/100
else:
 value = height

# # Calculate BMI using the formula (weight / (feet * feet))
bmi = weight / (value ** 2)

 
if bmi < 18.5:
 print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
 print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
 print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
 print(f"Your BMI is {bmi}, you are obese.")
else:
 print(f"Your BMI is {bmi}, you are clinically obese.")

 
 