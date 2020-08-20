from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw()

password = "coding"

input = simpledialog.askstring("Greeter", "what is your secret message?")
python = simpledialog.askstring("Greeter", "you can only see the secret message if you guess the secret password!!")
if password.lower() == python:
    messagebox.showinfo("Title", input )
else :
    messagebox.showinfo("Title", " you guessed wrong try again!:( ")
