"""
Author: MustafaXD (github.com/MustafaTheCoder)
MIT License: https://opensource.org/licenses/MIT
Github: github.com/MustafaTheCoder/Math-Equation-Calculator/blob/main/main.py
"""

# Importing essential modules
import tkinter
import customtkinter

# Configuring appearance mode and color theme
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

# Defining the main app variable 
app = customtkinter.CTk()

# Defining master root and app geometry
root_tk = app.geometry("900x600")

# Defining app title
app.title("COOOL CALCULATOR | github.com/MustafaTheCoder")

# Defining app header label value
heading_label_text_var = tkinter.StringVar(value="COOOL CALCULATOR")
# Defining app header label custom font size 
heading_label_font = customtkinter.CTkFont(size=50)

# Defining the text variable (label value) and font size variable of the app header label
heading_label = customtkinter.CTkLabel(master=root_tk, textvariable=heading_label_text_var, font=heading_label_font)
# Placing the app header label in the center anchor
heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Defining app input label value
input_label_text_var = tkinter.StringVar(value="Input your equation:")
# Defining app input label custom font size
input_label_font = customtkinter.CTkFont(size=25)

# Defining the text variable (label value) and font size variable of the app input label
input_label = customtkinter.CTkLabel(master=root_tk, textvariable=input_label_text_var, font=input_label_font)
# Placing the app input label in the center anchor
input_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# Defining the main calculation function to evaluate the equation given in the input textbox by the user
def calculate_function():
    # Defining a try and exception statement
    try:
        # Getting the user input stored in a variable
        inp = input_.get()
        # Evaluating the answer of the equation that the user gave as an input and storing the value in a new variable
        calculated_answer = eval(inp)
        # Changing the value of a pre-defined label to display the answer
        answer_label.configure(text=f"Answer: {calculated_answer}")
    # This is to handle if any exceptions occur such as user entering incorrect equations
    except Exception as e:
        # Changing the value of a pre-defined label that was definied to show the answer and now it will display the error for the incorrect input instead
        answer_label.configure(text=f"[ERROR OCCURED] | {e}")

# Defining the main app input textbox that will take the equation as an input
input_ = customtkinter.CTkEntry(master=root_tk, placeholder_text="Enter equation.")
# Placing the app input textbox in the center anchor
input_.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

# Defining the main app button that will be clicked to display the answer of the entered input
button = customtkinter.CTkButton(master=app, text="Calculate", command=calculate_function)
# Placing the app main calculate button in the center anchor
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Defining app answer label custom font size 
answer_font = customtkinter.CTkFont(size=25)

# Defining the text variable (label value) and font size variable of the app answer label
answer_label = customtkinter.CTkLabel(master=root_tk, text="Answer: -", font=answer_font)
# Placing the app answer label in the center anchor
answer_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Executing the main app loop
app.mainloop()



