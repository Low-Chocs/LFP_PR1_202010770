from tkinter import filedialog

def cargarData():
    prueba=filedialog.askopenfilename(title="Select A file")
    print(prueba)