# Python-Labs
Assignments I have done in college.
Assignment 1

Input:
1)	Enter height in inches (Must be a whole number)
2)	Enter weight in pounds (Must be a whole number)

Output:
1)	Display the user’s height.
2)	Display the user’s weight.
3)	Display the BMI of the user.
4)	Display a message according to the user’s BMI.

Process:
1)	First, user needs to enter their height and weight.
2)	Use the height value  that the user entered and store as “height in inches”.
3)	Use the weight value that the user entered and store as “weight in pounds”.
4)	The entered value will be checked and then goes further.
5)	If the value is not a whole number, it will show an error.
6)	If the value is a whole number, it will calculate the user’s BMI and then show relevant category.
7)	Use the BMI calculator formula to calculate this.
8)	BMI = (weight/height^2) * 703
9)	BMI is less than or equal to 16 then print “Severely underweight”.
10)	BMI is less or equal to 18.5 then print “Underweight”.
11)	BMI is between 18.5 to 25 or equals then print “Healthy”.
12)	BMI is greater than 25 then print “Overweight”.
13)	BMI is greater than 30 then print “Obese”.
14)	Calculate the measured weight using the formula = (calculated bmi * height in inches ** 2) / 703
15)	Display the final result.
16)	If the value is severely underweight and underweight, then it will print “You should gain weight”.
17)	If the value is overweight and obese, then it will print “You should loose weight”.
18)	Prompt the user to press enter to  end the running program.

Assignment 2


Input:
•	Ask the user to enter the diameter of the pizza.
Process:
•	User needs to enter the diameter of pizza to get the number of slices and its area.
•	Press “0” to exit the code.
•	If the user enters number out of 8 to 24, print an error message.
•	If the user enters alphabets, print an error message.
•	if input is between greater or equals to 8 and less than 12 result will be 6 slices.
•	if input is between greater or equals to 12 and less than 14 result will be 6 and 8 slices.
•	if input is between greater or equals to 14 and less than 16 result will be 6, 8 and 10 slices.
•	if input is between greater or equals to 16 and less than 20 result will be 6, 8, 10 and 12 slices.
•	if input is greater than 20 result will be 6, 8, 10, 12 and 16 slices.
•	Calculation: total_radius = diameter_of_pizza / 2
•	Calculation:  area_of_pizza = pi * total_radius ** 2
•	Calculation: possible_slices = area_of_pizza / len(pizza_slices)
•	Print number of slices 
•	Calculation: total_area_of_slice = area_of_pizza / number_of_slices
Output:
•	Print total slices with area of each slice.

Assignment 3




Input: 
-	Ask the user to get an input by pressing 1 for encryption
-	Ask the user to get an input by pressing 2 for decryption
-	Press 3 to exit
Process:
-	User needs to enter the option they would like to execute 
-	For output of Al Bhed letters, Convert English letters to Al Bhed by adding 1 letter more
-	For output of English letters, Convert AL Bhed to English by moving 1 letter back
Output: 
-	Print the encoded or decoded message 


ASSIGNMENT 4
Constant 
- CONSTANT = 1.6093
Input
- Ask the user to enter the value (kilometer or mile)
- Prompt the user to choose either kilometer to mile or mile to kilometer
Process
- User must select convert button to proceed further calculation
- User need to select reset button if they want to clear all
- User should select close button to close the distance converter 
- If the user select kilometer to mile 
• Kilometer / 1.6093
- If the user select mile to kilometer
• Mile * 1.6093
- If the user enter other than numbers print an error message
Output
- Display the converted result asked by the user
- Display error for wrong entries
