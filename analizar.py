from cProfile import label
from itertools import product
from matplotlib import pyplot
import os
graphTitles={}
graphProducts=[]
graphSales=[]



def analizar(productList,instructions):
    graphTitles.clear()
    graphProducts.clear()
    graphSales.clear()

    #Se trata de ver si el archivo no ha sido creado anteriormente 
    try:
        os.remove(instructions["Nombre"]+".png")
    except:
        print()
    #Se le agrega el titulo a la grafica
    if(instructions["Titulo"]==None):
        pyplot.title("Ventas del mes de " + productList[0] + " del "+productList[1]+"")
    else:
        pyplot.title(instructions["Titulo"])
    graphProduct(productList)
    for i in graphProducts:
        print(i)

    #Grafica de barras
    if(instructions["Grafica"]=="Barras"):
    #Se agregan los titulos en x y "y"
        if(instructions["TituloX"]!=None):
            pyplot.xlabel(instructions["TituloX"])
        if(instructions["TituloY"]!=None):
            pyplot.ylabel(instructions["TituloY"])
        pyplot.bar(graphProducts, graphSales, width=0.8)
        pyplot.savefig(instructions["Nombre"]+".png")
        os.startfile(instructions["Nombre"]+".png")

    #Grafica de lineas 
    if(instructions["Grafica"]=="Lã\xadneas" or instructions["Grafica"]=="Lineas"):
        ordenamientoBurbuja(productList)
        graphProduct(productList)
        if(instructions["TituloX"]!=None):
            pyplot.xlabel(instructions["TituloX"])
        if(instructions["TituloY"]!=None):
            pyplot.ylabel(instructions["TituloY"])
        pyplot.plot(graphProducts, graphSales)
        print("Se realizará una gráfica de líneas")
        pyplot.savefig(instructions["Nombre"]+".png")
        os.startfile(instructions["Nombre"]+".png")
        
    #Grafica de pie
    if(instructions["Grafica"]=="Pie" or instructions["Grafica"]=="Pastel"):
        pyplot.pie(graphSales, autopct='%1.1f%%')
        pyplot.savefig(instructions["Nombre"]+".png")
        pyplot.legend(graphProducts)
        os.startfile(instructions["Nombre"]+".png")

#Se agregan los productos a una lista para ponerlos en la grafica
def graphProduct(productList):
    for char in range(2,len(productList)):
        graphSales.append(productList[char].getSales())
        graphProducts.append(productList[char].getProduct())

#Se realiza el ordenamiento burbuja, esto con el fin de mejorar la visualización de la grafica de líneas
def ordenamientoBurbuja(dataList):
    dataLen=len(dataList)
    dataList2=[]
    for lista in range(2,dataLen):
        for lista2 in range(2,dataLen-3):
            if(float(dataList[lista2].getSales())>float(dataList[lista2+1].getSales())):
                dataList2.append(dataList[lista2])
                dataList[lista2]=dataList[lista2+1]
                dataList[lista2+1]=dataList2[0]
                dataList2.clear()
    print()
    print("Lista ordenada")
    for i in range(2, len(dataList)):
        print(dataList[i].getSales())

