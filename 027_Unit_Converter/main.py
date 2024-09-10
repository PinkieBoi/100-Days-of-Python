import tkinter


def unit_conversion():
    value = convert_to_m(float(user_input.get()), f_units.get())
    new_val = convert_from_m(value, t_units.get())
    new_units = get_units()
    converted_val["text"] = f"{new_val} {new_units}"


def convert_to_m(value, units):
    if units == 1:
        meters = value * 1609.344
    elif units == 2:
        meters = value * 1000
    elif units == 3:
        meters = value
    elif units == 4:
        meters = value * 0.01
    elif units == 5:
        meters = value * 0.0254
    elif units == 6:
        meters = value * 149597870700
    else:
        meters = user_input.get()
    return meters


def convert_from_m(value, units):
    if units == 1:
        new_val = value / 1609.344
    elif units == 2:
        new_val = value / 1000
    elif units == 3:
        new_val = value
    elif units == 4:
        new_val = value / 0.01
    elif units == 5:
        new_val = value / 0.0254
    elif units == 6:
        new_val = value / 149597870700
    else:
        new_val = user_input.get()
    return new_val


def get_units():
    units = t_units.get()
    if units == 1:
        new_units = "Mi"
    elif units == 2:
        new_units = "Km"
    elif units == 3:
        new_units = "m"
    elif units == 4:
        new_units = "cm"
    elif units == 5:
        new_units = "in"
    elif units == 6:
        new_units = "AUs"
    else:
        new_units = "Error"
    return new_units


FONT = ("Ubuntu", 12, "normal")

win = tkinter.Tk()
win.title("Unit Converter")
win.minsize(width=200, height=300)

# Heading label
header = tkinter.Label(text="Unit Converter", font=("Ubuntu", 15, "normal"), justify="center")
header.grid(row=1, column=1, columnspan=2)

# Input box
user_input = tkinter.Entry()
user_input.grid(row=2, column=1, columnspan=2)

# From label
from_box = tkinter.LabelFrame(text="from")
from_box.grid(row=4, column=1, padx=10)

# From options
f_units = tkinter.IntVar()
f_mi = tkinter.Radiobutton(from_box, variable=f_units, value=1, text="miles", font=FONT)
f_km = tkinter.Radiobutton(from_box, variable=f_units, value=2, text="km", font=FONT)
f_m = tkinter.Radiobutton(from_box, variable=f_units, value=3, text="meters", font=FONT)
f_cm = tkinter.Radiobutton(from_box, variable=f_units, value=4, text="cm", font=FONT)
f_in = tkinter.Radiobutton(from_box, variable=f_units, value=5, text="inches", font=FONT)
f_au = tkinter.Radiobutton(from_box, variable=f_units, value=6, text="AUs", font=FONT)
f_mi.pack()
f_km.pack()
f_m.pack()
f_cm.pack()
f_in.pack()
f_au.pack()

# To label
to_box = tkinter.LabelFrame(text="to")
to_box.grid(row=4, column=2, padx=10)

# To options
t_units = tkinter.IntVar()
t_mi = tkinter.Radiobutton(to_box, variable=t_units, value=1, text="miles", font=FONT)
t_km = tkinter.Radiobutton(to_box, variable=t_units, value=2, text="km", font=FONT)
t_m = tkinter.Radiobutton(to_box, variable=t_units, value=3, text="meters", font=FONT)
t_cm = tkinter.Radiobutton(to_box, variable=t_units, value=4, text="cm", font=FONT)
t_in = tkinter.Radiobutton(to_box, variable=t_units, value=5, text="inches", font=FONT)
t_au = tkinter.Radiobutton(to_box, variable=t_units, value=6, text="AUs", font=FONT)
t_mi.pack()
t_km.pack()
t_m.pack()
t_cm.pack()
t_in.pack()
t_au.pack()


# Convert button
convert_btn = tkinter.Button(win, text="Convert", font=FONT, command=unit_conversion)
convert_btn.grid(row=11, column=1, columnspan=2)

# Output box
converted_val = tkinter.Label(win, text="", font=FONT)
converted_val.grid(row=12, column=1, columnspan=2, pady=10)

win.mainloop()
