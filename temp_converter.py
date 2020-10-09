import tkinter as tk

def fahrenheitToCelsius():
    """convert farenheit to celsius and input it to lbl_result
    """
    fahrenheit = ent_temp.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# setup the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# create the fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temp = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature entry and label in frm_entry
# using the .grid() geometry manager
ent_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# create conversion button and result display label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheitToCelsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# setup the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# run the application
window.mainloop()
