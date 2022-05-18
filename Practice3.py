''' This app is a BMI calculator app
 Lets get the users name, weight and height. Here i can use
 this method for multiple line commenting
 '''


def B_M_I(W, H):
    ans = W/(H**2)
    return round(ans, 1)


print("Welcome to BMI CAL, kindly fill in the sections below")
f_name = str(input("First Name: "))
l_name = str(input("Last Name: "))
height = float(input("Height (in meters): "))
weight = float(input("Weight (in kilograms): "))
# Now lets get to the calculation
BMI = B_M_I(height, weight)
# Display the users BMI and the category they belong
if(BMI < 18.5):
    print(f_name, l_name, "your BMI is", BMI, "(Underweight)")
elif((BMI >= 18.5) and (BMI <= 24.9)):
    print(f_name, l_name, "your BMI is", BMI, "(Normal)")
elif((BMI >= 25) and (BMI <= 29.9)):
    print(f_name, l_name, "your BMI is", BMI, "(Overweight)")
else:
    print(f_name, l_name, "your BMI is", BMI, "(Obese)")
