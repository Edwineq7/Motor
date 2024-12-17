from tkinter import Tk, Label, Canvas, messagebox
from PIL import Image, ImageTk
from time import strftime

ventana = Tk()
ventana.geometry("800x600")
ventana.title("GUI Dirección de Motor")
ventana.iconbitmap("img/stop.jpeg")
titulo = Label(ventana, text="Control Motor", font=("Arial", 20, "bold"))
titulo.pack()


ventana.mainloop()