import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=450)

topic1 = tkinter.Label(text="BMI Calculator",font=("Arial",15,"normal"))
topic1.pack(pady=(0,50))

topic2 = tkinter.Label(text="Enter your height in meters",font=("Arial",15,"normal"))
topic2.pack()
input_1 = tkinter.Entry(width=50)
input_1.pack(pady=(0,50))

topic3 = tkinter.Label(text="Enter your weight in kilograms",font=("Arial",15,"normal"))
topic3.pack()
input_2 = tkinter.Entry(width=50)
input_2.pack(pady=(0,50))


def Calculator():

    try:
        height = float(input_1.get())
        weight = float(input_2.get())
        BMI = weight/(height)**2

        if height <= 0 or weight <= 0:
            print_label.config(text="Please enter valid numbers!")
        elif BMI < 18.5:
            print_label.config(text="Under the ideal weight!")
        elif 18.5 <= BMI < 24.9:
            print_label.config(text="Ideal Weight :)")
        elif 24.9 <= BMI < 29.9:
            print_label.config(text="Above the ıdeal weight!")
        elif 29.9 <= BMI < 39.9:
            print_label.config(text="Way Above the ideal weight!(Obez)")
        else:
            print_label.config(text="Way more above the ideal weight!!!(Morbid Obez)")
    except ValueError:
        print_label.config(text="Please enter valid number!")


calculate_button = tkinter.Button(text= "Calculate", command=Calculator)
calculate_button.pack(pady=(0,50))

print_label = tkinter.Label()
print_label.pack()

window.mainloop()


