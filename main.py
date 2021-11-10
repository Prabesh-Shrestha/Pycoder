from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import sys

Window = Tk()
Window.title("Pycoder")
font = ("Comic Sans MS", 16)
fontcolor = "black"
fontback = "gray"


try:
    FilePath = sys.argv[1]
except:
    FilePath = ""


def prompt(message):
    messagewiddow = Toplevel()
    messagewiddow.geometry("250x50")
    Label(messagewiddow, text = message).pack()


def save():
    with open(FilePath, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)


def saveas():
    global FilePath
    FilePath = asksaveasfilename(filetype = [("Python File", "*.py")])
    with open(FilePath, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)


def openfile():
    global FilePath
    FilePath = askopenfilename(filetype = (("Python File", "*.py"),))
    with open(FilePath, "r") as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)

  
def runcode():
    if FilePath == "":
        prompt("file not saved")
        return
    com = f'python {FilePath}'
    process = subprocess.Popen(com, stdout= subprocess.PIPE,  stderr= subprocess.PIPE, shell=True) 
    output, error = process.communicate()
    ConsoleOut.insert("1.0", output)
    ConsoleOut.insert("1.0", error)

MainBar = Menu(Window)

# file menu
FileBar = Menu(MainBar, tearoff = 0)
FileBar.add_command(label = "Open", command = openfile)
FileBar.add_command(label = "Save", command = save)
FileBar.add_command(label = "Save As", command = saveas)
FileBar.add_command(label = "Exit", command = exit)
MainBar.add_cascade(label ="File", menu = FileBar)

# run menu
runBar = Menu(MainBar, tearoff = 0)
runBar.add_command(label = "Run", command = runcode)
MainBar.add_cascade(label ="Run", menu = runBar)

Window.config(menu=MainBar)



editor = Text(height = 10,bg=fontback, fg = fontcolor)
editor.grid(row=0, column = 0)
editor.configure(font = font)


ConsoleOut = Text(height = 7,bg=fontback, fg = fontcolor)
ConsoleOut.grid(row=1, column =0)
ConsoleOut.configure(font = font)

Window.mainloop()
