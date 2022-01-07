from tkinter import *
from tkinter import filedialog
from fileFormatter import FileFormatter

formatter = FileFormatter()


def openfile():
    formatter.open_file(filedialog.askopenfilename())
    Label(root, text=formatter.file_path).grid(row=0, column=1)


def format_file():
    formatter.format_file()


# Screen configuration
root = Tk(className="File Formatter")
root.geometry("400x100")

# Elements
Label(root, text="File Name:").grid(row=1, column=0)
Label(root, text="Choose a File").grid(row=1, column=1)
Button(text="input file", command=openfile, padx=50).grid(row=2, column=0)
Button(text="format file", command=format_file, padx=50).grid(row=3, column=0)

root.mainloop()
