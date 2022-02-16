from tkinter import filedialog
from cargarData import spelling

instructionList = []


def cargarInstrucciones():
    instructionList.clear()
    prueba = filedialog.askopenfilename(title="Select A file")
    with open(prueba, "r") as archivo:

        ver = archivo.read()
        archivo.close()
    readFile(ver)
    return instructionList




def readFile(fileContent):
    for char in range(len(fileContent)):
        if(fileContent[char]=="¿"):
            readString(fileContent, char)
            break
        


def readString(fileContent, number):
    comma=0
    name=""
    graph=""
    title=""
    titleX=""
    titleY=""
    num=0
    for char in range(number, len(fileContent)):

        if(fileContent[char]=="?"):
            break

        if(comma ==0 and fileContent[char]=="\"" and fileContent[char]!=" "):
            for char2 in range(char+1, len(fileContent)):
                if(fileContent[char2]=="\"" or fileContent[char2]=="," ):
                    comma=1
                    instructionList.append(spelling(name))
                    print(instructionList[0])
                    num=char2
                    break
                name+=fileContent[char2]
        
        if(comma ==1 and fileContent[char]=="\"" and fileContent[char]!=" " and num<char):
            for char2 in range(char+1, len(fileContent)):
                if(fileContent[char2]=="\"" or fileContent[char2]=="," ):
                    comma=2
                    instructionList.append(spelling(graph))
                    print(instructionList[1])
                    num=char2
                    break
                graph+=fileContent[char2]        

        if(comma ==2 and fileContent[char]=="\"" and fileContent[char]!=" " and num<char):
            for char2 in range(char+1, len(fileContent)):
                if(fileContent[char2]=="\"" or fileContent[char2]=="," ):
                    comma=3
                    instructionList.append(spelling(title))
                    print(instructionList[2])
                    num=char2
                    break
                title+=fileContent[char2]  
        
        if(comma ==3 and fileContent[char]=="\"" and fileContent[char]!=" "and num<char):
            for char2 in range(char+1, len(fileContent)):
                if(fileContent[char2]=="\"" or fileContent[char2]=="," ):
                    comma=4
                    instructionList.append(spelling(titleX))
                    print(instructionList[3])
                    num=char2
                    break
                titleX+=fileContent[char2]
    

        if(comma ==4 and fileContent[char]=="\"" and fileContent[char]!=" " and num<char):
            for char2 in range(char+1, len(fileContent)):
                if(fileContent[char2]=="\"" or fileContent[char2]=="," ):
                    comma=5
                    instructionList.append(titleY)
                    print(instructionList[4])
                    num=char2
                    break
                titleY+=fileContent[char2]
          



