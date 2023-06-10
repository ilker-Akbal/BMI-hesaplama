import tkinter

window = tkinter.Tk()
window.title("BMI Hesaplama")
window.minsize(width=200, height=150)
kg_label = tkinter.Label(text="Enter Your Weight (kg)")
kg_label.pack()
kg_entry = tkinter.Entry(width=10)
kg_entry.pack()
m_label = tkinter.Label(text="Enter Your Height (m)")
m_label.pack()
m_entry = tkinter.Entry(width=10)
m_entry.pack()
conclusion_label = tkinter.Label()


def click_button():
    try:
        kg = int(kg_entry.get())
        m = float(m_entry.get()) / 100
        BMI = kg / (m * m)
        BMI = round(BMI, 2)
        if BMI < 18.5:
            conclusion_label.config(text=f"Your BMI is {BMI} . You are weak")
            conclusion_label.pack()
        elif 18.5 < BMI < 24.9:
            conclusion_label.config(text=f"Your BMI is {BMI} . You are normal weight")
            conclusion_label.pack()
        elif 25 < BMI < 29:
            conclusion_label.config(text=f"Your BMI is {BMI} . You are overweight")
            conclusion_label.pack()
        elif BMI > 30:
            conclusion_label.config(text=f"Your BMI is {BMI} . You are obese")
            conclusion_label.pack()
    except ValueError:
        conclusion_label.config(text="Enter a valid number!")
        conclusion_label.pack()


submit_button = tkinter.Button(text="calculate", command=click_button)
submit_button.pack()
window.mainloop()
