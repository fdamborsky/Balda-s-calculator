import customtkinter
from tkinter import *
from PIL import Image,ImageTk
import pywinstyles,pywinstyles

# MASTER
width = 300
height = 600
window = customtkinter.CTk(fg_color="#161616")
window.geometry(f"{width}x{height}")
window.resizable(False,False)
window.title("Calculator")
window.iconbitmap("images/icon.ico")

back_image = customtkinter.CTkImage(Image.open("images/back.png"),size=(25,25))

bg = customtkinter.CTkImage(Image.open("images/bg.jpg"),size=(300,600))
bg_label = customtkinter.CTkLabel(window, 
            image=bg,
            width=300,
            height=600,
            text="")
bg_label.place(x=0,y=0)

# FUNCTIONS
first_number = ""
symbol = ""
second_number = ""
result = ""
secondnumber_on_off = False
symbol_pick_allowed = False

def add_to_number(sth):
    global first_number, second_number,symbol_pick_allowed
    result = ""
    result_label.configure(text=result)
    if secondnumber_on_off == True:
        second_number += str(sth)
        numbers2_label.configure(text = second_number)
        symbol_pick_allowed = False

    else:
        first_number += str(sth)
        numbers1_label.configure(text = first_number)
        symbol_pick_allowed = True


def symbol_picker(sth):
    global symbol,secondnumber_on_off,first_number
    if symbol_pick_allowed == True or first_number != "":
        symbol = ""
        symbol += str(sth)
        symbol_label.configure(text = symbol)
        secondnumber_on_off = True
    if sth == "-" and first_number == "" and result == "":
        first_number += str(sth)
        result == ""
        result_label.configure(text=result)
        numbers1_label.configure(text = first_number)

def equals():
    global result,first_number,symbol,second_number,secondnumber_on_off,symbol_pick_allowed

    str_numbers = first_number+symbol+second_number
    result = eval(str_numbers)
    result = round(result, 5)
    numbers1_label.configure(text=result)

    symbol = ""
    second_number = ""
    numbers2_label.configure(text = second_number)
    symbol_label.configure(text = symbol)
    secondnumber_on_off = False

def percentage(result):
    global secondnumber_on_off,symbol_pick_allowed
    if result != "":
        result = result/100
        first_number = ""
        symbol = ""
        second_number = ""
        result_label.configure(text=result)
        numbers2_label.configure(text = second_number)
        numbers1_label.configure(text = first_number)
        symbol_label.configure(text = symbol)
        secondnumber_on_off = False
        symbol_pick_allowed = False

def back():
    global second_number,first_number,symbol_pick_allowed
    if secondnumber_on_off == True:
        second_number = second_number[:-1]
        numbers2_label.configure(text = second_number)
    else:
        first_number = first_number[:-1]
        numbers1_label.configure(text = first_number)
        if first_number == "":
            symbol_pick_allowed = False

def clear_entry():
    global second_number,first_number
    if secondnumber_on_off == True:
        second_number = ""
        numbers2_label.configure(text = second_number)
    else: 
        first_number = ""
        numbers1_label.configure(text = first_number)

def clear():
    global symbol_pick_allowed,secondnumber_on_off,first_number,second_number,symbol
    first_number = ""
    numbers1_label.configure(text = first_number)
    second_number = ""
    numbers2_label.configure(text = second_number)
    symbol = ""
    symbol_label.configure(text = symbol)
    symbol_pick_allowed = False
    secondnumber_on_off = False

# LABELS
# - NUMBERS
numbers1_label = customtkinter.CTkLabel(bg_label,
                font=("Helvetica",65,"bold"),
                text=first_number,
                width=300,
                justify = "center",
                text_color="#D2D6D9",
                fg_color="#000000",
                bg_color="#000000")
pywinstyles.set_opacity(numbers1_label,color="#000000")
numbers1_label.place(x=0,y=10)

symbol_label = customtkinter.CTkLabel(bg_label,
                font=("Helvetica",65,"bold"),
                text=symbol,
                width=300,
                justify = "center",
                text_color="#D2D6D9",
                bg_color="#000000")
pywinstyles.set_opacity(symbol_label,color="#000000")
symbol_label.place(x=0,y=80)

