import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry("100x100")
yn = messagebox.askyesno('continue', "continue?")
if yn == True:
  messagebox.showinfo('yes', 'you clicked yes.')
else:
  messagebox.showinfo('you clicked no', 'you clicked no')


tk.mainloop()
