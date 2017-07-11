import Tkinter as Tk
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
import numpy as np


class SpielfeldGui(object):
    def __init__(self, root):
        self.root = root
        self.root.title("Spielfeld")
        self.root.minsize(width=500, height = 700)
        self.menubar()
        self.schachbrettmuster = Image.open("Schachbrett.png")
        self.resized_image = None
        self.draw = ImageDraw.Draw(self.schachbrettmuster)
        self.schachbrettmuster_photoimage = ImageTk.PhotoImage(self.schachbrettmuster)
        self.schachbrettmuster_image_label = Tk.Label(root,
                                                      image=self.schachbrettmuster_photoimage,
                                                      borderwidth=0,
                                                      cursor="cross")
        self.schachbrettmuster_image_label.bind("<ButtonPress-1>", self.mouse_down)
        self.schachbrettmuster_image_label.bind("<ButtonRelease-1>", self.mouse_up)
        self.schachbrettmuster_image_label.pack(side="top", fill="both", expand=True)
        self.mouse_x, self.mouse_y = 0, 0

    @property
    def screen_size(self):
        return self.schachbrettmuster_image_label.winfo_width(), self.schachbrettmuster_image_label.winfo_height()

    def mouse_position(self, event):
        print event.x
        print event.y

    def mouse_down(self, event):
        print event.x
        print event.y

    def mouse_up(self, event):
        print event.x
        print event.y

    def show_image(self):
        self.resized_image = self.life_image.resize(self.screen_size, Image.NEAREST)
        self.life_photoimage = ImageTk.PhotoImage(self.resized_image)
        self.life_image_label.config(image=self.life_photoimage)

    def set_image_size(self, size):
        self.image_size = size
        self.life_image = Image.new("RGB", (self.image_size[0], self.image_size[1]), "white")
        self.draw = ImageDraw.Draw(self.life_image)
        self.show_image()

    def menubar(self):
        """menu_main = Tk.Menu(self.root)
        menu_neu = Tk.Menu(menu_main, tearoff=0)
        menu_start = Tk.Menu(menu_main, tearoff=0)
        menu_options = Tk.Menu(menu_main, tearoff=0)
        menu_options.add_radiobutton(label="Klassische Regeln (Aufgabenteil a)", value=0, variable=self.rules)
        menu_options.add_radiobutton(label="Bunte Ameisen (Aufgabenteil b)", value=1, variable=self.rules)
        menu_neu.add_command(label="50x50", underline=0, command=lambda: self.set_image_size((50, 50)))
        menu_neu.add_command(label="100x100", underline=1, command=lambda: self.set_image_size((100, 100)))
        menu_neu.add_command(label="200x200", underline=1, command=lambda: self.set_image_size((200, 200)))
        menu_help = Tk.Menu(menu_main, tearoff=0)
        help_text = ("Conway's Game of Life\n"
                     "Analysieren und Visualisieren mit Python SS17\n"
                     "Informationswissenschaft\n"
                     "Uni Regensburg")
        menu_help.add_command(label="Ueber", underline=0, command=lambda: tkMessageBox.showinfo("GOL", help_text))
        menu_main.add_cascade(label="Neu", underline=0, menu=menu_neu)
        menu_main.add_cascade(label="Start", underline=0, menu=menu_start)
        menu_start.add_command(label="Start", underline=0, command=self.start)
        menu_start.add_command(label="Stop", underline=1, command=self.stop)
        menu_start.add_command(label="1 Schritt", underline=1, command=self.step)
        menu_main.add_cascade(label="Optionen", underline=0, menu=menu_options)
        menu_main.add_cascade(label="Hilfe", underline=0, menu=menu_help)
        self.root.config(menu=menu_main)"""


r = Tk.Tk()
mainWindow = SpielfeldGui(r)
r.mainloop()
