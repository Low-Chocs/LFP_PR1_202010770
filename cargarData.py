from itertools import product
from tkinter import filedialog
from io import open
from producto import producto as newProduct

productList = []


def loadData():
    prueba = filedialog.askopenfilename(title="Select A file")
    with open(prueba, "r") as archivo:

        ver = archivo.read()
        archivo.close()
    monthYear(ver)
    readFile(ver)
    showData()


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


# Function with the correct writing
def spelling(word):
    correctWord = word[0].upper()
    for char in range(1, len(word)):
        correctWord += word[char].lower()
    return correctWord


def showData():
    for data in productList:
        print("El producto es: "+data.getProduct()+" Con ventas de: " +
              data.getPrice() + " Con la cantidad de: "+data.getQuantity())


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
            print("El mes es: "+spelling(month))
            print("El año es: "+year)
            break

