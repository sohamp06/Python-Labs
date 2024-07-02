# PROGRAM NAME: iteration_pizza
# PROGRAM AUTHOR: SOHAM PATEL
# DATE: 05-03-2023
# PROGRAM DESCRIPTION: Calcuation of slices and its area by entering pizza diameter


# variable
diameter_of_pizza = 0

pi = 3.14

# while loop
while True:
    try:
        valid = True
        # ask the user to enter the diameter of pizza or to press "0" to endd the program
        diameter_of_pizza = float(input("Please enter the diameter of your pizza (Press 0 to end program):"))
        # to end the running program
        if diameter_of_pizza == 0:
         
         break
        # invalid input. pizza  should be between the range of 8" to 24"
        if 8 > diameter_of_pizza or diameter_of_pizza > 24:
         print('"Wrong entry!" \n Pizza must have a diameter in the range of 8” to 24” inclusive. \nTry again.')
         continue
        # if input is between greater or equals to 8 and less than 12
        elif 8>= diameter_of_pizza <12:
            # result of possible slices
            pizza_slices = [6]
        # if input is between greater or equals to 12 and less than 14
        elif 12>= diameter_of_pizza <14:
             # result of possible slices
            pizza_slices = [6, 8]
        # if input is between greater or equals to 14 and less than 16
        elif 14>= diameter_of_pizza <16:
             # result of possible slices
            pizza_slices = [6, 8, 10]
        # if input is between greater or equals to 16 and less than 20
        elif 16>= diameter_of_pizza <20:
             # result of possible slices
            pizza_slices = [6, 8, 10, 12]
        # if input is greater than 20
        else:
             # result of possible slices
            pizza_slices = [6, 8, 10, 12, 16]
# calculation to get total radius 
        total_radius = diameter_of_pizza / 2
# calculation to get area of the pizza
        area_of_pizza = pi * total_radius ** 2
# calculation to get the result of slices
        possible_slices = area_of_pizza / len(pizza_slices)
# display the number of slices
        print(f'\n Slices of {diameter_of_pizza}" pizza:')


        for number_of_slices in pizza_slices:
# calculation to get the area of a single slice
           total_area_of_slice = area_of_pizza / number_of_slices
        # display the final result with area of slices and number of possible slices
           print(f'{number_of_slices} slices and per slice is of {round(total_area_of_slice, 2)} square inches')
    except ValueError:
#invalid input. Input must be numeric value.
        print('"Entry error!" \n Input must be numeric value. ')





# DESK CHECK 1
# Please enter the diameter of your pizza (Press 0 to end program): 21
# Slices of 21.0" pizza:
# 6 slices and per slice is of 57.7 square inches
# 8 slices and per slice is of 43.27 square inches
# 10 slices and per slice is of 34.62 square inches
# 12 slices and per slice is of 28.85 square inches
# 16 slices and per slice is of 21.64 square inches


# DESK CHECK 2
# Please enter the diameter of your pizza (Press 0 to end program): 6
# "Wrong entry!"
#  Pizza must have a diameter in the range of 8” to 24” inclusive.
# Try again.


# DESK CHECK 3
# Please enter the diameter of your pizza (Press 0 to end program): XYZ
# "Entry error!"
#  Input must be numeric value.


# DESK CHECK 4
# Please enter the diameter of your pizza (Press 0 to end program): 14.2
#  Slices of 14.2" pizza:
# 6 slices and per slice is of 26.38 square inches
# 8 slices and per slice is of 19.79 square inches
# 10 slices and per slice is of 15.83 square inches
# 12 slices and per slice is of 13.19 square inches


# DESK CHECK 5
# Please enter the diameter of your pizza (Press 0 to end program): 432984
# "Wrong entry!"
#  Pizza must have a diameter in the range of 8” to 24” inclusive.
# Try again.