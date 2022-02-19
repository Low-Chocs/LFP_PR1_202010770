from tkinter import N, filedialog
from cargarData import spelling
import re

instructionList = []
instructionDiccionary={}

def cargarInstrucciones():
    instructionList.clear()
    prueba = filedialog.askopenfilename(title="Select A file")
    with open(prueba, "r") as archivo:
        ver = archivo.read()
        ver = ver.lower()
        print(ver)
        archivo.close()
    analizar(ver)
    return instructionDiccionary


def analizar(text):
    name=""
    graph=""
    title=""
    titleX=""
    titleY=""

    try:
        nombreInstruccion= re.search("nombre:",text)
        for char in range(nombreInstruccion.end(),len(text)):
            if text[char]=="," or text[char]=="?":
                instructionDiccionary["Nombre"]=spelling(name)
                break
            if text[char]!="\"" and text[char]!=" " and text[char]!="\n":
                name+=text[char]
    except:
        print("El nombre no fue ingresado") 

    try:
        nombreInstruccion= re.search("grafica:",text)
        for char in range(nombreInstruccion.end(),len(text)):
            if text[char]=="," or text[char]=="?":
                instructionDiccionary["Grafica"]=spelling(graph)
                break
            if text[char]!="\"" and text[char]!=" " and text[char]!="\n":
                graph+=text[char]
    except:
        print("El tipo de grafica no fue ingresado")
        
    try:
        nombreInstruccion= re.search("titulo:",text)
        for char in range(nombreInstruccion.end(),len(text)):
            if text[char]=="," or text[char]=="?":
                title=title.upper()
                instructionDiccionary["Titulo"]=title
                break
            if text[char]!="\"" and text[char]!="\n":
                title+=text[char]
    except:
        instructionDiccionary["Titulo"]=None
        print("No hay titulo")
    
    try:
        nombreInstruccion= re.search("titulox:",text)
        for char in range(nombreInstruccion.end(),len(text)):
            if text[char]=="," or text[char]=="?":
                instructionDiccionary["TituloX"]=spelling(titleX)
                break
            if text[char]!="\"" and text[char]!=" " and text[char]!="\n":
                titleX+=text[char]
    except:
        instructionDiccionary["TituloX"]=None
        print("No hay titulo en x")

    try:
        nombreInstruccion= re.search("tituloy:",text)
        for char in range(nombreInstruccion.end(),len(text)):
            if text[char]=="," or text[char]=="?":
                instructionDiccionary["TituloY"]=spelling(titleY)
                print(instructionDiccionary["TituloY"])
                break
            if text[char]!="\"" and text[char]!=" " and text[char]!="\n":
                titleY+=text[char]
    except:
        instructionDiccionary["TituloY"]=None
        print("No hay titulo en y")

    for word in text:
        if(word=="?"):
            return print("Has leido todo")




