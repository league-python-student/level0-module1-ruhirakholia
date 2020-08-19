from tkinter import messagebox, simpledialog, Tk
window= Tk()
window.withdraw()

input = simpledialog.askstring("Greeter", "What is your birthday?")
if input == "08/19":
    messagebox.showinfo("Title", " happy birthday!!:) ")
else:
    messagebox.showinfo("Title", " merry unbirthday:( ")