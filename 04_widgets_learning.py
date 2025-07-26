import tkinter as tk
from tkinter import ttk

# -------------------------------
# Create the main window
# -------------------------------
window = tk.Tk()  # You can also name it 'root' or 'app'
window.title("Tkinter Widgets Cheatsheet")
window.geometry("800x600")  # Width x Height

# -------------------------------
# 1. Label (for displaying text)
# -------------------------------
label = tk.Label(
    master=window, 
    text="📌 Label: Hello, Tkinter!", 
    font=("Arial", 20), 
    fg="blue"  # Font color
)
label.pack(pady=10)

# -------------------------------
# 2. Text Widget (multiline input)
# -------------------------------
text_widget = tk.Text(master=window, height=5, width=50)
text_widget.pack()
text_widget.insert(tk.END, "You can write multiple lines here...")

# -------------------------------
# 3. Entry (single-line input)
# -------------------------------
entry_label = tk.Label(window, text="Enter your name:")
entry_label.pack()
entry = tk.Entry(master=window, width=30)
entry.pack()

# -------------------------------
# 4. Button (triggers a function)
# -------------------------------
def say_hello():
    user_input = entry.get()
    output_label.config(text=f"Hello, {user_input}!")

button = tk.Button(master=window, text="Greet Me", command=say_hello)
button.pack(pady=5)

output_label = tk.Label(window, text="", font=("Arial", 14))
output_label.pack()

# -------------------------------
# 5. StringVar (bind value to a widget)
# -------------------------------
name_var = tk.StringVar()
name_var.set("Type your message...")  # Default text

entry2 = tk.Entry(master=window, textvariable=name_var)
entry2.pack()

def show_stringvar():
    print("StringVar contains:", name_var.get())

tk.Button(master=window, text="Print StringVar", command=show_stringvar).pack(pady=5)

# -------------------------------
# 6. IntVar (bind integer to widget)
# -------------------------------
int_var = tk.IntVar()

def show_scale_value(value):
    int_var.set(int(float(value)))  # update int_var
    scale_value_label.config(text=f"Slider Value: {int_var.get()}")

scale = tk.Scale(window, from_=0, to=100, orient='horizontal', command=show_scale_value)
scale.pack()
scale_value_label = tk.Label(window, text="Slider Value: 0")
scale_value_label.pack()

# -------------------------------
# 7. Radiobuttons (single choice)
# -------------------------------
radio_var = tk.StringVar(value="Python")

tk.Label(window, text="Choose your language:").pack()
languages = ["Python", "JavaScript", "C++"]
for lang in languages:
    tk.Radiobutton(window, text=lang, variable=radio_var, value=lang).pack()

def print_radio_choice():
    print("Selected language:", radio_var.get())

tk.Button(window, text="Print Selected Language", command=print_radio_choice).pack(pady=5)

# -------------------------------
# 8. Checkbuttons (multiple selections)
# -------------------------------
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()

tk.Label(window, text="Select your skills:").pack()
tk.Checkbutton(window, text="Problem Solving", variable=check_var1).pack()
tk.Checkbutton(window, text="Teamwork", variable=check_var2).pack()

def print_checkbox_choices():
    print("Problem Solving:", check_var1.get())
    print("Teamwork:", check_var2.get())

tk.Button(window, text="Print Selected Skills", command=print_checkbox_choices).pack(pady=5)

# -------------------------------
# 9. Combobox (dropdown menu)
# -------------------------------
tk.Label(window, text="Select your country:").pack()
countries = ["Pakistan", "India", "USA", "Germany"]
country_var = tk.StringVar()
combo = ttk.Combobox(window, values=countries, textvariable=country_var)
combo.pack()
combo.current(0)

def print_country():
    print("Selected Country:", country_var.get())

ttk.Button(window, text="Print Country", command=print_country).pack(pady=5)

# -------------------------------
# Main Event Loop
# -------------------------------
window.mainloop()
