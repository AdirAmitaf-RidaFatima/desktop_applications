import tkinter as tk
from tkinter import ttk

# -------------------------------
# Create the main window
# -------------------------------
window = tk.Tk()
window.title("🎨 Tkinter Drawing & Widgets Cheat Sheet")
window.geometry("1000x700")
window.config(bg="white")

# -------------------------------
# VARIABLES using StringVar and IntVar
# -------------------------------
color_var = tk.StringVar(value="Black")     # For brush color
size_var = tk.IntVar(value=5)               # For brush size

# -------------------------------
# 1. Combobox (Dropdown for Color selection)
# -------------------------------
ttk.Label(window, text="Select Brush Color:").pack()
color_picker = ttk.Combobox(
    window, textvariable=color_var, values=[
        "Black", "Red", "Blue", "Green", "Yellow", "White"
    ]
)
color_picker.pack()

# -------------------------------
# 2. Spinbox (For Brush Size)
# -------------------------------
ttk.Label(window, text="Select Brush Size:").pack()
size_picker = tk.Spinbox(window, from_=1, to=50, textvariable=size_var)
size_picker.pack()

# -------------------------------
# 3. Canvas Widget (Main drawing area)
# -------------------------------
canvas = tk.Canvas(window, bg="white", width=900, height=500)
canvas.pack(pady=20)

# -------------------------------
# 4. Drawing Logic (Mouse events)
# -------------------------------
# Store coordinates for drawing
last_x, last_y = None, None

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y  # Starting point of drawing

def draw(event):
    global last_x, last_y
    brush_color = color_var.get()
    brush_size = size_var.get()
    canvas.create_line(last_x, last_y, event.x, event.y,
                       fill=brush_color, width=brush_size,
                       capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y  # Update new starting point

# Bind mouse events to the canvas
canvas.bind("<Button-1>", start_draw)    # Mouse click
canvas.bind("<B1-Motion>", draw)         # Mouse drag with left button

# -------------------------------
# 5. Extra Functions
# -------------------------------
def clear_canvas():
    canvas.delete("all")  # Wipes the entire canvas

def use_eraser():
    color_var.set("White")  # Set brush color to background color

def draw_circle():
    # Draws a sample circle using canvas method
    canvas.create_oval(100, 100, 200, 200, outline=color_var.get(), width=2)

# Buttons for Clear, Eraser, Circle
ttk.Button(window, text="Clear Canvas", command=clear_canvas).pack(pady=5)
ttk.Button(window, text="Use Eraser", command=use_eraser).pack(pady=5)
ttk.Button(window, text="Draw Circle (Static)", command=draw_circle).pack(pady=5)

# -------------------------------
# Run the Application
# -------------------------------
window.mainloop()
