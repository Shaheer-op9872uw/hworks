from tkinter import Tk, Label, Entry, Button, StringVar
from datetime import datetime

def calculate_age():
    try:
        name = name_var.get()
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())
        birth_date = datetime(year, month, day)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result.set(f"Hello {name}, you are {age} years old.")
    except ValueError:
        result.set("Invalid Input")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#f0f0f0")

Label(root, text="Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_var = StringVar()
Entry(root, textvariable=name_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Day:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky='w')
day_var = StringVar()
Entry(root, textvariable=day_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Month:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky='w')
month_var = StringVar()
Entry(root, textvariable=month_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Year:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky='w')
year_var = StringVar()
Entry(root, textvariable=year_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5)

Button(root, text="Calculate Age", font=("Arial", 12), bg="#4CAF50", fg="white", command=calculate_age).grid(row=4, columnspan=2, pady=10)

result = StringVar()
Label(root, textvariable=result, font=("Arial", 12), bg="#f0f0f0").grid(row=5, columnspan=2, pady=10)

root.mainloop()
