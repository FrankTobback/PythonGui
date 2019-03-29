from Tkinter import *

from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # Creating a menu bar
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create file object
        file = Menu(menu)

        # Added "file" to our menu
        menu.add_cascade(label="File",  menu=file)

        # Option to make a new file
        file.add_command(label="New")

        # Save file
        file.add_command(label="Save")

        # Adds a command to the menu option, calling it exit ,
        # And the command it runs on the even is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # Create the edit object
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        # Added "edit" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("GUI/Goku.jpeg")
        render = ImageTk.PhotoImage(load)

        # Labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text="What up guys!")
        text.pack()

    # Exit button function

    def client_exit(self):
        exit()


root = Tk()

# size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()
