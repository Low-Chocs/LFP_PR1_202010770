from cProfile import label
from matplotlib import pyplot
graphTitles={}
graphProducts=[]
graphSales=[]

def analizar(productList,instructions):
    if(instructions["Titulo"]==None):
        pyplot.title("Ventas del mes de " + productList[0] + " del "+productList[1]+"")
    else:
        pyplot.title(instructions["Titulo"])
    graphProduct(productList)
    for i in graphProducts:
        print(i)
    if(instructions["Grafica"]=="Barras"):
    
        if(instructions["TituloX"]!=None):
            pyplot.xlabel(instructions["TituloX"])
        if(instructions["TituloY"]!=None):
            pyplot.ylabel(instructions["TituloY"])
        pyplot.bar(graphProducts, graphSales, width=0.8)
        pyplot.savefig(instructions["Nombre"]+".png")
        pyplot.show()
    if(instructions["Grafica"]=="Lã\xadneas" or instructions["Grafica"]=="Lineas"):
        if(instructions["TituloX"]!=None):
            pyplot.xlabel(instructions["TituloX"])
        if(instructions["TituloY"]!=None):
            pyplot.ylabel(instructions["TituloY"])
        pyplot.plot(graphProducts, graphSales)
        print("Se realizará una gráfica de líneas")
        pyplot.savefig(instructions["Nombre"]+".png")
        pyplot.show()
    if(instructions["Grafica"]=="Pie" or instructions["Grafica"]=="Pastel"):
        pyplot.pie(graphSales, autopct='%1.1f%%', labels=graphProducts)
        pyplot.savefig(instructions["Nombre"]+".png")
        pyplot.show()

def graphProduct(productList):
    for char in range(2,len(productList)):
        graphSales.append(productList[char].getSales())
        graphProducts.append(productList[char].getProduct())

