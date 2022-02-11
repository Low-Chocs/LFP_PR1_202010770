from itertools import product
from tkinter import filedialog
from io import open
from producto import producto as newProduct

productList=[]
def loadData():
    prueba = filedialog.askopenfilename(title="Select A file")
    with open(prueba, "r") as archivo:

        ver = archivo.read()
        archivo.close()
    readFile(ver)


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


def readValues(word):
    producto = ""
    price = ""
    quantity = ""
    count = 0

    for char in range(len(word)):

        if(word[char] == ","):
            count += 1
            continue
        elif(word[char] != "\"" and count==0):
            producto += word[char]
            continue
        elif(word != " " and count == 1):
            price += word[char]
            continue
        elif(word != " " and count == 2):
            quantity += word[char]
            continue

    print("El producto es: "+producto+" Con ventas de: " +
          str(price) + " Con la cantidad de: "+str(quantity))
    productList.append(newProduct(producto, price, quantity))
    
    


