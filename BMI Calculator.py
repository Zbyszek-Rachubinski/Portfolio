weight = float(input("Please, specify your weight in kg"))
height = float(input("Please, specify your height cm")) * 0.01

BMI = weight / height**2

if BMI < 18.5:

    print("Your Body Mass Index (BMI) is " + str(BMI))
    print("You are Underweight")

elif BMI >= 18.5 and BMI < 25:

    print("Your Body Mass Index (BMI) is " + str(BMI))
    print("It is Normal")

elif BMI >= 25 and BMI < 30:

    print("Your Body Mass Index (BMI) is " + str(BMI))
    print("You are Overweight")

else:

    print("Your Body Mass Index (BMI) is " + str(BMI))
    print("You have a problem with Obesity")
