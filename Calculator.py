from tkinter import *
from tkinter import messagebox
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Math error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Operation error", "Please select a valid operation")
            return
        entry3.delete(0, END)
        entry3.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")
window = Tk()
window.title('Simple Calculator')
window.geometry('450x500')
Label(window, text='Calculator', font=('Arial', 25)).place(x=135, y=40)
Label(window, text='Type value1', font=('Arial', 15)).place(x=60, y=100)
Label(window, text='Type value2', font=('Arial', 15)).place(x=60, y=135)
Label(window, text='Operation', font=('Arial', 15)).place(x=60, y=170)
Label(window, text='Result', font=('Arial', 15)).place(x=120, y=250)
entry1 = Entry(window)
entry1.place(x=190, y=105, height=20, width=120)
entry2 = Entry(window)
entry2.place(x=190, y=140, height=20, width=120)
entry3 = Entry(window)
entry3.place(x=190, y=255, height=20, width=120)
operation_var = StringVar(window)
operation_var.set("Select Operation")  # default value
operations_menu = OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.place(x=190, y=170, height=30, width=120)
Button(window, text='Calculate', bg='green', fg='white', font=('Arial', 14), command=calculate).place(x=190, y=200, height=30, width=120)
window.mainloop()