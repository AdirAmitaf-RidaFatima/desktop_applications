import tkinter as tk
from tkinter import ttk

# Create the main application window
window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("300x150")

#title - 1st Frame
title_label = ttk.Label(master = window, text="Miles to Kilometers Converter", font="Calibri 24 bold")
title_label.pack()

#Function for conversion
def convert_miles_to_kilometers():
    mile_input=entryInt.get()
    kilometer_output = mile_input * 1.60934
    output_string.set(f"{kilometer_output:.2f} km")

# Input field for miles - 2nd Frame (2 widgets in it)
input_frame = ttk.Label(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
button =ttk.Button(master=input_frame, text="Convert", command=convert_miles_to_kilometers)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)


#output frame/Widget
output_string = tk.StringVar()
output_label=ttk.Label(master=window, text="Kilometers: ", font=("Calibri 14"), textvariable=output_string)
output_label.pack(pady=10)

# Run the application
window.mainloop()
