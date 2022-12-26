"""
Author: MustafaXD (github.com/MustafaTheCoder)
MIT License: https://opensource.org/licenses/MIT
Github: github.com/MustafaTheCoder
"""

import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
root_tk = app.geometry("900x600")
app.title("COOOL CALCULATOR | github.com/MustafaTheCoder")

heading_label_text_var = tkinter.StringVar(value="COOOL CALCULATOR")
heading_label_font = customtkinter.CTkFont(size=50)

heading_label = customtkinter.CTkLabel(master=root_tk, textvariable=heading_label_text_var, font=heading_label_font)
heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

input_label_text_var = tkinter.StringVar(value="Input your equation:")
input_label_font = customtkinter.CTkFont(size=25)

input_label = customtkinter.CTkLabel(master=root_tk, textvariable=input_label_text_var, font=input_label_font)
input_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

def calculate_function():
    try:
        inp = input_.get()
        calculated_answer = eval(inp)
        answer_label.configure(text=f"Answer: {calculated_answer}")
    except Exception as e:
        answer_label.configure(text=f"[ERROR OCCURED] | {e}")

input_ = customtkinter.CTkEntry(master=root_tk, placeholder_text="Enter equation.")
input_.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Calculate", command=calculate_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

answer_font = customtkinter.CTkFont(size=25)

answer_label = customtkinter.CTkLabel(master=root_tk, text="Answer: -", font=answer_font)
answer_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


app.mainloop()



