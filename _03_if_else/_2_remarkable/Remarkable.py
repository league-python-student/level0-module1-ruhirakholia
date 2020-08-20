from tkinter import messagebox, simpledialog, Tk
window= Tk()
window.withdraw()

input = simpledialog.askstring("Greeter", "What is your name?")
if input.lower() == "nathan":
    messagebox.showinfo("Title", " you are experienced in coding!!:) ")
if input.lower() == "leonard" :
    messagebox.showinfo( " Title ", " you are a very hard worker and a good coder!! :)")