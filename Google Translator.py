from tkinter import *
from tkinter import ttk,messagebox
import googletrans 
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

#icon
try:
    image_icon = PhotoImage(file=r"C:\Users\Lenovo\Desktop\Google Translator\google.png")
    label = Label(root, image=image_icon)
    label.pack()
except Exception as e:
    print("Error loading the image:", e)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combol = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combol.place(x=110,y=20)
combol.set("ENGLISH")

root.configure(bg="white")
root.mainloop()