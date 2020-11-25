# Code for Day 3, Exercise 2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2), 1)

if bmi < 18.5:
    print('Your BMI is {}, you are underweight.'.format(bmi))

else:
    if bmi < 25:
        print('Your BMI is {}, you have a normal weight.'.format(bmi))

    else:
        if bmi < 30:
            print('Your BMI is {}, you are slightly overweight.'.format(bmi))

        else:
            if bmi < 35:
                print('Your BMI is {}, you are obese.'.format(bmi))

            else:
                print('Your BMI is {}, you are clinically obese.'.format(bmi))
