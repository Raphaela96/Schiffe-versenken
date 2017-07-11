# -*- coding: utf-8 -*-
import Tkinter as Tk
from PIL import Image, ImageTk, ImageDraw


class SpielfeldGui(object):
    def __init__(self, root):
        self.root = root
        self.root.title("Spielfeld")
        self.root.minsize(width=500, height=500)
        # self.menubar()
        self.schachbrettmuster = Image.open("Schachbrett.png")
        self.resized_image = None
        self.draw = ImageDraw.Draw(self.schachbrettmuster)
        self.schachbrettmuster_photoimage = ImageTk.PhotoImage(self.schachbrettmuster)
        self.schachbrettmuster_image_label = Tk.Label(root,
                                                      image=self.schachbrettmuster_photoimage,
                                                      borderwidth=0,
                                                      cursor="cross")
        self.schachbrettmuster_image_label.pack(side="top", fill="both", expand=True)

    @property
    def screen_size(self):
        return self.schachbrettmuster_image_label.winfo_width(), self.schachbrettmuster_image_label.winfo_height()

    def show_image(self):
        self.resized_image = self.schachbrettmuster_image.resize(self.screen_size, Image.NEAREST)
        self.schachbrettmuster_photoimage = ImageTk.PhotoImage(self.resized_image)
        self.schachbrettmuster_image_label.config(image=self.schachbrettmuster_photoimage)

    def set_image_size(self, size):
        self.image_size = size
        self.schachbrettmuster_image = Image.new("RGB", (self.image_size[0], self.image_size[1]), "white")
        self.draw = ImageDraw.Draw(self.schachbrettmuster_image)
        self.show_image()


class EntryGui(object):
    def __init__(self, root):
        self.root = root
        self.entry = Tk.Entry(root, bd=3)
        self.entry.pack()


class InfoText(object):
    def __init__(self, root):
        self.root = root
        self.infoString = Tk.StringVar()
        self.infoText = Tk.Label(root, textvariable=self.infoString)
        self.infoString.set("Willkommen beim \"Schiffe versenken\"! Drücke Enter.")
        self.infoText.pack()

    def set_text(self, text):
        self.infoString.set(text)


def key(event):
    if event.char == '\r':
        print "pressed", repr(event.char)
        textWindow.set_text('Bitte setze ein Schiff der Länge 5.')


r = Tk.Tk()
r.bind("<Key>", key)
mainWindow = SpielfeldGui(r)
textWindow = InfoText(r) # https://www.tutorialspoint.com/python/tk_label.htm
entryWindow = EntryGui(r) # https://www.tutorialspoint.com/python/tk_entry.htm
r.mainloop()
