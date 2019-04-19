from tkinter import Tk, Label, Button, Text

class GUI:
    def __init__(self, root):
        self.root = root 
        root.title = "GUI prog"
        
        self.label = Label(root, text="Name")
        self.label.pack()

        self.text = Text(root)
        self.text.config(width=50, height=10)
        self.text.pack()

        self.button = Button(root, text="Click Me", command=self.DisplaySomething)
        self.button.pack()

    def DisplaySomething(self):
        self.text.config(text="Clicked")
        
root = Tk()
Gui = GUI(root)
root.mainloop()

