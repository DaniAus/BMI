weight_user = float(input("Please enter your weight in kilograms: "))
# asks the user what thier weight is in kilograms

height_user = float(input("Please enter your height in metres: "))
# asks the user what their height is in metres

user_bmi = weight_user / (height_user * height_user)
# calculating the users BMI

if user_bmi >= 30:
    print (f"Your BMI is {user_bmi:.2f} this is considered obese")
# if the users bmi is over 30 this message will display

elif user_bmi >= 25 and user_bmi < 30:
    print (f"Your BMI is {user_bmi:.2f} this is considered overweight")
# if the users bmi is over 25 but under 30 this message will display

elif user_bmi >= 18.5 and user_bmi < 25:
    print (f"Your BMI is {user_bmi:.2f} this is considered normal")
# if the users bmi is over 18.5 but under 25 this message will display

else:
    print(f"Your BMI is {user_bmi:.2f} this is considered underweight")
# if the users bmi is under 18.5 this message will display