numbers2_label = customtkinter.CTkLabel(bg_label,
                font=("Helvetica",65,"bold"),
                text=second_number,
                width=300,
                justify = "center",
                text_color="#D2D6D9",
                bg_color="#000000")
pywinstyles.set_opacity(numbers2_label,color="#000000")
numbers2_label.place(x=0,y=150)

result_label = customtkinter.CTkLabel(bg_label,
                font=("Helvetica",65,"bold"),
                text=result,
                width=300,
                justify = "center",
                text_color="#D2D6D9",
                bg_color="#000000")
pywinstyles.set_opacity(result_label,color="#000000")
result_label.place(x=0,y=80)


# BUTTONS
percent_button = customtkinter.CTkButton(master=window,
                command=lambda: percentage(result),
                fg_color="#2b116c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="%",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10)
pywinstyles.set_opacity(percent_button,color="#35138c")
percent_button.place(x=15,y=269)

clearentry_button = customtkinter.CTkButton(master=window,
                command=clear_entry,
                fg_color="#2b116c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="CE",
                font=("Helvetica",20,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(clearentry_button,color="#35138c")
clearentry_button.place(x=85,y=269)

clear_button = customtkinter.CTkButton(master=window,
                command=clear,
                fg_color="#2b116c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="C",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(clear_button,color="#35138c")
clear_button.place(x=155,y=269)

back_button = customtkinter.CTkButton(master=window,
                command=lambda: back(),
                fg_color="#2b116c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="",
                image=back_image,
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(back_button,color="#35138c")
back_button.place(x=225,y=269)

seven_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(7),                     
                fg_color="#281065",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="7",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(seven_button,color="#35138c")
seven_button.place(x=15,y=333)

eight_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(8),
                fg_color="#281065",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="8",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(eight_button,color="#35138c")
eight_button.place(x=85,y=333)

nine_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(9),
                fg_color="#281065",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="9",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(nine_button,color="#35138c")
nine_button.place(x=155,y=333)

division_button = customtkinter.CTkButton(master=window,
                command=lambda: symbol_picker("/"),
                fg_color="#281065",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="÷",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(division_button,color="#35138c")
division_button.place(x=225,y=333)

four_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(4),
                fg_color="#25105c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="4",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(four_button,color="#35138c")
four_button.place(x=15,y=397)

five_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(5),
                fg_color="#25105c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="5",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(five_button,color="#35138c")
five_button.place(x=85,y=397)

six_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(6),
                fg_color="#25105c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="6",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(six_button,color="#35138c")
six_button.place(x=155,y=397)

multiply_button = customtkinter.CTkButton(master=window,
                command=lambda: symbol_picker("*"),
                fg_color="#25105c",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="*",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(multiply_button,color="#35138c")
multiply_button.place(x=225,y=397)

one_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(1),
                fg_color="#220e54",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="1",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(one_button,color="#35138c")
one_button.place(x=15,y=461)

two_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(2),
                fg_color="#220e54",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="2",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(two_button,color="#35138c")
two_button.place(x=85,y=461)

three_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(3),                                      
                fg_color="#220e54",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="3",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(three_button,color="#35138c")
three_button.place(x=155,y=461)

minus_button = customtkinter.CTkButton(master=window,
                command=lambda: symbol_picker("-"),
                fg_color="#220e54",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="-",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(minus_button,color="#35138c")
minus_button.place(x=225,y=461)

zero_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number(0),                                     
                fg_color="#1e0d49",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="0",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(zero_button,color="#35138c")
zero_button.place(x=15,y=525)

comma_button = customtkinter.CTkButton(master=window,
                command=lambda: add_to_number("."),
                fg_color="#1e0d49",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text=",",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(comma_button,color="#35138c")
comma_button.place(x=85,y=525)

count_button = customtkinter.CTkButton(master=window,
                command=equals,
                fg_color="#1e0d49",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="=",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(count_button,color="#35138c")
count_button.place(x=155,y=525)

plus_button = customtkinter.CTkButton(master=window,
                command=lambda: symbol_picker("+"),
                fg_color="#1e0d49",
                bg_color="#35138c",
                hover_color="#1e0c4c",
                text="+",
                font=("Helvetica",30,"bold"),
                width=50,
                height=50,
                corner_radius=10,)
pywinstyles.set_opacity(plus_button,color="#35138c")
plus_button.place(x=225,y=525)

# INICIALISATION
window.mainloop()