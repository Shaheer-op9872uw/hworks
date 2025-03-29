from tkinter import Tk, Label, Entry, Button, StringVar

def convert():
    try:
        meters = float(entry.get())
        result.set(f"{meters * 3.28084:.2f} Feet")
    except ValueError:
        result.set("Invalid Input")

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")
root.configure(bg="#f0f0f0")

Label(root, text="Enter Length (Meters):", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entry = Entry(root, font=("Arial", 12))
entry.pack(pady=5)

Button(root, text="Convert", font=("Arial", 12), bg="#4CAF50", fg="white", command=convert).pack(pady=10)

result = StringVar()
Label(root, textvariable=result, font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

root.mainloop()
