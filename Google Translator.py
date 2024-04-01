from tkinter import *
from tkinter import ttk,messagebox
import googletrans 
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

#icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False,image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combol = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combol.place(x=110,y=20)
combol.set("ENGLISH")

root.configure(bg="white")
root.mainloop()