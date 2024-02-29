"""_summary_
A simple program to demo how to run GUI
"""

# Importing librabries
import tkinter
import customtkinter
import imgResize
from tkinter import messagebox
import imgThreshold

"""_summary_
Initializing system settings
"""
# Set to dark mode
customtkinter.set_appearance_mode("dark")

# Set deafult color for button
customtkinter.set_default_color_theme("dark-blue")

"""_summary_
Show the actual window
"""
app = customtkinter.CTk()

# Set the size and title of the window
app.geometry("860x480")
app.title("IPR_Assignment 1_Resize Image")

"""_summary_
Add UI elements
"""
title1 = customtkinter.CTkLabel(app, text="Enter width and height")
title1.pack(ipadx=10, ipady=10)

"""_summary_
Add two box to enter width and height
See image_resize() function
"""
# Initialzing a height variable
height_var = tkinter.StringVar()
height = customtkinter.CTkEntry(app, width=500, height=50, border_color="red",
                                textvariable=height_var, placeholder_text="Enter the height you want:")
height.pack(padx=10, pady=10)

# Initalizing a width variable
width_var = tkinter.StringVar()
width = customtkinter.CTkEntry(app, width=500, height=50, border_color="blue",
                               textvariable=width_var, placeholder_text="Enter the width you want: ")
width.pack(padx=10, pady=10)

title2 = customtkinter.CTkLabel(
    app, text="Enter a threshold value between 0 and 255")
title2.pack(ipadx=10, ipady=10)
threshold_from_user = tkinter.StringVar()
threshold = customtkinter.CTkEntry(
    app, width=100, height=50, border_color="#d6e9ff", textvariable=threshold_from_user)
threshold.pack(padx=15, pady=15)
# A function to handle the resize function (by calling )

def handle_threshold_value():
    # Accept input from the entry box
    input_threshold = int(threshold.get())

    # Raising exception if the number is smaller than 0
    if (input_threshold < 0):
        messagebox.showerror(
            'Python Error', "Threshold value can not be negative!")

    # Raising another exception if the number is bigger than 255
    if (input_threshold > 255):
        messagebox.showerror(
            'Python Error', "Threshold value is larger than 255")

    # Call function from back end:
    # Args accepted (in order of agrs: original image, threshold )
    imgThreshold.make_photo_binary(input_threshold, filepath)


def handle_resize():
    desired_height = int(height.get())
    desired_width = int(width.get())
    path_from_user = filepath
    imgResize.image_resize(desired_height, desired_width, path_from_user)

def handle():
    handle_resize()
    handle_threshold_value()
"""_summary_
Add a button to resize image
"""
button = customtkinter.CTkButton(
    master=app, text="Process Image", command=handle)
button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


def handle_path_input():
    from customtkinter import filedialog

    # Set to global (in lieu of .get() from box input)
    global filepath

    # Specify what kind of file is accepted
    filepath = filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[
            ("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif")
        ]
    )


    # Remember to modify the code at back end to take into account the filepath:
# Sample code to add another button:
button = customtkinter.CTkButton(
    master=app, text="Select Image", command=handle_path_input)
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
