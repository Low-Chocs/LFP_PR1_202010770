from calendar import month
from itertools import product
from tkinter import filedialog
from io import open
from producto import producto as newProduct

productList = []

#Función encargada de enviar la lista con la info del .data
def loadData():
    productList.clear()
    prueba = filedialog.askopenfilename(title="Select A file")
    print(prueba)
    
    with open(prueba, "r") as archivo:
        ver = archivo.read()
        archivo.close()
    #Encuentra el año y mes y lo agrega a la lista
    monthYear(ver)
    #Encuentra los productos
    readFile(ver)

    return productList


#Analiza los brakets, que identifica los objetos
def readFile(fileContent):
    for char in range(len(fileContent)):
        word = ""
        if(fileContent[char] == "["):
            firstBraket = char
        if(fileContent[char] == "]"):
            secondBraket = char
            for review in range(firstBraket+1, secondBraket):
                word += str(fileContent[review])
            readValues(word)

#Con el rango de donde estan los objetos, esta función busca crearlos
def readValues(word):
    producto = ""
    price = ""
    quantity = ""
    count = 0

    for char in range(len(word)):

        if(word[char] == ","):
            count += 1
            continue
        elif(word[char] != "\"" and count == 0):
            producto += word[char]
            continue
        elif(word != " " and count == 1):
            price += word[char]
            continue
        elif(word != " " and count == 2):
            quantity += word[char]
            continue
    productList.append(newProduct(spelling(producto), price, quantity))


# Hace una buena escritura de los elementos que se van a presentar
def spelling(word):
    correctWord = word[0].upper()
    for char in range(1, len(word)):
        correctWord += word[char].lower()
    return correctWord

#Muestra la info
def showData(list):
    print("El mes es: "+productList[0])
    print("El año es: "+productList[1])
    for data in range(2,len(list)):
        print("El producto es: "+list[data].getProduct()+" Con ventas de: " +
              list[data].getPrice() + " Con la cantidad de: "+list[data].getQuantity()
              +" Y ventas de: "+str(list[data].getSales()))


def monthYear(word):
    count = 0
    month = ""
    year = ""
    for char in word:
        if(char != ":" and count == 0 and char != " "):
            month += char
        if(char == ":"):
            count = 1
        if(char != ":" and count == 1 and char != " " and char!="="):
            year += char
        if(char == "="):
            productList.append(spelling(month))
            productList.append(year)
            break


