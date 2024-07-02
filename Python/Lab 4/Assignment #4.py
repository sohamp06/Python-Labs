# Author: Soham Patel
# File name: distance_converter.py
# Date: April 9, 2023
# Description: This is Python code using tkinter to create a form designed to convert distance from kilometer to miles and miles to kilometer.  

# Importing tkinter as tk 
import tkinter as tk

#CONSTANTS 
CONSTANT = 1.6093

# Defining clear_all functions 
def clear_all():
    #using delete function 
    entered_distance.delete(0, tk.END)
    #configuring output_message
    output_message.config(text="")
    #setting it to false
    only.set(False)

# defining function to convert the distance
def convert_distance():
    #prompt user to enter the distance 
    distance = entered_distance.get()

    #using try and except function 
    try:
        distance = float(distance)
    except ValueError:
        #print message if invalid input is entered 
        #print"Input Error"
        output_message.config(text="Input Error")
        #use return function if the condition doesn't match 
        return
 
    #using if-else statement 
    #set condition to True 
    if only.get() == True:
        #for calculating KILOMETER TO MILES 
        #output is equal to distance divided by Constant 
        output = distance / CONSTANT
        #print mile as unit
        unit = "mile"
        #configuring the output message 
        output_message.configure(text=f"{distance} kilometer is {output:.2f} {unit}")
    else:
        #for calculating  MILES TO KILOMETER
        #the output is equal to distance * Constant 
        output = distance * CONSTANT
        #print kilometer as unit 
        unit = "kilometer" 
        #configuring output message
        output_message.configure(text=f"{distance} mile is {output:.2f} {unit}")

# Creating the window form 
window = tk.Tk()
#setting up the window title as "Distance Convertor"
window.title("Distance Converter")
#Setting up the form geometry
window.geometry("650x320")
#setting width and height 
window.minsize(width=700, height=300)
#let color of the background be grey 
window.configure(bg='grey')

#Labelling the window and defining row and column number for textbox 
tk.Label(window, text="Enter Distance you want to change").grid(row=0, column=0)
#prompt user to enter the desired distance 
entered_distance = tk.Entry(window)
#setting window minimum size
window.minsize(width=20, height=30)
entered_distance.grid(row=0, column=1)

#using tk.BooleanVar function to let user enter the string 
only = tk.BooleanVar()

#Using radionbuttons to let user have a choice between kilometer and miles 
button1 = tk.Radiobutton(window, text="Kilometer to Mile", variable=only, value=True, bg='#c7ecee', fg='#2d3436').grid(row=1, column=0)

button2 = tk.Radiobutton(window, text="Mile to Kilometer", variable=only, value=False, bg='#c7ecee', fg='#2d3436').grid(row=1, column=2)

#using tk.lable to print the result 
output_message = tk.Label(window, text="")
output_message.grid(row=2, column=1)


#Using Button function 
#using Convert button to convert from kilometer/miles 
button3 = tk.Button(window, text="Convert", command=convert_distance, bg='#4cd137', fg='white').grid(row=3, column=0)
#using Reset button to clear the window 
button4 = tk.Button(window, text="Reset", command=clear_all, bg='#e84118', fg='white').grid(row=3, column=1)
#using close button to exit from the window 
button5 = tk.Button(window, text="Close", command=window.destroy, bg='#a3cb38', fg='white').grid(row=3, column=2)

# Setting grid configuration using range function 
for row_counter in range(4):
    window.rowconfigure(row_counter, weight=1)
for column_counter in range(3):
    window.columnconfigure(column_counter, weight=1)

# setting up window main loop
window.mainloop()
