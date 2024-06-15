# pip install qrcode pillow

# Importing the modules...

import qrcode, PIL #pillow ==PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# GUI Code ....

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x380")  # Use "x" instead of "×"
root.config(bg="white")
root.resizable(0,0)



root.mainloop()