from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=600, height=500)
window.config(padx=50, pady=50)

# Entry
miles_input = Entry(width=20)
miles_input.insert(END, string="0")
miles_input.grid(column=3, row=2)
miles_input.get()

# label
label1 = Label(text="Miles")
label1.grid(column=4, row=2)

label2 = Label(text="is equal to")
label2.grid(column=2, row=3)

label3 = Label(text="0")
label3.grid(column=3, row=3)

label4 = Label(text="Km")
label4.grid(column=4, row=3)


# Button Listening
def button_response():
    input_text = float(miles_input.get()) * 1.60934
    label3.config(text=input_text)



# Button
button = Button(text="Calculate", command=button_response)
button.grid(column=3, row=4)

window.mainloop()
