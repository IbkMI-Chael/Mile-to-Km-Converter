from tkinter import *


def convert():
	"""Converts miles to kilometre"""
	km = float(miles_input.get()) * 1.609  # Get entry input, convert to int and multiply
	km_result.config(text = f"{km}")


# Creating window
window = Tk()
window.minsize(width = 300, height = 150)  # Specifying window size
window.title("Mile to Km Converter")  # Window title
window.config(padx = 20, pady = 20)  # Specifying padding

# Entry
miles_input = Entry(width = 15)
miles_input.grid(column = 1, row = 0)

# Labels
miles_label = Label(text = "Miles", font = ("arial", 15, "bold"))
miles_label.grid(row = 0, column = 2)
is_equal_label = Label(text = "is equal to", font = ("arial", 15, "bold"))
is_equal_label.grid(column = 0, row = 1)
km_result = Label(text = 0, font = ("arial", 15, "bold"))
km_result.grid(column = 1, row = 1)
km_label = Label(text = "Km", font = ("arial", 15, "bold"))
km_label.grid(column = 2, row = 1)

# Button
button = Button(text = "Calculate", command = convert)
button.grid(column = 1, row = 2)

##
##
##
window.mainloop()
