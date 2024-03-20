from tkinter import *
def decimal_to_binary(value):
    converted_value = []
    values = []
    while value != 0:
        remainder = int(value) % 2
        converted_value.append(str(remainder))
        value = int(value) // 2

    converted_value.reverse()
    for i in converted_value:
        values.append(i)
        # strips out list brackets and commas to output the number by itself
        binary_number = f"{values}".replace('[', '').replace(']', '').replace(',', '').replace("'", '')

    return binary_number



def convert():

    ascii_value = []

    try:
        value = int(input.get())
        binary_number = decimal_to_binary(value)

        oct_number = oct(value)
        binary_display = Label(window, text=f"{binary_number}").grid(column=300, row=500)
        oct_display = Label(window, text=f"{oct_number}").grid(column=300, row=300)
        hexa_decimal = Label(window, text = f"{hex(value)}").grid(column = 300, row = 400)


    except ValueError:

        value = input.get()
        for i in list(value):
            new_value = ord(i)
            ascii_value.append(new_value)
            ascii_value.reverse()
        for i in ascii_value:
            final_value = decimal_to_binary(i)
            oct_value = oct(i)
            hexa_value = hex(i)
            display_ascii = Label(window, text =f"{i}").grid(column = 300 + i, row = 200)
            binary_display = Label(window, text=f"{final_value}").grid(column=300 + i, row=500)
            oct_display = Label(window, text=f"{oct_value}").grid(column=300 + i, row=300)
            hexa_decimal = Label(window, text=f"{hexa_value}").grid(column=300 + i, row=400)



window = Tk()
window.geometry('400x400')

input = Entry(window, textvariable='decimal')
input.grid(row = 200, column =100)

R3 = Checkbutton(window, text="convert",  command=convert)
R3.grid(column = 100, row = 400)

display_binary = Label(window, text=f"binary: ").grid(column=200, row=500)
display_hexadecimal = Label(window, text=f"hexadecimal: ").grid(column=200, row=400)
display_octal = Label(window, text=f"octal: ").grid(column=200, row=300)
display_ascii = Label(window, text=f"ascii: ").grid(column=200, row=200)



window.mainloop()