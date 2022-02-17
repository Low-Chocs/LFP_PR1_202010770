from matplotlib import pyplot

def analizar(productList,instructionList):
    if(instructionList[1]=="Barras"):
        print("Se realizará una gráfica de barras")
    if(instructionList[1]=="Líneas"):
        print("Se realizará una gráfica de líneas")
    if(instructionList[1]=="Pie" or instructionList[1]=="Pastel"):
        print("Se realizara una grafica de pie")

    slices=(100,30,20,50,10,128)
    colors=("red","red","red","red","red","red")
    pyplot.pie(slices,colors=colors)
    pyplot.show()
    
def pie():
    print()