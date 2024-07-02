# PROGRAM NAME: soham_patel_bmi_calculator
# PROGRAM AUTHOR: SOHAM PATEL
# DATE: 10-02-2023
# PROGRAM DESCRIPTION: Body Mass Index calculation and define the relevant category




# MY CONSTANTS FOR THE CODE
MINMUM_REQUIRED_HEIGHT = 20
MAXIMUM_REQUIRED_HEIGHT = 120
MINIMUM_REQUIRED_WEIGHT = 10
EXACT_BMI_NUMBER = 703



# VARIABLES I USED
height_in_inches = 0
weight_in_pounds = 0
the_bmi = 0
your_category_is = ""
bmi_number_for_the_category = 0
measured_weight = 0



print("Welcome to the BMI calculator")


# INPUT
try:
    height_in_inches = float(input("Please enter your height in iches."))
    weight_in_pounds = float(input("Please enter your weight in pounds."))

    # CHECK IF THE INPUT IS A WHOLE NUMBER OR NOT AND IF NOT SHOW THE ERROR
except ValueError:
    print("The height and weight must be a whole number.")



# MY VALIDATION FOR THE HEIGHT 

if not MINMUM_REQUIRED_HEIGHT <= height_in_inches <= MAXIMUM_REQUIRED_HEIGHT:
    print('INPUT IS INVALID "Height must be entered between 20" to 120". ')


# MY VALIDATION FOR THE WEIGHT 

elif weight_in_pounds < MINIMUM_REQUIRED_WEIGHT:
    print('Weight must be greater than {MINIMUM_REQUIRED_WEIGHT} pounds.')


# HOW I CALCULATED BMI
else:
    the_bmi = weight_in_pounds / (height_in_inches ** 2) * EXACT_BMI_NUMBER
    # PROCESS
    #BMI CATEGORIES
    if the_bmi <= 16:
        your_category_is = "Severely underweight"
        calculated_bmi = 16
    elif the_bmi <= 18.5:
        your_category_is = "Underweight"
        calculated_bmi = 18.5
    elif 18.5 < the_bmi <= 25:
        your_category_is = "Healthy"
        calculated_bmi = 18.5 < the_bmi <= 25
    elif the_bmi > 25:
        your_category_is = "Overweight"
        calculated_bmi = 25
    elif 30 < the_bmi:
        your_category_is = "Obese"
        calculated_bmi = 30
        

# WEIGHT CALCULATION AS PER VALUES
if your_category_is != "Healthy":
    measured_weight = (calculated_bmi * height_in_inches ** 2) / EXACT_BMI_NUMBER


# OUTPUT
# FINAL RESULTS ACCORDING TO THE ENTERED VALUES
print("\nHere is your result:") 
print(f"Users height is: {height_in_inches} inches")
print(f"Users weight is: {weight_in_pounds} pounds")
print(f"the_bmi: {the_bmi:.1f} ({your_category_is})")

if calculated_bmi < 18.5 :
    print(f"You should gain {measured_weight:.1f} pounds to be healthy.")
else:
     print(f"You should loose {measured_weight:.1f} pounds to be healthy.")


# END OF THE CODE
input("\nPRESS ENTER TO END THE RUNNING PROGRAM.")

